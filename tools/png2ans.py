#!/usr/bin/env python3

from PIL import Image
import argparse

RESET = "\033[0m"

def rgb_escape(r, g, b, foreground=True):
    if foreground:
        return f"\033[38;2;{r};{g};{b}m"
    return f"\033[48;2;{r};{g};{b}m"


def pixel(img, x, y):
    if x >= img.width or y >= img.height:
        return (0, 0, 0, 0)

    return img.getpixel((x, y))


def convert(image_path, output_path, width):

    image = Image.open(image_path).convert("RGBA")

    aspect = image.height / image.width

    #
    # Unicode half blocks represent TWO pixels vertically.
    #
    new_height = int(width * aspect * 2)

    image = image.resize(
        (width, new_height),
        Image.Resampling.LANCZOS
    )

    lines = []

    for y in range(0, image.height, 2):

        line = ""

        for x in range(image.width):

            top = pixel(image, x, y)
            bottom = pixel(image, x, y + 1)

            tr, tg, tb, ta = top
            br, bg, bb, ba = bottom

            #
            # Transparent pixel
            #

            if ta == 0 and ba == 0:
                line += RESET + " "
                continue

            #
            # Upper half
            #

            line += (
                rgb_escape(tr, tg, tb, True)
                + rgb_escape(br, bg, bb, False)
                + "▀"
            )

        line += RESET

        lines.append(line)

    with open(output_path, "w", encoding="utf-8") as f:

        f.write("\n".join(lines))

    print(f"Generated {output_path}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("input")

    parser.add_argument("output")

    parser.add_argument(
        "--width",
        type=int,
        default=56
    )

    args = parser.parse_args()

    convert(
        args.input,
        args.output,
        args.width
    )
