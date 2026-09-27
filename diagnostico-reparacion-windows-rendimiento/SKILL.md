---
name: diagnostico-reparacion-windows-rendimiento
description: |
  Diagnostica y repara CAÍDAS DE APLICACIONES y LENTITUD en este
  Windows 11 (Dell, i7-1255U, 32 GB RAM). Ordena el diagnóstico de modo
  que primero DESCARTA hardware, luego mide MEMORIA VIRTUAL, y solo
  después culpa al software — al revés de como suele hacerse.

  Hallazgo fundacional (2026-07-27): el equipo tenía el **ARCHIVO DE
  PAGINACIÓN COMPLETAMENTE DESACTIVADO** (`pagefile.sys` inexistente,
  `AutomaticManagedPagefile=False`, límite de confirmación idéntico a la
  RAM física = margen 0). Con 0 de margen, cualquier pico de memoria no
  se pagina: **falla la reserva y la aplicación MUERE en el acto**.
  Firma inconfundible: `msedge.exe` con excepción **`e0000008`** (en
  Chromium = «sin memoria») mientras el Administrador de tareas todavía
  muestra RAM libre, y **cero** pantallazos azules.

  Incluye `diagnostico_sistema.ps1` (sin elevación) y
  `REPARAR_ADMIN.bat` (un clic, elevado) que reactiva la paginación,
  pone los emuladores en Manual y purga la cola de impresión.

trigger_phrases:
  - "el computador está lento / se cae todo"
  - "se cierra solo Edge / Claude / NotebookLM / YouTube"
  - "no se cargan los archivos en pantalla"
  - "parece que no alcanza la memoria"
  - "diagnostica el sistema / revisa la computadora"
  - "unknown software exception"

idioma_de_salida: español
nivel: aplicada
dominio: operaciones / rendimiento de Windows
metadata:
  version: 1.0
  fecha: 2026-07-27
  equipo: Dell · i7-1255U (10 núcleos / 12 hilos) · 31,7 GB RAM · Iris Xe · C: 930 GB
  scripts:
    - scripts/diagnostico_sistema.ps1
    - scripts/REPARAR_ADMIN.bat (+ .ps1)
  relacionada:
    - agente-gui-autoaprobado-windows
    - impresion-local-hp-diagnostico
    - ui-tars-desktop-control-local
---

# Skill `diagnostico-reparacion-windows-rendimiento`

## Resultado verificado del caso fundacional (2026-07-27)

| Indicador | Antes | Después |
|---|---|---|
| Archivo de paginación | **inexistente** | `C:\pagefile.sys` activo, gestionado |
| Límite de confirmación | 31,69 GB | **33,69 GB** |
| **Margen virtual** | **0 GB** | **2 GB (y crece bajo demanda)** |
| **Memory Compression** | **702 MB** | **0 MB** |
| RAM libre (recién arrancado) | 11 GB | **20,6 GB** |
| Entradas de arranque (HKCU) | 12 | **0** |
| Servicios WSA | Automático | Manual (detenidos) |

La caída de *Memory Compression* de 702 MB a **0** es la prueba más
limpia: Windows ya no necesita comprimir RAM a la desesperada porque
por fin tiene dónde paginar.

## Doctrina: el orden del diagnóstico

Ante «todo se cae y está lento», el instinto es culpar a la RAM o al
disco. **El orden correcto es otro**, porque separa causas que se
parecen mucho:

1. **¿Cae el NÚCLEO o caen las APLICACIONES?**
   `Kernel-Power 41` (apagón inesperado) y `BugCheck` (pantallazo azul).
   - **Ambos en 0** → el hardware y los drivers están bien. Deja de
     buscar RAM defectuosa: el problema es de software o de memoria
     virtual. *(Este fue el caso.)*
   - Alguno > 0 → sí hay sospecha de hardware: `mdsched` (memoria),
     temperatura, drivers.
2. **¿Hay MARGEN de memoria virtual?**
   `Límite de confirmación − RAM física`. Si da **0**, no hay archivo de
   paginación y el sistema está a un pico de distancia del fallo.
3. **¿QUÉ módulo falla exactamente?**
   Evento 1000 del registro Aplicación: da app + DLL culpable + código
   de excepción. Ahí se distingue «sin memoria» de «bug de un plugin».
4. **¿Qué carga permanente hay?** Arranque automático, emuladores, VMs.

## Tabla de códigos de excepción (lo que realmente significan)

| Código | Significado | Qué hacer |
|---|---|---|
| **`e0000008`** | **Sin memoria** (lo lanza Chromium/Edge al fallar una reserva) | Revisar paginación y commit. **No** es «Edge dañado» |
| `c0000005` | Violación de acceso | Bug del módulo nombrado (plugin, complemento, driver) |
| `c0000409` | Desborde de búfer de pila | Bug de la app; actualizarla |
| `c00001ad` | Sin recursos de gráficos/compositor (`dwm.exe`) | Presión de memoria o driver de video |

## 🚦 El error clásico que esta skill evita

> **«Hay RAM libre, así que no es memoria.»** FALSO.
> Windows no limita por RAM libre sino por el **límite de confirmación**
> (commit). Sin archivo de paginación, ese límite es la RAM física y
> **no hay válvula de escape**: cuando una app pide un bloque grande y
> el commit está cerca del tope, la reserva falla y el proceso muere —
> aunque el Administrador de tareas muestre gigas «libres».
> Señal de apoyo: el proceso **«Memory Compression»** crecido (Windows
> comprimiendo RAM porque no tiene disco donde paginar).

## Por qué NO se debe desactivar el archivo de paginación
Circula el consejo de «desactivar la paginación si tienes mucha RAM
para que vaya más rápido». Es **falso y dañino**:
- Windows usa el commit como contabilidad, no solo como respaldo.
- Sin él no se pueden generar volcados de fallo.
- Aplicaciones modernas (navegadores, Electron, Office, IA local)
  **reservan** mucha más memoria de la que tocan; sin paginación esas
  reservas fallan.
Lo correcto es **gestionado por el sistema** (Windows lo dimensiona y
solo ocupa disco cuando hace falta).

## Protocolo

> **Tómate tu tiempo. Calidad antes que velocidad.**

### 1. Diagnosticar (sin elevación)
```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\datos\.claude\skills\diagnostico-reparacion-windows-rendimiento\scripts\diagnostico_sistema.ps1"
```
Da los 5 bloques: memoria/commit · descarte de hardware · quién se cae y
por qué · carga permanente · disco.

### 2. Reparar (un clic, elevado)
`scripts\REPARAR_ADMIN.bat` → **clic derecho → Ejecutar como
administrador**. Reactiva la paginación gestionada, pone WSA/BlueStacks
en Manual y purga la cola de impresión. Deja `reparacion_log.txt`.
**Reiniciar** para que la paginación entre en vigor.

### 3. Aligerar el arranque (sin elevación)
Quitar de `HKCU:\...\CurrentVersion\Run` lo que no se use a diario
(emuladores, actualizadores). Guardar respaldo del valor antes.

## 🚦 Límite real: el UAC en escritorio seguro
En este equipo `PromptOnSecureDesktop=1`. **El escritorio seguro del UAC
NO es automatizable** — ni por computer-use, ni por UI-TARS, ni por
tarea programada (registrarla también exige elevación). No es una
limitación del agente: es una frontera de seguridad de Windows y
**no debe intentar sortearse**. Por eso las reparaciones elevadas se
empaquetan en **un solo .bat** para que el usuario dé **un único clic**.
Ver [[agente-gui-autoaprobado-windows]] (que sí cubre todo lo demás).

## Cómo depurar si falla
- **El .bat dice «no eres administrador»**: se abrió con doble clic;
  hay que usar clic derecho → Ejecutar como administrador.
- **Tras reiniciar el margen sigue en 0**: una directiva de grupo o una
  «app optimizadora» está desactivando la paginación de nuevo; revisar
  software de «limpieza/tuning» instalado.
- **Sigue cayéndose una app concreta**: mirar su módulo en el paso 3; si
  es un complemento (p. ej. `MsoAria.dll` de Office), actualizar o
  desactivar ese complemento — eso es un bug aparte, no memoria.

## Portabilidad (revisar el 20%)
Las rutas, el nombre de los servicios de emulador y los umbrales. La
doctrina (orden del diagnóstico, commit vs RAM libre, tabla de códigos)
es estable y aplica a cualquier Windows 10/11.

## Relacionado
- [[agente-gui-autoaprobado-windows]] — qué sí puedo automatizar por GUI.
- [[impresion-local-hp-diagnostico]] — la purga del spooler también vive aquí.
- [[selector-modelo-claude-optimo]] · [[eficiencia-generacion-respuestas]].

## Vecindad en la red

Skills de mantenimiento que dependen de esta y que antes no la citaban de vuelta:

- [[forense-cuelgues-y-caidas-windows]]
- [[saneamiento-complementos-office]]
- [[escanear-a-pdf-sin-dependencias]]

> Puente tendido el 9-sep-2026: este racimo estaba conectado entre sí pero desprendido del cuerpo principal ([[regla-del-primer-tropiezo]] §10).

## Política de actualizaciones: seguridad SÍ, drivers NO (27-sep-2026)

**La pregunta no es «¿actualizo o no?». Es «¿qué tipo de actualización?»** —
Windows las mezcla a propósito y tienen riesgos opuestos.

| Tipo | Qué hacer | Por qué |
|---|---|---|
| **Seguridad** (`KB` + «Security Update») | **Siempre, sin excepción** | Tapan agujeros que ya se explotan. Desactivarlas no ahorra latencia: abre la puerta |
| **Drivers por Windows Update** | **Excluir** | Microsoft sirve versiones genéricas, a veces MÁS VIEJAS que las instaladas, y pisan lo que ya funciona |
| **Funciones** (saltos de versión anuales) | **Diferir semanas**, no rechazar | Los fallos gordos salen los primeros días |

### La prueba de que los drivers de WU son un retroceso
En este Dell Inspiron 15 3520, Windows Update ofrecía un driver del monitor LG
cuyo propio detalle decía **«released in March, 2016»** — diez años de atraso
sobre el genérico que ya funcionaba. Junto a él, un Intel Display de 525 MB que
tocaría justo el monitor principal (ver `feedback_monitor_primario_apagado`).

### El ajuste quirúrgico
`scripts/` no lo lleva; el script vive en el scratchpad de la sesión
(`drivers_fuera_de_wu.ps1`, con `-Revertir` y respaldo en JSON). Son dos valores,
ambos en HKLM y ambos con administrador:

| Llave | Valor | Efecto |
|---|---|---|
| `…\Policies\Microsoft\Windows\WindowsUpdate` → `ExcludeWUDriversInQualityUpdate` | `1` | Los drivers no viajan en las actualizaciones de calidad |
| `…\CurrentVersion\DriverSearching` → `SearchOrderConfig` | `0` | No buscar drivers en Windows Update |

🚦 **`ExcludeWUDriversInQualityUpdate` es directiva de Windows Update for
Business y esta máquina es Windows 11 HOME, que a veces las ignora.** La que sí
funciona con seguridad en Home es `SearchOrderConfig = 0`. No dar por hecho el
efecto de la primera: la prueba es de comportamiento, con el tiempo.

### Cómo comprobar el estado sin instalar nada
La búsqueda por COM es de solo lectura y separa los dos canales:

```powershell
$sr = (New-Object -ComObject Microsoft.Update.Session).CreateUpdateSearcher()
$sr.Search("IsInstalled=0 and IsHidden=0 and Type='Software'").Updates.Count  # seguridad
$sr.Search("IsInstalled=0 and IsHidden=0 and Type='Driver'").Updates.Count    # drivers
```

Mirar además `AutoSelectOnWebSites` e `IsMandatory` de cada uno: si ambos son
`False`, ese driver **es opcional** y Windows no lo iba a instalar solo. El
riesgo real entonces no es Windows, es pulsar «instalar todo» en la ventana.

### Contrapartida que hay que decirle al usuario
Al cortar esta vía, **revisar Dell SupportAssist o Intel DSA una o dos veces al
año pasa a ser tarea suya**. El olvido es el riesgo de esta opción, y hay que
nombrarlo al recomendarla.

Relacionado: [[forense-cuelgues-y-caidas-windows]] ·
`feedback_monitor_primario_apagado` · `feedback_camara_bloqueada_es_camara_virtual`.
