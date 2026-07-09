# Resume RAG Assistant — Frontend

A framework-free (HTML5 / CSS3 / vanilla ES6) frontend for an AI-powered
resume RAG assistant. Upload a resume, watch it move through the
processing pipeline, and ask questions about it with every answer backed
by a visible trail of retrieved evidence.

## Running it locally

The app talks to a backend at `POST /upload` and `POST /ask`, so it
should be served over HTTP rather than opened directly as a `file://`
path. From the project root:

```bash
python3 -m http.server 5500
# or: npx serve .
```

Then open `http://localhost:5500`.

If no backend is reachable at `http://localhost:8000`, the interface
falls back to a local simulation for uploads and chat so the UI stays
fully explorable on its own. Point it at a real backend by setting
`window.__RESUME_RAG_API_BASE__` before `js/config.js` loads, e.g.:

```html
<script>window.__RESUME_RAG_API_BASE__ = "https://api.example.com";</script>
<script src="js/config.js"></script>
```

## Structure

```
index.html            Root dashboard (upload, chat, processing, retrieval)
components/*.html      Reference partials mirroring the markup inlined
                        in each page (no build step / templating in use)
css/                   One stylesheet per concern (variables, layout,
                        each major component, responsive breakpoints)
js/
  config.js            Endpoints, limits, storage keys
  api.js                fetch/XHR wrappers for /upload and /ask
  upload.js             Drag-and-drop state machine
  chat.js               Message rendering, typing indicator, retrieval panel
  main.js               Theme, sidebar, cross-component wiring, bootstrap
pages/
  dashboard.html        Same dashboard, reachable from within pages/
  history.html          Past uploads and conversations
  settings.html         Appearance, assistant, and data preferences
```

## Design notes

The palette and type system are built around the one thing this product
actually does: turn a resume into evidence you can question. The
Retrieved Context panel borrows the look of a library card catalog —
dashed-edge cards with a rotated match-score stamp — rather than a
generic chat-app citation list, since transparency into *why* the
assistant said something is the feature that matters most in a RAG tool.

Typefaces: Fraunces (display), Inter (UI text), IBM Plex Mono (scores,
timestamps, file sizes, and anything read as data rather than prose).
