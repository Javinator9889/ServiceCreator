def isRunningLinux():
    import platform
    return platform.system() == "Linux"


def isUserAdmin():
    # type: () -> bool
    import os

    try:
        return os.getuid() == 0
    except AttributeError:
        return False


def isNewVersionAvailable():
    # type: () -> bool
    import requests
    import pickle
    from service_creator.values.Constants import MAIN_PROGRAM_VERSION, OP_VERSION_RAW

    response = requests.get(OP_VERSION_RAW)
    version_dict = pickle.loads(response.content)
    return version_dict["version"] != MAIN_PROGRAM_VERSION


def exportVersion():
    import pickle
    from service_creator.values.Constants import MAIN_PROGRAM_VERSION

    filename = "version.json"
    version_dict = {"version": MAIN_PROGRAM_VERSION}
    with open(filename, "wb") as file:
        pickle.dump(version_dict, file, pickle.HIGHEST_PROTOCOL)


def shouldContinueWith(text: str):
    # type: () -> bool
    from service_creator.output import prompt_input
    from service_creator.output import OutputColors
    from service_creator.exceptions import NonValidInput

    text_for_input = text + " [Y/n]"
    user_selection = prompt_input(text_for_input, OutputColors.BOLD).lower()
    if (user_selection == 'y') or (user_selection == "yes"):
        return True
    elif (user_selection == 'n') or (user_selection == "no"):
        return False
    else:
        raise NonValidInput(OutputColors.FAIL + "Input must be [y|yes] or [n|no]" + OutputColors.END_COLOR)


def isAnExistingUser(username: str):
    # type: () -> bool
    import pwd  # Only available on Linux systems. If importing on Windows, ImportError | ModuleNotFound will appear

    try:
        if pwd.getpwnam(username):
            return True
        else:
            return False
    except KeyError:
        return False


def makeBashScript(filename: str, new_sh_file: str):
    # type: () -> bool
    import os
    from service_creator.values.Constants import OP_BASH_HEADER, OP_SH_HEADER, P_USR_LOCAL_BIN_DIR

    with open(filename, 'r') as script:
        script_content = script.readlines()
    if (script_content[0] != OP_BASH_HEADER) or (script_content[0] != OP_SH_HEADER):
        script_content.insert(0, OP_SH_HEADER)
    else:
        if os.path.exists(P_USR_LOCAL_BIN_DIR + new_sh_file):
            return False
        else:
            with open(P_USR_LOCAL_BIN_DIR + new_sh_file, 'w') as sh_file:
                for script_line in script_content:
                    sh_file.write(script_line)
            os.chmod(P_USR_LOCAL_BIN_DIR + new_sh_file, 0o755)
            return True


def ifCommandExists(command: str):
    # type: () -> bool
    from shutil import which

    return which(command) is not None


def getCommandFullPath(command: str):
    # type: () -> str
    from shutil import which

    return which(command)


def getUsernameUID(username: str):
    


def generateLogFile(service_name: str, username: str):
    import os

    new_file = open("/var/log/" + service_name, 'w')
    new_file.close()
    os.chown("/var/log/" + service_name, username)
