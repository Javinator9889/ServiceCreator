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


def cleanString(input_string: str):
    # type: () -> str
    import re

    return re.sub("[^-a-zA-Z0-9]", '', input_string)


def shouldContinueWith(text: str):
    # type: () -> bool
    from service_creator.output import prompt_input
    from service_creator.output import OutputColors
    from service_creator.exceptions import NonValidInput

    text_for_input = text + " [Y/n]: "
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
        script_content.insert(0, OP_SH_HEADER + "\n\n")
    usr_exec_file = os.path.basename(new_sh_file)
    from pprint import pprint
    pprint(script_content)
    pprint("Path: " + P_USR_LOCAL_BIN_DIR + usr_exec_file)
    if os.path.exists(P_USR_LOCAL_BIN_DIR + usr_exec_file):
        return False
    else:
        with open(P_USR_LOCAL_BIN_DIR + usr_exec_file, 'w') as sh_file:
            for script_line in script_content:
                sh_file.write(script_line)
        os.chmod(P_USR_LOCAL_BIN_DIR + usr_exec_file, 0o755)
        return True


def ifCommandExists(command: str):
    # type: () -> bool
    from shutil import which

    return which(command.split()[0]) is not None


def getCommandFullPath(command: str):
    # type: () -> str
    from shutil import which

    return which(command)


def getUsernameUID(username: str):
    # type: () -> int
    import pwd

    return pwd.getpwnam(username).pw_uid


def getUsernameGID(username: str):
    # type: () -> int
    import pwd

    return pwd.getpwnam(username).pw_gid


def generateLogFile(service_name: str, username: str):
    import os

    filename = "/var/log/" + service_name + ".log"
    new_file = open(filename, 'w')
    new_file.close()
    os.chown(filename, getUsernameUID(username), getUsernameGID(username))


def generateNewServiceFileFromTemplate(service_name: str, username: str, command: str, short_description: str,
                                       long_description: str):
    import requests
    import os
    from service_creator.values.Constants import OP_TEMPLATE_FILE, P_ETC_INIT_DIR

    web_template = requests.get(OP_TEMPLATE_FILE)
    template = web_template.text

    template = template.replace("<NAME>", service_name)
    template = template.replace("<SHORT-DESCRIPTION>", short_description)
    template = template.replace("<DESCRIPTION>", long_description)
    template = template.replace("<COMMAND>", command)
    template = template.replace("<USERNAME>", username)

    with open(P_ETC_INIT_DIR + service_name, 'w') as new_script_file:
        new_script_file.write(template)
    os.chmod(P_ETC_INIT_DIR + service_name, 0o755)


def applyConfigurationIsSuccessful(service_name: str):
    # type: () -> bool
    import subprocess
    from service_creator.values.Constants import C_UPDATE_RC

    command = C_UPDATE_RC.format(service_name)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(process.stdout.read().decode("utf-8"))
    print(process.stderr.read().decode("utf-8"))
    return_code = process.returncode
    return return_code == 0


def startServiceIsSuccessful(service_name: str):
    # type: () -> bool
    import subprocess

    command = "service {} start".format(service_name)
    start_process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return_code = start_process.returncode
    return return_code == 0
