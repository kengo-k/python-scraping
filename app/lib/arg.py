import argparse
from enum import Enum, auto


class ResultCode(Enum):
    E0001 = auto()
    E0002 = auto()
    SUCCESS = auto()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="target url")
    parser.add_argument("selector", help="selector")
    parser.add_argument("-a", "--attribute", help="target attribute")
    parser.add_argument("-c", "--content", help="content", action="store_true")
    return parser


def validate_args(args):
    if args.attribute is None and args.content is False:
        return (ResultCode.E0001, "Error: both attribute and content is not specified")
    if args.attribute is not None and args.content is True:
        return (ResultCode.E0002, "Error: both attribute and content is specified")
    return (ResultCode.SUCCESS, None)
