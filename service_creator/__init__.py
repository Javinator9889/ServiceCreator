import argparse

from .values.Constants import (MAIN_PROGRAM_NAME,
                               MAIN_PROGRAM_COMMAND,
                               MAIN_PROGRAM_DESCRIPTION,
                               MAIN_PROGRAM_VERSION,
                               MAIN_PROGRAM_EPILOG,
                               MAIN_PROGRAM_USAGE)


def application(args: argparse.Namespace):
    is_usage_chosen = args.u
    if is_usage_chosen:
        print(MAIN_PROGRAM_USAGE)
        exit(2)
    else:
        print("to do")


def main():
    argument_creator = argparse.ArgumentParser(prog=MAIN_PROGRAM_COMMAND,
                                               description=MAIN_PROGRAM_DESCRIPTION,
                                               epilog=MAIN_PROGRAM_EPILOG)
    argument_creator.add_argument("-u",
                                  "--usage",
                                  action="store_true",
                                  help="Show full usage for this program")
    args = argument_creator.parse_args()
    application(args)


if __name__ == '__main__':
    main()
