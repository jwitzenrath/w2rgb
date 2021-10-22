#!/usr/bin/env python
from w2rgb.converter import wavelength_to_rgb
import w2rgb.formatter as formatter

def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='w2rgb - convert a wavelength to an RGB color')
    parser.add_argument('wavelength', help="wavelength in nm, [380 nm to 750 nm]", type=float)
    parser.add_argument('--fmt', help="Output format. ['hex', 'rgb', 'RGB']", type=str, default='hex')
    args = parser.parse_args()

    r,g,b = wavelength_to_rgb(args.wavelength)

    if args.fmt == 'RGB':
        printer = formatter.rgb_to_rgb_255
    elif args.fmt == 'rgb':
        printer = formatter.rgb_to_rgb_1
    else:
        printer = formatter.rgb_to_hex

    print(printer(r,g,b))


if __name__ == '__main__':
    main()
