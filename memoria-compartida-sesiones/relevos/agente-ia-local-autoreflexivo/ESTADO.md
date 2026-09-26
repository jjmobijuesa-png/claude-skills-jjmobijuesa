# RELEVO — Agente IA Local autoreflexivo

| Campo | Valor |
|---|---|
| **TURNO** | NUBE |
| Principal | Sesión local "Agente IA Local autoreflexivo" (PC, Remote Control) |
| Espejo | Sesión nube "Agente IA Local autoreflexivo - en la nube" (también coordinador de hilos) |
| Último checkpoint | 2026-09-26 00:18 (Guayaquil) — espejo nube: toma de posta |
| Motivo del último relevo | toma automática: PC detenida (tope de gasto mensual; sin volcado previo de la PC) |

## Tema / objetivo del hilo
_Pendiente de confirmar por la PC._ **Hipótesis del espejo:** el hilo trabaja sobre el
bucle autoreflexivo de aprendizaje de la skill `agente-local-autoreflexivo-bookmarks`
(bookmarks de X @fdc_ec → clasificación por tema → aumentar o crear skills `intereses-*`),
posiblemente extendido a LinkedIn (`linkedin-guardados-fedphd`) y a la memoria compartida.
La sesión de la PC acumuló ~400k tokens de contexto antes de detenerse.

## Razonamiento en curso
_No hay volcado de la PC:_ la sesión se detuvo antes de que existiera el protocolo de relevo,
así que su razonamiento solo está en esa conversación.

Lo que sí construyó el espejo en este hilo (sesión nube, 2026-09-26):
- La skill `memoria-compartida-sesiones` (MEMORIA, bitácora, RELEVO en caliente, hooks,
  plantilla de hilos, rol de coordinador). Nació como herramienta para este hilo.
- Los hilos `flujo-caja-proyeccion-mobijuesa` y `financial-report-mobijuesa`, cada uno con su
  propio espejo (no se razonan aquí).

## Archivos centrales
- _Ninguno todavía en `archivos/`._ La PC debe copiar el archivo principal y marcarlo.
- Contexto relacionado en el repo: `agente-local-autoreflexivo-bookmarks/SKILL.md`,
  `memoria-compartida-sesiones/PROMPT-agente-local.md` (prompt con toda la historia).

## Siguiente paso concreto
1. **PC** (cuando se libere el límite): pegar `memoria-compartida-sesiones/PROMPT-agente-local.md`.
   Instala los 4 hooks y hace el primer volcado: tema real, razonamiento en curso, archivo
   principal a `archivos/`, siguiente paso. Al ver TURNO = NUBE, lee este ESTADO y recupera la posta.
2. **Espejo**: con el volcado, continuar desde el siguiente paso que registre la PC.

## Bloqueantes
- 🔴 Sin volcado de la PC: el espejo no conoce el razonamiento ni el archivo principal del hilo.

## Pendientes / preguntas abiertas
- ¿Cuál es el archivo principal del hilo y en qué ruta está?
- ¿Confirma la PC que el tema es el bucle autoreflexivo de bookmarks, u otro?
- Usuario: el espejo viejo de flujo de caja y el "(en caliente)" siguen activos; elegir uno.
