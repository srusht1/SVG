import argparse
import os
import tempfile
from skimage import io, color
from skimage.filters import threshold_otsu
from skimage.morphology import skeletonize


def png_to_centerline_svg(input_png, output_svg):
    # Load image and convert to grayscale
    image = io.imread(input_png)
    if image.ndim == 3:
        image_gray = color.rgb2gray(image)
    else:
        image_gray = image

    # Binarize using Otsu's threshold
    thresh = threshold_otsu(image_gray)
    binary = image_gray > thresh

    # Skeletonize to get 1-pixel wide centerline
    skeleton = skeletonize(binary)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_svg)), exist_ok=True)

    # Save skeleton image temporarily as a PBM for potrace
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_pbm = os.path.join(tmpdir, "skeleton.pbm")
        io.imsave(tmp_pbm, (skeleton * 255).astype("uint8"))

        # Use potrace to convert to SVG
        os.system(f"potrace {tmp_pbm} -s -o {output_svg}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PNG to SVG centerline")
    parser.add_argument("input_png", help="Input PNG file")
    parser.add_argument("output_svg", help="Output SVG file")
    args = parser.parse_args()

    png_to_centerline_svg(args.input_png, args.output_svg)
