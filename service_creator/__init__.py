import argparse
import time

from .values.Constants import (MAIN_PROGRAM_NAME,
                               MAIN_PROGRAM_COMMAND,
                               MAIN_PROGRAM_DESCRIPTION,
                               MAIN_PROGRAM_VERSION,
                               MAIN_PROGRAM_EPILOG,
                               MAIN_PROGRAM_USAGE,
                               MAIN_PROGRAM_URL)
from .utils import isRunningLinux, isUserAdmin, isNewVersionAvailable
from .exceptions import LinuxSystemNotFound, NoRootPermissions
from .output import OutputColors as Colors
from .output import Printer


def application(args: argparse.Namespace):
    is_usage_chosen = args.u
    if is_usage_chosen:
        print(MAIN_PROGRAM_USAGE)
        exit(2)
    else:
        try:
            if isNewVersionAvailable():
                Printer.cprint("There is a new version available | Download it via pip or go to this URL: "
                               + MAIN_PROGRAM_URL, Colors.BOLD)
                time.sleep(8)
            if isRunningLinux():
                if isUserAdmin():

            else:
                raise LinuxSystemNotFound(Colors.FAIL + "Linux system not found on this machine. You must use Linux to"
                                                        " use this app" + Colors.END_COLOR)
        except Exception as e:
            print(e)


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
