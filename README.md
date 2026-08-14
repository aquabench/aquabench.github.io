# aquabench.github.io

Project page for **AQUABENCH — Evaluating Vision Foundation Models for Underwater Segmentation**
(Torben Globisch, Stefan Oehmcke — University of Rostock).

Served by GitHub Pages from the `main` branch. The site is a single self-contained
`index.html` — no build step, no dependencies.

## Releasing the links

The Paper / Dataset / Code cards in the `#resources` section are intentionally inert until
the conference. Each is a `<span class="link" aria-disabled="true">` containing a
`<span class="soon">Coming soon</span>` badge.

To activate one, change the element to an `<a>` with an `href` and drop the badge:

```html
<!-- before -->
<span class="link" aria-disabled="true">
  <span class="soon">Coming soon</span>
  ...

<!-- after -->
<a class="link" href="https://arxiv.org/abs/XXXX.XXXXX">
  ...
```

The active hover styling is already in the stylesheet and applies automatically to any
`a.link` without `aria-disabled`. Remember to close with `</a>` instead of `</span>`,
and delete the amber "not live yet" notice above the cards once all three are published.

## Logo

The hero uses `assets/logo.png` — the mark cropped to its circle, white background replaced
with transparency, downscaled to 512px and palette-quantized (125 KB, down from 291 KB
unquantized).

To regenerate it from a new export:

```bash
python3 tools/make-logo.py path/to/logo-export.png   # -> assets/logo.png
```

The script finds the circular artwork by its non-white bounding box, so the source can be a
plain screenshot on a white page. The original export is preserved in git history at commit
`d4a342e`.

If `assets/logo.png` is ever missing, the hero falls back to an inline SVG mark: the `<img>`
`onerror` handler removes itself and unhides `#markFallback`. Two details that fallback
depends on — the SVG is declared *before* the `<img>` so it is already parsed when the error
fires, and the reveal uses `removeAttribute('hidden')` because `hidden` is an `HTMLElement`
IDL property that does nothing when assigned on an `SVGElement`.

`img.mark` is also clipped with `border-radius:50%`, which keeps the circle crisp and means
a non-transparent square export would still render correctly. Drop that rule if you ever
switch to artwork that is not circular.

## Citation

The BibTeX entry in the `#citation` section is a placeholder and should be updated with the
real venue on publication.
