// Snippet de JavaScript reutilizable para enviar una query a Perplexity
// y leer la respuesta vía Chrome MCP (mcp__Claude_in_Chrome__javascript_tool).
//
// Pasos:
//   1. Localizar el textarea de Perplexity (selector probado:
//      'textarea[placeholder]' sin id estable).
//   2. Setear su valor + dispatch input event (React necesita el evento).
//   3. Encontrar el botón Send (aria-label "Submit" o Enter).
//   4. Esperar a que aparezca el bloque de respuesta.
//   5. Devolver el texto.
//
// Uso desde Claude:
//   mcp__Claude_in_Chrome__javascript_tool({
//     action: "javascript_exec",
//     tabId: <tab>,
//     text: <contenido de submit_query.js, con QUERY reemplazado>
//   });

const QUERY = "__QUERY_PLACEHOLDER__";

// 1) localizar textarea (Perplexity usa textarea sin id estable; buscamos
//    el primero contenteditable o textarea visible en el body principal).
const ta = document.querySelector(
  'textarea[placeholder], div[contenteditable="true"][data-lexical-editor]'
);
if (!ta) {
  return JSON.stringify({error: "no textarea encontrado"});
}

// 2) setear valor — para React usar nativeInputValueSetter
const nativeSetter = Object.getOwnPropertyDescriptor(
  window.HTMLTextAreaElement.prototype, "value"
).set;
if (ta.tagName === "TEXTAREA") {
  nativeSetter.call(ta, QUERY);
} else {
  ta.innerText = QUERY;
}
ta.dispatchEvent(new Event("input", {bubbles: true}));
ta.focus();

// 3) submit con Enter (Perplexity acepta Enter en el textarea)
await new Promise(r => setTimeout(r, 300));
ta.dispatchEvent(new KeyboardEvent("keydown", {
  key: "Enter", code: "Enter", keyCode: 13, bubbles: true
}));

// 4) esperar respuesta — Perplexity stream → 30s timeout
const deadline = Date.now() + 60000;
let lastLen = 0;
let stable = 0;
while (Date.now() < deadline) {
  await new Promise(r => setTimeout(r, 1500));
  const txt = document.querySelector('main')?.innerText || "";
  if (txt.length === lastLen) {
    stable++;
    if (stable >= 3) break;  // estable durante 4,5s
  } else {
    stable = 0;
    lastLen = txt.length;
  }
}

// 5) devolver
const result = document.querySelector('main')?.innerText || "";
return JSON.stringify({
  query: QUERY,
  length: result.length,
  text: result.slice(0, 12000),
  truncated: result.length > 12000
});
