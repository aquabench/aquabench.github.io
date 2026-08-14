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

The hero currently uses an inline SVG mark. To use the real logo, add `assets/logo.png`
and replace the `<svg class="mark">` block with `<img class="mark" src="assets/logo.png" alt="AquaBench logo">`.

## Citation

The BibTeX entry in the `#citation` section is a placeholder and should be updated with the
real venue on publication.
