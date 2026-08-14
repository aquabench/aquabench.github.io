#!/usr/bin/env python3
"""Turn the white-background logo export into assets/logo.png.

Crops tight to the circular artwork, replaces the white surround with
transparency, downscales, and palette-quantizes for web delivery.

    python3 tools/make-logo.py <source.png> [-o assets/logo.png]

Requires: Pillow, numpy.
"""
import argparse
import os

from PIL import Image, ImageDraw
import numpy as np

SUPERSAMPLE = 4      # edge antialiasing factor
INSET_PX = 2.0       # radius trimmed, in source px, so no white rim survives
WHITE_CUTOFF = 247   # per-channel: brighter than this counts as background


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source', help='logo export with a white background')
    ap.add_argument('-o', '--out', default='assets/logo.png')
    ap.add_argument('--size', type=int, default=512)
    ap.add_argument('--colors', type=int, default=256,
                    help='palette size; 0 disables quantization')
    args = ap.parse_args()

    im = Image.open(args.source).convert('RGBA')
    rgb = np.array(im.convert('RGB')).astype(int)

    # Bounding box of everything that is not the white page.
    ys, xs = np.where(rgb.sum(axis=2) < WHITE_CUTOFF * 3)
    if not len(xs):
        raise SystemExit('no non-white content found — is the source blank?')
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()

    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    r = max(x1 - x0, y1 - y0) / 2.0
    print(f'content {x1-x0+1}x{y1-y0+1} -> circle centre ({cx:.1f},{cy:.1f}) r={r:.1f}')

    crop = im.crop((int(round(cx - r)), int(round(cy - r)),
                    int(round(cx + r)), int(round(cy + r))))
    src_size = crop.size[0]
    crop = crop.resize((args.size, args.size), Image.LANCZOS)

    # Circular alpha mask, drawn oversized then downsampled for a clean edge.
    inset = INSET_PX * args.size / src_size
    hi = args.size * SUPERSAMPLE
    mask = Image.new('L', (hi, hi), 0)
    ImageDraw.Draw(mask).ellipse(
        [inset * SUPERSAMPLE, inset * SUPERSAMPLE,
         (args.size - inset) * SUPERSAMPLE - 1,
         (args.size - inset) * SUPERSAMPLE - 1], fill=255)
    crop.putalpha(mask.resize((args.size, args.size), Image.LANCZOS))

    if args.colors:
        crop = crop.quantize(colors=args.colors, method=Image.FASTOCTREE,
                             dither=Image.FLOYDSTEINBERG).convert('RGBA')

    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    crop.save(args.out, 'PNG', optimize=True)

    chk = np.array(Image.open(args.out))
    assert chk[0, 0, 3] == 0, 'corner is not transparent'
    assert chk[args.size // 2, args.size // 2, 3] > 250, 'centre is not opaque'
    print(f'wrote {args.out}: {args.size}px, {os.path.getsize(args.out)//1024} KB')


if __name__ == '__main__':
    main()
