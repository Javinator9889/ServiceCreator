from service_creator.values import OutputColors as Colors

# Default program constants
MAIN_PROGRAM_NAME = "Service Creator"
MAIN_PROGRAM_COMMAND = "service_creator"
MAIN_PROGRAM_DESCRIPTION = "Create custom services for your Debian-based systems (such as Ubuntu) with this tool | " \
                           "Automate the process and make everything faster and easier than ever"
MAIN_PROGRAM_VERSION = "0.99b"
MAIN_PROGRAM_EPILOG = MAIN_PROGRAM_NAME + " | v" + MAIN_PROGRAM_VERSION
MAIN_PROGRAM_USAGE = Colors.HEADER + MAIN_PROGRAM_NAME + Colors.END_COLOR + "\nUse this tool for creating custom " \
                                                                            "init.d scripts that will run" \
                     + Colors.UNDERLINE + " on boot" + Colors.END_COLOR + ".\nThis program needs " + Colors.OK_GREEN \
                     + "admin rights" + Colors.END_COLOR + " in order to " + Colors.BOLD + "copy the new script" \
                     + Colors.END_COLOR + " to the \"/etc/init.d\" folder and be able to execute it on computer boot" \
                                          ".\nThe new created service will have the following configuration params:\n" \
                     + Colors.OK_BLUE + "\t- start: will start executing the service if not running\n\t- stop: will" \
                                        " stop executing the service if running\n\t- restart: first, stops the " \
                                        "service if running and then starts it again\n\t- uninstall: stops the " \
                                        "service if running. Then, removes the service from boot and from " \
                                        "\"/etc/init.d\" folder\n\t- disable: will disable the service from starting " \
                                        "on computer boot\n\t- enable: will enable the service for starting on " \
                                        "computer boot\n\t- status: will show the current status for the service" \
                     + Colors.END_COLOR + "\n\nThe script you create will store its logs in \"/var/log\" directory," \
                                          " with your service name."
MAIN_PROGRAM_URL = "https://github.com/Javinator9889/ServiceCreator"

# Other params
OP_VERSION_RAW = "https://github.com/Javinator9889/ServiceCreator/raw/development/version.json"
OP_BASH_HEADER = "#!/bin/bash"
OP_SH_HEADER = "#!/bin/sh"
OP_TEMPLATE_FILE = "https://raw.githubusercontent.com/Javinator9889/ServiceCreator/development/template.sh"

# Paths
P_ETC_INIT_DIR = "/etc/init.d/"
P_USR_LOCAL_BIN_DIR = "/usr/local/bin/"

# Inputs
I_PATH_NOT_FOUND = Colors.BOLD + "Please, provide a complete path where the script will be stored: " + Colors.END_COLOR
I_SERVICE_NAME = Colors.OK_BLUE + "Which name will have the service? (Notice that special characters such as \"\\n\" " \
                                  "or whitespaces \" \" will be deleted): " + Colors.END_COLOR + Colors.OK_GREEN
I_CORRECT_SERVICE_NAME = Colors.END_COLOR + "The name you chose is \"{}\". Is that correct?"
I_USERNAME = Colors.OK_BLUE + "Now, tell me with which user permissions should the scrip be executed (this field is a" \
                              " username): " + Colors.END_COLOR + Colors.OK_GREEN
I_CORRECT_USERNAME = Colors.END_COLOR + "The username you chose is \"{}\". Is that correct?"
I_READ_COMMAND_FROM_FILE = Colors.OK_BLUE + "It is almost completed. Now you must tell me which command will the " \
                                            "service execute." + Colors.END_COLOR + Colors.BOLD + \
                           " Would you like to load it from file?" + Colors.END_COLOR
I_FILENAME_DESC = Colors.WARNING + "Notice that if your file contains the \"#!/bin/bash\" header (or \"#!/bin/sh\", " \
                                   "it must be at the first line of the file. If it is not present, it will be " \
                                   "added automatically" + Colors.END_COLOR
I_FILENAME = Colors.UNDERLINE + "Please, give me the complete filename:" + Colors.END_COLOR + " "
I_COMMAND = Colors.OK_BLUE + "Type the command your service must execute on boot (be careful with new lines): " \
            + Colors.END_COLOR
I_SHORT_DESCRIPTION = Colors.OK_BLUE + "Enter a short description for your service: " + Colors.END_COLOR
I_LONG_DESCRIPTION = Colors.OK_BLUE + "Enter a long description for your service. It can be empty: " + Colors.END_COLOR

# Animation texts
ANIM_GENERATING_FILE = "Generating new script file..."
ANIM_CREATING_FOLDERS = "Creating required folders for the created script..."
ANIM_APPLYING_NEW_CONFIGURATION = "Copying new file and updating boot configuration..."
ANIM_STARTING_SERVICE = "Starting new service..."

# Commands
C_UPDATE_RC = "update-rc.d {} defaults"
