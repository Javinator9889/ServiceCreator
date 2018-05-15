#!/bin/bash
### BEGIN INIT INFO
# Provides:          <NAME>
# Required-Start:    $local_fs $network $named $time $syslog
# Required-Stop:     $local_fs $network $named $time $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: <SHORT-DESCRIPTION>
# Description:       <DESCRIPTION>
### END INIT INFO

#################################################################################
#
# start-stop-daemon template for creating service scripts out of executables
#
# Most of the installations can be achieved by changing the variables below.
#
# This template is meant to be used freely.
# This template derives from a common template that is found on the web.
# Unfortunately I could not find the original source to give the proper credits
#
# source: https://gist.github.com/bcap/5397674
# Feel free to contribute!
#################################################################################


#################################################################################
# Fill/change the following vars
#################################################################################

PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin
DESC="<SHORT-DESCRIPTION>"                # String describing the service
NAME="<NAME>"                             # Name of the service, will be used in another vars
DAEMON="<COMMAND>"                        # Path to the service executable, e.g. /usr/bin/java
DAEMON_ARGS="<ARGS>"                      # Arguments passed to the service startup
RUN_AS="<USERNAME>"                       # Which user will run the service
LIB_LOG_FILENAME="<LIB-LOG_FILENAME>"     # The custom name for the lib & log path

WORK_DIR="/var/lib/${LIB_LOG_FILENAME}"   # Working directory where the service will be started, defaults to /var/lib/${NAME}
USER=${RUN_AS}                            # User that will spawn the process, defaults to the service name
GROUP=${RUN_AS}                           # Group that will spawn the process, defaults to the service name
PID_FILE=/var/run/${NAME}.pid             # Pid file location, defaults to /var/run/${NAME}.pid
SCRIPT_NAME=/etc/init.d/${NAME}           # Location of this init script
LOG_PATH=/var/log/${LIB_LOG_FILENAME}     # Standard output and Standard error will be outputted here

START_STOP_DAEMON_OPTIONS="--chuid=$USER:$GROUP --background --chdir=$WORK_DIR"

#################################################################################
# Change the code below if needed
#################################################################################

# Exit if the package is not installed
[ -x "$DAEMON" ] || exit 0

# Read configuration variable file if it is present
[ -r /etc/default/$NAME ] && . /etc/default/$NAME

# Load the VERBOSE setting and other rcS variables
. /lib/init/vars.sh

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.2-14) to ensure that this file is present
# and status_of_proc is working.
. /lib/lsb/init-functions

#
# Function that starts the daemon/service
#
do_start()
{
  # Return
  #   0 if daemon has been started
  #   1 if daemon was already running
  #   2 if daemon could not be started
  start-stop-daemon $START_STOP_DAEMON_OPTIONS --start --pidfile $PID_FILE --exec $DAEMON --test >> \
  ${LOG_PATH}/${NAME}.out 2>> ${LOG_PATH}/${NAME}.err || return 1
  start-stop-daemon $START_STOP_DAEMON_OPTIONS --start --pidfile $PID_FILE --exec $DAEMON -- $DAEMON_ARGS >> \
  ${LOG_PATH}/${NAME}.out 2>> ${LOG_PATH}/${NAME}.err || return 2

  sleep 2
  # Add code here, if necessary, that waits for the process to be ready
  # to handle requests from services started subsequently which depend
  # on this one.  As a last resort, sleep for some time.
}

#
# Function that stops the daemon/service
#
do_stop()
{
  # Return
  #   0 if daemon has been stopped
  #   1 if daemon was already stopped
  #   2 if daemon could not be stopped
  #   other if a failure occurred
  start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 --pidfile $PID_FILE
  RETVAL="$?"
  [ "$RETVAL" = 2 ] && return 2
  # Wait for children to finish too if this is a daemon that forks
  # and if the daemon is only ever run from this initscript.
  # If the above conditions are not satisfied then add some other code
  # that waits for the process to drop all resources that could be
  # needed by services started subsequently.  A last resort is to
  # sleep for some time.
  start-stop-daemon --stop --quiet --oknodo --retry=0/30/KILL/5 --exec $DAEMON
  [ "$?" = 2 ] && return 2
  # Many daemons don't delete their pidfiles when they exit.
  rm -f ${PID_FILE}
  return "$RETVAL"
}

uninstall() {
  echo -n "Are you sure you want to uninstall this service? That cannot be undone [yes|no]: "
  local SURE
  read SURE
  if [ "$SURE" = "yes" ]; then
    do_stop
    rm -f "$PID_FILE"
    echo "Notice: log path was not removed: $LOG_PATH" >&2
    update-rc.d -f "$NAME" remove
    rm -fv "$0"
    rm -r "$WORK_DIR"
  else
    echo "Aborting..."
  fi
}

disable() {
    printf "Disabling service from boot...\n"
    printf "This will cause your service not running on boot and stopping it right now\n"
    do_stop
    update-rc.d -f "$NAME" remove
    printf "Service correctly disabled\n"
}

enable_again() {
    printf "Enabling service...\n"
    printf "This will cause your service running on boot and restarting it right now\n"
    do_stop
    do_start
    update-rc.d "$NAME" defaults
    printf "Service correctly enabled\n"
}

case "$1" in
  start)
    [ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
    do_start
    case "$?" in
      0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
      2)   [ "$VERBOSE" != no ] && log_end_msg 1 ;;
    esac
    ;;
  stop)
    [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
    do_stop
    case "$?" in
      0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
      2)   [ "$VERBOSE" != no ] && log_end_msg 1 ;;
    esac
    ;;
  status)
    status_of_proc "$DAEMON" "$NAME" && exit 0 || exit $?
    ;;
  restart|force-reload)
    log_daemon_msg "Restarting $DESC" "$NAME"
    do_stop
    case "$?" in
      0|1)
      do_start
      case "$?" in
        0) log_end_msg 0 ;;
        1) log_end_msg 1 ;; # Old process is still running
        *) log_end_msg 1 ;; # Failed to start
      esac
      ;;
      *)
        # Failed to stop
        log_end_msg 1
      ;;
    esac
    ;;
  uninstall)
    uninstall
    ;;
  disable)
    disable
    ;;
  enable)
    enable_again
    ;;
  *)
    echo "Usage: $SCRIPT_NAME {start|stop|status|restart|force-reload|uninstall|disable|enable}" >&2
    exit 3
    ;;
esac

: