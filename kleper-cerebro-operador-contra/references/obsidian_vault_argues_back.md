# Obsidian: A Vault That Argues Back

**Fuente:** https://x.com/Nazik2053/status/2082370975132225737
**Autor:** Nazar (@Nazik2053)
**Fecha:** 2026-07-29T07:41:43.000Z
**Recuperado:** 2026-07-29 via api.fxtwitter.com (blocks + entityMap COMPLETO, incluye bloques de codigo)

> Transcripcion literal, fuente citable de [[kleper-cerebro-operador-contra]]. Curar != firmar.

---

Everyone building a second brain builds the same thing. It catches duplicates, surfaces patterns, flags dropped threads. What none of them do is disagree with you.

The best argument against your last decision is already in your vault. You wrote it eight months ago and forgot.

Your notes aren't neutral. They hold several versions of you, each with different conclusions. The you from 2023 thought X. The you from six months ago thought the opposite. Both are still in there. Neither is talking to the other, because you were the only one ever holding the conversation.

This is a build for the layer nobody ships: a vault that runs the argument for you, on a schedule.


---


## Why a loop, not another chat tab

You can already open Claude, paste a note, and type "argue against this". It works once. Close the tab and the argument stops.

The value shows up when the argument runs on its own. Every idea in the vault gets steelmanned against your other notes automatically, without you remembering to ask. The friction the vault was built to remove - finding notes - gets replaced by the friction it stayed silent about: finding contradictions.


---


## DO passes vs CONTRA passes

Every second brain article talks about DO passes:

- extract ideas
- find patterns
- link related notes
- surface old work
This one is about CONTRA passes:

- steelman the strongest counterargument
- surface contradictions between your own notes
- cross-pollinate concepts from unrelated domains
- run the "ghost self" - you from six months ago debating you from today
The DO layer finds what fits together. The CONTRA layer finds what doesn't.


---


## The stack

Three pieces, nothing exotic.

The vault. Obsidian, local markdown. Every note readable and writable by a script. No API wall between you and your own thinking.

The engine. Claude, split by role. A stronger model for judgment work - steelmanning, contradiction detection, cross-domain analogies. A cheaper model for tagging, indexing, and parsing. You don't spend the expensive model to check a filename.

The trigger. A cron job or a file watcher. No new app, no dashboard - the same automation tool you already use.


---


## Loop 1 - ingestion with argument tags

Loop 1 does what every ingestion loop does, plus one extra field.


```
TRIGGER: new note added or existing note edited
STEPS:
  1. Read the note
  2. Extract the core claim being made
  3. Identify the assumption behind that claim
  4. Add three fields to frontmatter:
     ---
     claim: [what the note asserts]
     assumption: [what must be true for the claim to hold]
     ready_for_contra: false
     ---
  5. If the assumption is unclear, flag the note for review
VERIFY: every processed note has claim and assumption filled
STOP:   verify passes, or flag after 2 retries
```

The assumption field is the unlock. Without it, contradictions look like disagreements. With it, they look like arguments about premises. Two notes that seem to clash usually rest on different assumptions - make the assumption explicit and the argument becomes tractable.


---


## Loop 2 - the contrarian loop

This is the part no article ships out of the box. Four passes, each with its own job.

TRIGGER: every 6 hours


```
STEPS:

Pass 1 - steelman:
  Pick 5 notes at random. For each, write the strongest
  counterargument using material from other notes in the
  vault. Save as: [note-title]-contra.md

Pass 2 - contradictions:
  Compare assumption fields across all notes. Find pairs
  where one note's assumption conflicts with another
  note's claim. Log the collision in memory/CONTRA.md
  with direct quotes from both notes.

Pass 3 - cross-domain:
  Pick one technical note and one personal or
  philosophical note. Force an analogy between them.
  Record it in memory/BRIDGES.md.

Pass 4 - ghost self:
  Load all notes older than 6 months on the same topic
  as any note edited in the last 14 days. Write a short
  paragraph in the voice of past-you reacting to
  current-you. Save to memory/GHOST.md.

VERIFY: each pass writes at least one entry.
        Pass 2 collisions include real quotes.
        Pass 4 uses only quotes from old notes.
STOP:   all four passes complete, or a pass logs and moves on
```

Pass 4 is the one that changes how you use the vault. Reading past-you tell future-you that you're rationalizing hits differently than reading a bullet list of similar ideas.


---


## Never auto-merge the contradictions

Two notes that contradict each other aren't necessarily wrong. They might be about different contexts, constraints, or phases. A steelman is a suggestion, not a verdict.

Keep a human on merges and corrections. The loop surfaces, you decide. The moment you let it auto-resolve, it will merge two notes about "quitting a bad client" that were actually about two different clients, and you lose the reasoning that made both right at the time.


---


## Prove it by hand first

Before you schedule anything, run this against your real notes in a single chat:

Read every note in [folder].


```
For each note:
1. Extract the core claim
2. Find one other note where the assumption conflicts
   with this claim
3. Write the steelman of the opposite position, using
   direct quotes from both notes

Success criteria (strict, no soft passes):
- every steelman quotes both notes directly
- every contradiction pair identifies the assumption gap
- no vague "you might reconsider X" output

LOOP PROTOCOL, repeat every turn:
1. PLAN   - state the single next step
2. DO     - produce or improve the output
3. VERIFY - score 1-10 on each criterion, be brutally honest
4. DECIDE - if every criterion is 8+, print "FINAL" and stop

Begin. Run the loop until FINAL.
```

Run it a few times. If what comes back genuinely makes you rethink something, the loop earns a schedule. If it doesn't, don't automate it. Manual proof first, always.


---


## What it costs

Loop 1 runs once per note change - a handful of cheap-model calls, a fraction of a cent each. Not recurring.

Loop 2 runs four passes every six hours. Put the steelman and cross-domain passes on the stronger model, since they need real judgment. Put contradictions and quote extraction on the cheap model.

Sixteen passes a day comes out to roughly the price of one coffee. If the loop catches a single contradiction that stops a bad decision, it pays for a year of itself in one afternoon.


---


## The order that actually works

Build Loop 1 first. Let the vault fill with claim and assumption metadata for at least three weeks - the loop needs material to argue against.

Add Pass 2 (contradictions) by hand a few times. If the collisions surprise you, schedule it.

Then Pass 4 (ghost self). This one needs about three months of history to feel real. Ghost self on a young vault is just guessing.

Add Pass 1 (steelman) and Pass 3 (cross-domain) last. They're the fun ones, but they only land once you have critical mass.

Don't schedule everything on day one. A loop running against three notes will hallucinate connections and train you to ignore the output. Prove each pass by hand, then automate.


---


## What this actually means

Every second brain promises the same thing: it never forgets, it notices patterns, it becomes a living wiki. Fine - that's the DO layer.

This adds the CONTRA layer. Not "here's what fits together" but "here's what doesn't fit, and both parts came from you".

The point isn't that the vault remembers everything. It's that the vault argues with itself in ways you never would, and every argument surfaces something you should have caught yourself.

Your best advisor isn't Claude. It's you from eight months ago, still writing in your vault, waiting for something to translate what you wrote into a language present-you will actually listen to.

The loop is that translator.

Written for nazik3502. If you build it, post a real CONTRA.md collision from your own vault - the proof is a contradiction that actually made you stop.
