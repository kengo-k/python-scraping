import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="target url")
    parser.add_argument("selector", help="selector")
    parser.add_argument("-a", "--attribute", help="target attribute")
    parser.add_argument("-c", "--content", help="content", action="store_true")
    return parser