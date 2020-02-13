import argparse
from htmlreader import SwimParser

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Parse a swim results file')
    arg_parser.add_argument('htmlfile', type=open,
        help='name of the HTML file to parse')
    args = arg_parser.parse_args()

    swim_reader = SwimParser()
    swim_reader.feed(args.htmlfile.read())
