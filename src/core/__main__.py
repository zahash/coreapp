from src import core
import argparse


def my_cli():
    parser = argparse.ArgumentParser(usage='core.py [-h] POS_ARG [-o OPT_ARG]',
                                     description="What core.py does here.")
    parser.add_argument('positional',
                        metavar='POS_ARG',
                        type=str,
                        help='What this argument does.')
    parser.add_argument('-o',
                        '--optional',
                        metavar='OPT_ARG',
                        type=str,
                        help='What this option does.')
    args = parser.parse_args()
    core.MyClass2.main(args.positional, args.optional)


if __name__ == "__main__":
    my_cli()
