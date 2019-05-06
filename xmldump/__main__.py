import argparse
from .parser import XMLParserIter


def arguments_parser():
    parser = argparse.ArgumentParser(description="Dump a xml file.")
    parser.add_argument("filename", help="Filename of the file to dump")
    parser.add_argument(
        "-i",
        "--ignore-attributes",
        dest="ignore_attributes",
        help="tags for which attributes should be ignored",
    )
    return parser.parse_args()


def main():
    args = arguments_parser()
    parser = XMLParserIter(args.filename, ignore_attributes=args.ignore_attributes)
    parser.parse(export=True)


if __name__ == "__main__":
    main()
