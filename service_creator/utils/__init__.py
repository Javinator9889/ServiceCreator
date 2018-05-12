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
