import argparse
from .parse import xml_parse


def arguments_parser():
    parser = argparse.ArgumentParser(description="Dump a xml file.")
    parser.add_argument(
        "filename",
        help="Filename of the file to dump",
    )
    return parser.parse_args()


def main():
    args = arguments_parser()
    xml_parse(args.filename)


if __name__ == "__main__":
    main()
