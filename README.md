# PNG to Centerline SVG

This repository provides a simple command-line tool for converting a PNG image to a centerline SVG. It uses `scikit-image` for image processing and `potrace` for vectorization.

## Requirements

- Python 3
- `scikit-image` and `svgwrite` Python packages
- `potrace` command-line tool

Install dependencies (Ubuntu example):

```bash
apt-get update && apt-get install -y potrace
pip install scikit-image svgwrite
```

## Usage

```bash
python png_to_centerline_svg.py input.png output.svg
```

This will read `input.png`, compute the skeleton (centerline) of the shapes, and export the result as `output.svg`.
