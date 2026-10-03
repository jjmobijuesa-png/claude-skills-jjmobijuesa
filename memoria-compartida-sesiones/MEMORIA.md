# MEMORIA — estado vivo

_Última actualización: 2026-09-29 (coordinador: sesión nube "Agente IA Local autoreflexivo - en la nube")_

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
| `agente-ia-local-autoreflexivo` | Agente IA Local autoreflexivo | "Agente IA Local autoreflexivo - en la nube" (también coordinador) | NUBE | PC: comandos §7/§8 de `AUDITORIA_RED.md`, regenerar `skills_network.md`; luego fusionar PR #1 |
| `flujo-caja-proyeccion-mobijuesa` | Flujo de caja y proyección Mobijuesa | "Espejo — Flujo de caja y proyección Mobijuesa" (hay un duplicado "(en caliente)"; ver aviso A4) | NUBE | Ver su ESTADO (Excel v2 + ESCENARIOS) |
| `financial-report-mobijuesa` | Financial report for Mobijuesa | "Espejo — Financial report for Mobijuesa" | PC | Ver su ESTADO (modelo San Sebastián, PPTX, PDFs A4) |
| `agente-integrado-estudios-generales` | Agente integrado de estudios generales | "Espejo — Agente integrado de estudios generales" | NUBE | Espejo: redactar el MC3 (estadística) tras el OK de Francisco; base en `archivos/volcado-pc-01.md` |
| `ingenieria-de-prompts` | Ingienería de prompts | "Espejo — Ingienería de prompts" | PC | Primer volcado en caliente desde la PC |
| `junta-politica-financiera-blockchain-soberana` | Ecuador financial policy blockchain integration (por crear en la PC) | La sesión nube del mismo nombre trabaja como principal | NUBE | Matriz artículo por artículo con el informe de primer debate; falta acceso a la carpeta de Drive |
| `ibpp-ecualedger-soberana` | IBPP - EcuaLedger Soberana (id PC pendiente) | "Espejo — IBPP - EcuaLedger Soberana" | PC | Primer volcado en caliente desde la PC; hilo hermano de `junta-politica-financiera-blockchain-soberana` |

Avisos vigentes para todos los agentes: `AVISOS.md` (el hook los muestra en cada respuesta).
Registro de espejos con ids de sesión: `ESPEJOS.md`. Espejos nuevos: skill `espejo-automatico-remote-control`.

## Regla de datos y excepciones
- Regla general: `relevos/<hilo>/archivos/` solo lleva resúmenes y punteros en `.md`
  (candado `.gitignore`; rige `gobernanza-datos-financieros-ia`).
- **Excepción aprobada por Francisco (2026-09-28):** el hilo `flujo-caja-proyeccion-mobijuesa`
  puede guardar el Excel real de flujo de caja de Mobijuesa en su `archivos/` (repo privado),
  para que el espejo trabaje sobre el modelo real. Ningún agente debe borrarlo ni ponerle
  candado a esa carpeta por su cuenta. La excepción no se extiende a otros hilos ni a otros datos
  (cédulas, escrituras, expediente COAC, Belén, San Sebastián).

## Pendientes
- [ ] Identificar y subir el archivo principal.
- [ ] Pegar `relevos/flujo-caja-proyeccion-mobijuesa/PROMPT-pc.md` en la sesión local de flujo de caja.
- [ ] Pegar `relevos/financial-report-mobijuesa/PROMPT-pc.md` en la sesión local "Financial report for Mobijuesa".
- [ ] PR #1 (`claude/awesome-einstein-6h3af4`): verificación en disco desde la PC y merge.
- [ ] Pegar `relevos/agente-integrado-estudios-generales/PROMPT-pc.md` en la sesión local de estudios generales (si no tiene los hooks).
- [ ] Elegir un solo espejo para flujo de caja y archivar el otro.
