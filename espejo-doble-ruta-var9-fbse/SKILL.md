---
name: espejo-doble-ruta-var9-fbse
description: |
  REGLA PERMANENTE (Francisco Duque, 4-oct-2026, vigente hasta nueva orden): todo lo que se cree o
  modifique para la FBSE en «var 9 FBSE» debe quedar actualizado SIMULTÁNEAMENTE en las dos rutas:
  E:\vars\var 9 FBSE  y  G:\Mi unidad\var 9 FBSE (Google Drive). Esta skill indica cuándo y cómo
  sincronizar, con un script bidireccional que nunca borra y siempre conserva la versión más reciente.

  Úsala SIEMPRE al terminar cualquier tarea que escriba en «var 9 FBSE» (cartas, paquetes, PDF
  unificados, publicaciones, presentaciones, convenios), y antes de leer un archivo que el usuario
  pudo haber editado en Drive.
trigger_phrases:
  - "var 9 FBSE"
  - "actualiza en ambas rutas"
  - "sincroniza con el Drive"
  - "G:\\Mi unidad\\var 9 FBSE"
idioma_de_salida: español neutro, usted
nivel_madurez: aplicada (4-oct-2026)
fuente: hilo JRPFM
---

# Espejo de doble ruta: var 9 FBSE

## Regla
- **Ruta de trabajo:** `E:\vars\var 9 FBSE`, donde escriben los generadores.
- **Ruta espejo:** `G:\Mi unidad\var 9 FBSE` (Google Drive para escritorio, cuenta mobijuesa360).
- Al cerrar cada tarea, **ejecutar el espejo**. No basta con copiar «lo que creo que cambió».

## Cómo
```bash
python "E:/vars/var 9 FBSE/Tokenizacion Activos Reales - RWA/1 Matriz de Acuerdos/JRPFM/_generador_paquetes/espejo_var9_fbse.py"
# u otras subrutas relativas a la raíz «var 9 FBSE»:
python ".../espejo_var9_fbse.py" "Tokenizacion Activos Reales - RWA\BlockChain Soberana\Nuevas Publicaciones IN"
```
- Usa `robocopy /E /XO` **en los dos sentidos**: gana la versión más reciente y **nunca borra**
  (sin `/MIR` ni `/PURGE`).
- Excluye los documentos nativos de Google (`*.gdoc`, `*.gsheet`, `*.gslides`…): no son copiables
  y provocan el error 1 de robocopy, «Función incorrecta». Excluye también `~$*` y `desktop.ini`.
- Códigos de robocopy: del 0 al 7 es éxito; 8 o más es error. El script lanza la excepción con el
  detalle.

## Cuidados
- Si el usuario editó un archivo en Drive, el espejo lo trae a E: (por /XO). Regenerar después
  desde E: puede pisar esa edición: **leer primero el archivo de G: si es más reciente**.
- Un archivo abierto en un visor bloquea la copia (Device busy): avisar y reintentar al cerrarlo.
- ⭐ **G: NO es disco: es la unidad virtual de Google Drive, y puede dejar de responder a mitad
  de un proceso largo (11-oct-2026).** Un generador que recorría `G:` perdió el acceso tras una
  hora y, al comprobar `Path.exists()`, concluyó que **siete carpetas no tenían su archivo de
  texto** y las saltó sin error: el proceso terminó «con éxito» habiendo hecho la mitad.
  **Regla: todo proceso largo recorre y escribe en `E:` (disco físico) y espeja a `G:` pieza a
  pieza, en caliente.** Espejar solo al final pierde lo producido si el proceso se corta.
  Mismo mecanismo que [[feedback_linkedin_corpus_pisado_por_cosecha_vacia]]: el delator no es
  un error, es un conteo que no cuadra. Comprobar siempre **cuántas piezas** se produjeron
  frente a cuántas se esperaban, y no fiarse del código de salida.

- ⭐ **Rutas de más de 259 caracteres en `G:` (28-oct-2026).** Fallan con `WinError 3` o «cannot
  open file» **aunque se use el prefijo `\\?\`** (la unidad de Drive no lo acepta). La salida es
  montar la carpeta como unidad temporal y trabajar con rutas cortas:
  `subst W: "G:\Mi unidad\var 9 FBSE\…\1 Matriz de Acuerdos"` … `subst W: /d`. Comprobación barata:
  `len(ruta)` antes de copiar. Y nombrar las carpetas nuevas en corto.
- ⭐ **Nunca borrar y recrear en `G:` una carpeta con el mismo nombre (28-oct-2026).** Drive la deja
  en un estado transitorio: al listarla da «Acceso denegado» (error 5), sus archivos devuelven «ruta
  no encontrada» (error 3) y al final **Drive borró la carpeta junto con lo recién copiado**. Además, el
  borrado arrastra lo que el usuario haya puesto dentro (PDF firmados, RAR). **Regla:** sobrescribir
  archivo por archivo; borrar solo carpetas obsoletas con otro nombre. Lo borrado en `G:` se recupera
  desde la Papelera de Drive durante 30 días.
- 🚦 **El 28-oct-2026 el disco `E:` no estaba montado.** Sin `E:`, se trabaja directamente sobre `G:`,
  pieza a pieza, contando las piezas; el espejo se ejecuta cuando `E:` vuelva.

## Vecindad en la red
[[estilo-entregables-publicos-fbse]] · [[mapa-estado-ecuador-ibpp]] · [[memoria-compartida-sesiones]] ·
[[gobernanza-datos-financieros-ia]]
