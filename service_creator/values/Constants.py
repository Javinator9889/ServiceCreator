from service_creator.values import OutputColors as Colors

# Default program constants
MAIN_PROGRAM_NAME = "Service Creator"
MAIN_PROGRAM_COMMAND = "service_creator"
MAIN_PROGRAM_DESCRIPTION = "Create custom services for your Debian-based systems (such as Ubuntu) with this tool | " \
                           "Automate the process and make everything faster and easier than ever"
MAIN_PROGRAM_VERSION = "0.1d"
MAIN_PROGRAM_EPILOG = MAIN_PROGRAM_NAME + " | v" + MAIN_PROGRAM_VERSION
MAIN_PROGRAM_USAGE = Colors.HEADER + MAIN_PROGRAM_NAME + Colors.END_COLOR + "\nUse this tool for creating custom " \
                                                                            "init.d scripts that will run" \
                     + Colors.UNDERLINE + "on boot" + Colors.END_COLOR + ".\nThis program needs " + Colors.OK_GREEN \
                     + "admin rights" + Colors.END_COLOR + " in order to " + Colors.BOLD + "copy the new script" \
                     + Colors.END_COLOR + " to the \"/etc/init.d\" folder and be able to execute it on computer boot" \
                                          ".\nThe new created service will have the following configuration params:\n" \
                     + Colors.OK_BLUE + "\t- start: will start executing the service if not running\n\t- stop: will" \
                                        " stop executing the service if running\n\t- restart: first, stops the " \
                                        "service if running and then starts it again\n\tuninstall: stops the service" \
                                        " if running. Then, removes the service from boot and from \"/etc/init.d\" " \
                                        "folder\n\t- disable: will disable service from starting on computer boot" \
                     + Colors.END_COLOR + "\n\nThe script you create will store its logs in \"/var/log\" directory," \
                                          " with your service name."
