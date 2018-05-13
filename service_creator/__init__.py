import argparse
import time
import os

from .values.Constants import (MAIN_PROGRAM_NAME,
                               MAIN_PROGRAM_COMMAND,
                               MAIN_PROGRAM_DESCRIPTION,
                               MAIN_PROGRAM_VERSION,
                               MAIN_PROGRAM_EPILOG,
                               MAIN_PROGRAM_USAGE,
                               MAIN_PROGRAM_URL,
                               P_ETC_INIT_DIR,
                               I_PATH_NOT_FOUND,
                               I_SERVICE_NAME,
                               I_CORRECT_SERVICE_NAME,
                               I_USERNAME,
                               I_CORRECT_USERNAME,
                               I_READ_COMMAND_FROM_FILE,
                               I_FILENAME,
                               I_COMMAND,
                               I_SHORT_DESCRIPTION,
                               I_LONG_DESCRIPTION,
                               ANIM_CREATING_LOG_FILE,
                               ANIM_GENERATING_FILE,
                               ANIM_APPLYING_NEW_CONFIGURATION,
                               ANIM_STARTING_SERVICE)
from .utils import (isRunningLinux,
                    isUserAdmin,
                    isNewVersionAvailable,
                    shouldContinueWith,
                    cleanString,
                    isAnExistingUser,
                    makeBashScript,
                    ifCommandExists,
                    getCommandFullPath,
                    generateLogFile,
                    generateNewServiceFileFromTemplate,
                    applyConfigurationIsSuccessful,
                    startServiceIsSuccessful)
from .exceptions import LinuxSystemNotFound, NoRootPermissions
from .output import OutputColors as Colors
from .output import cprint, Animation


def application(args):
    is_usage_chosen = args.u
    if is_usage_chosen:
        print(MAIN_PROGRAM_USAGE)
        exit(2)
    else:
        animator = Animation(0.1)
        try:
            if isNewVersionAvailable():
                cprint("There is a new version available | Download it via pip or go to this URL: "
                       + MAIN_PROGRAM_URL, Colors.BOLD)
                time.sleep(8)
            if isRunningLinux():
                if isUserAdmin():
                    cprint("Script loaded. Let's start creating your new service\n")
                    service_folder = P_ETC_INIT_DIR
                    while not os.path.exists(service_folder):
                        cprint("It seems that \"" + service_folder + "\" does not exists",
                               Colors.FAIL)
                        partial_dir = input(I_PATH_NOT_FOUND)
                        if not partial_dir.endswith('/'):
                            service_folder = partial_dir + '/'
                        else:
                            service_folder = partial_dir
                    service_name = ""
                    is_valid_service_name = False
                    while not is_valid_service_name:
                        service_name = input(I_SERVICE_NAME)
                        if (service_name == "") or (service_name is None):
                            cprint("Empty values are not allowed. Please, provide a proper service name", Colors.FAIL)
                            is_valid_service_name = False
                        elif os.path.exists(service_folder + service_name):
                            cprint("The service name you provided already exists. Please, choose another one",
                                   Colors.FAIL)
                            is_valid_service_name = False
                        else:
                            if shouldContinueWith(I_CORRECT_SERVICE_NAME.format(service_name)):
                                service_name = cleanString(service_name)
                                is_valid_service_name = True
                            else:
                                cprint("Please, give me the new name you want the service to have", Colors.UNDERLINE)
                                is_valid_service_name = False
                    username = ""
                    is_valid_user = False
                    while not is_valid_user:
                        username = input(I_USERNAME)
                        if (username == "") or (username is None):
                            cprint("Empty values are not allowed. Please, provide a proper username", Colors.FAIL)
                            is_valid_user = False
                        elif isAnExistingUser(username):
                            if shouldContinueWith(I_CORRECT_USERNAME.format(username)):
                                is_valid_user = True
                            else:
                                cprint("Please, give me the new username you want the service to be run with",
                                       Colors.UNDERLINE)
                                is_valid_user = False
                    command = ""
                    if shouldContinueWith(I_READ_COMMAND_FROM_FILE):
                        filename = ""
                        is_valid_filename = False
                        while not is_valid_filename:
                            filename = input(I_FILENAME)
                            if (filename == "") or (filename is None):
                                cprint("Empty values are not allowed. Please, provide a proper filename",
                                       Colors.FAIL)
                                is_valid_filename = False
                            elif not os.path.exists(filename):
                                cprint("We have not found the file. Please, enter the full path for the file",
                                       Colors.FAIL)
                                is_valid_filename = False
                            else:
                                is_valid_filename = True
                        is_valid_script_filename = False
                        new_name = filename
                        while not is_valid_script_filename:
                            if not makeBashScript(filename, new_name):
                                new_name = input(Colors.FAIL + "We found an error creating the executable file. "
                                                               "Please, enter a new name: " + Colors.END_COLOR)
                                is_valid_script_filename = False
                            else:
                                is_valid_script_filename = True
                                command = "/usr/local/bin/" + new_name
                    else:
                        is_valid_command = False
                        while not is_valid_command:
                            command = input(I_COMMAND)
                            if (command == "") or (command is None):
                                cprint("Empty values are not allowed. Please, put an entire command",
                                       Colors.FAIL)
                                is_valid_command = False
                            elif ifCommandExists(command):
                                is_valid_command = True
                                command = getCommandFullPath(command)
                            else:
                                cprint("The specified command does not exist.", Colors.FAIL)
                                is_valid_command = False
                    short_description = ""
                    is_valid_short_description = False
                    while not is_valid_short_description:
                        short_description = input(I_SHORT_DESCRIPTION)
                        if (short_description == "") or (short_description is None):
                            cprint("Empty values are not allowed. Please, enter a short description", Colors.FAIL)
                            is_valid_short_description = False
                        else:
                            is_valid_short_description = True
                    long_description = ""
                    is_valid_description = False
                    while not is_valid_description:
                        long_description = input(I_LONG_DESCRIPTION)
                        if (long_description == "") or (long_description is None):
                            long_description = short_description
                            is_valid_description = True
                        else:
                            is_valid_description = True
                    animator.animate(ANIM_CREATING_LOG_FILE, None, Colors.OK_BLUE)
                    generateLogFile(service_name, username)
                    animator.stop()
                    time.sleep(1)
                    animator.animate(ANIM_GENERATING_FILE, None, Colors.OK_BLUE)
                    generateNewServiceFileFromTemplate(service_name, username, command, short_description,
                                                       long_description)
                    animator.stop()
                    time.sleep(1)
                    animator.animate(ANIM_APPLYING_NEW_CONFIGURATION, None, Colors.OK_BLUE)
                    if applyConfigurationIsSuccessful(service_name):
                        animator.stop()
                        time.sleep(1)
                        animator.animate(ANIM_STARTING_SERVICE, None, Colors.OK_BLUE)
                        if startServiceIsSuccessful(service_name):
                            animator.stop()
                            time.sleep(1)
                            cprint("All operations complete. Now you should be able to use all options with \"service"
                                   + service_name + "\" command. You can uninstall just adding \"uninstall\" to the"
                                                    " latest command.", Colors.BOLD)
                            exit(0)
                        else:
                            animator.force_stop()
                            cprint("There was an error while trying to start your new service. Please, check logs",
                                   Colors.FAIL)
                            exit(-1)
                    else:
                        animator.force_stop()
                        cprint("There was an error while trying to register your new service at boot. Please, check"
                               " logs", Colors.FAIL)
                        exit(-2)
                else:
                    raise NoRootPermissions(Colors.FAIL + "This app requires root access in order to work properly |"
                                                          " More info: " + MAIN_PROGRAM_URL + Colors.END_COLOR)
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
