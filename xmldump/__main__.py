import argparse
from .parser import XMLParserIter


def arguments_parser():
    parser = argparse.ArgumentParser(description="Dump a xml file.")
    parser.add_argument(
        "filename",
        help="Filename of the file to dump",
    )
    return parser.parse_args()


def main():
    args = arguments_parser()
    parser = XMLParserIter(args.filename)
    parser.parse(export=True)


if __name__ == "__main__":
    main()
