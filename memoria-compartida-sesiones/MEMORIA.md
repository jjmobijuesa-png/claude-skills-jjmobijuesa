# MEMORIA — estado vivo

_Última actualización: 2026-09-26 (sesión nube "Ver otras sesiones de Claude Code")_

## Estado actual
- Sesiones locales visibles en app/teléfono vía `claude remote-control` (funciona).
- Bloqueo de uso: **tope de gasto mensual** (subir en claude.ai/settings/usage).
- Memoria compartida + relevo en caliente activos en `main` (hooks SessionStart, UserPromptSubmit, PostToolUse, Stop).
- Estrategia: la nube tiene más saldo; la PC vuelca en caliente y el espejo toma la posta sin comandos.
- Sesión nube "Skills repository link integrity audit": grafo de skills refactorizado
  en rama `claude/awesome-einstein-6h3af4`, pendiente de revisión/merge.

## Archivo principal en trabajo
- _Pendiente de identificar_ — subirlo al repo para que esté en PC y nube.

## Hilos con relevo
Un hilo = un agente de la PC = una carpeta en `relevos/` = un chat espejo en la nube. Nunca mezclar hilos en un mismo chat.

| Hilo (carpeta en `relevos/`) | Agente principal (PC) | Espejo (nube) | TURNO | Siguiente paso |
|---|---|---|---|---|
| `agente-ia-local-autoreflexivo` | Agente IA Local autoreflexivo | "Ver otras sesiones de Claude Code" (coordinador) | PC | Primer checkpoint desde la PC |
| `flujo-caja-proyeccion-mobijuesa` | Flujo de caja y proyección Mobijuesa | "Espejo — Flujo de caja y proyección Mobijuesa" | NUBE | Directriz y hoja de ruta listas; falta que la PC suba el Excel del modelo y los datos de la fase 0 |
| `financial-report-mobijuesa` | Financial report for Mobijuesa | "Espejo — Financial report for Mobijuesa" | PC | Primer volcado en caliente desde la PC |

## Pendientes
- [ ] Identificar y subir el archivo principal.
- [ ] Pegar `PROMPT-agente-local.md` en la sesión local (instala hooks SessionStart + Stop y hace el primer checkpoint).
- [ ] Pegar `relevos/flujo-caja-proyeccion-mobijuesa/PROMPT-pc.md` en la sesión local de flujo de caja.
- [ ] Pegar `relevos/financial-report-mobijuesa/PROMPT-pc.md` en la sesión local "Financial report for Mobijuesa".
- [ ] Revisar rama `claude/awesome-einstein-6h3af4`.
