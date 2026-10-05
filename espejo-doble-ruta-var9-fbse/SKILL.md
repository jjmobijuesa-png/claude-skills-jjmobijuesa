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

## Vecindad en la red
[[estilo-entregables-publicos-fbse]] · [[mapa-estado-ecuador-ibpp]] · [[memoria-compartida-sesiones]] ·
[[gobernanza-datos-financieros-ia]]
