---
name: intereses-proteccion-patrimonial
description: |
  Skill de consulta y síntesis sobre 'Protección patrimonial / estructuras
  societarias' a partir de 51 bookmarks curados por @fdc_ec en X.com.
  Cubre: empresas fantasmas vs. planificación patrimonial legítima,
  holdings familiares, fideicomisos / trusts, offshore vs. UBO / CRS /
  FATCA, estate tax para No Residentes Extranjeros, costos de setup y
  mantenimiento, y casos arquetípicos. Invocar cuando el usuario o un
  agente necesite respaldar una afirmación sobre estructuración
  patrimonial con la curación real del usuario.
trigger_phrases:
  - "qué tengo sobre empresas fantasmas"
  - "estructuras patrimoniales que sigo"
  - "holding family office"
  - "offshore beneficial owner"
  - "protección patrimonial"
  - "fideicomiso trust"
  - "testaferro estructuración"
  - "ocultamiento patrimonial legal"
idioma_de_salida: español neutro
nivel_madurez: aplicada
fuente: bookmarks @fdc_ec exportados 2026-06-23 (51 entradas del tema)
creada_manualmente: true
razon_creacion_manual: |
  El tema (51 bookmarks) está bajo el umbral 100 del autoreflex_pipeline.
  Se creó manualmente por instrucción explícita del usuario en sesión
  2026-06-23 tras consulta sobre empresas fantasmas y planificación
  patrimonial. El umbral del pipeline se redujo a 50 simultáneamente.
---

# Protección patrimonial / estructuras societarias — Skill de consulta

## Doctrina

Esta skill expone lo que el usuario ha **curado** sobre estructuración
patrimonial. NO es asesoría legal. Distingue siempre entre:

- **Planificación patrimonial legítima** (UBO declarado al regulador,
  CRS-compatible, holding familiar SAS Ecuador con accionistas
  visibles, fideicomiso mercantil con beneficiario informado).
- **Ocultamiento ilícito** (testaferro al frente, capas anónimas en
  jurisdicciones sin registro UBO, "consultoría" desde fundación dueña).

La frontera operativa: **declarar el UBO al regulador competente** (SRI,
SEPS, Sucre, equivalente extranjero) aunque la estructura sea opaca al
mercado.

## Cómo usarla

1. Leer `references/sintesis-empresas-fantasmas-ocultamiento-legal.md`
   — síntesis curada el 2026-06-23 con las URL canónicas del corpus.
2. Para consultas finas, correr:
   ```
   python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
          --tema "patrimonial" --query "<keyword>" --top N
   ```
3. Siempre citar URL canónica del tweet.
4. Si una afirmación no está en el corpus, decirlo: **no inventar**.

## Voces curadas (top)

| Cuenta | Bookmarks | Especialidad |
|--------|-----------|--------------|
| @otolz_ | 7 | Hilo didáctico en español: anatomía de la estructura ultra-rica |
| @marianosardans | 3 | Estructurador argentino: costos, NRA estate tax, co-titularidad |
| @talkingaboutax | 2 | Estudio académico de 65 países, 3 patrones |
| @maximumpain333 | 2 | Casos geopolíticos |
| @shanaka86 | 2 | Casos sancionatorios |
| @Pacto_Secreto | 2 | Crítica al sistema |

## Compuertas 🚦

1. **No es asesoría legal.** Recomendar consultar a abogado tributario
   ecuatoriano o internacional licenciado.
2. **Curar ≠ firmar.** Que el usuario tenga bookmarks de @otolz_ no
   significa que apruebe el modelo agresivo descrito.
3. **No inventar jurisdicciones, leyes ni costos.** Si no está en el
   archivo, declararlo.
4. **Marco normativo aplicable al usuario (Ecuador)**: COMYF, Ley de
   Compañías 2025, SAS, fideicomiso mercantil, Reglamento UBO SRI,
   FATCA + CRS desde 2018.
5. **Tópicos sensibles**: discutir mecanismos sin entregar guías
   operativas para ocultamiento — esto es una skill de **consulta**, no
   de receta.

## Relacionado

- [[consulta-bookmarks-fdc-ec]] — patrón de consulta general.
- [[agente-local-autoreflexivo-bookmarks]] — meta-skill que orquesta.
- [[memoria-financiera-inteligenciada]] — backbone financiero del usuario.
- [[politica-retiros-socio-propietario]] — para la separación de sueldo
  / dividendo / capital en empresas familiares (Quevepalma, Vista al Río).
- [[estrategia-implementacion-juridica]] — para artículos sobre marco
  ecuatoriano.
