#!/bin/sh
### BEGIN INIT INFO
# Provides:          <NAME>
# Required-Start:    $local_fs $network $named $time $syslog
# Required-Stop:     $local_fs $network $named $time $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: <SHORT-DESCRIPTION>
# Description:       <DESCRIPTION>
### END INIT INFO

SCRIPT="<COMMAND>"
RUNAS=<USERNAME>
NAME=<NAME>

PIDFILE=/var/run/<NAME>.pid
LOGFILE=/var/log/<NAME>.log

start() {
  if [ -f "$PIDFILE" ] && [ -s "$PIDFILE" ] && kill -0 $(cat "$PIDFILE"); then
    echo 'Service already running' >&2
    return 1
  fi
  echo 'Starting service…' >&2
  local CMD="$SCRIPT & > $LOGFILE & echo \$!"
  su -c "$CMD" "$RUNAS" > "$PIDFILE"
 # Try with this command line instead of above if not workable
 # su -s /bin/sh $RUNAS -c "$CMD" > "$PIDFILE"
 
  sleep 2
  PID=$(cat "$PIDFILE")
    if pgrep -u "$RUNAS" -f "$NAME" > /dev/null
    then
      echo "$NAME is now running, the PID is $PID"
    else
      echo ''
      echo "Error! Could not start $NAME! - log is located at: \"$LOGFILE\""
    fi
}

stop() {
  if [ ! -f "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE"); then
    echo 'The service is not actually running' >&2
    return 1
  fi
  echo 'Stopping service…' >&2
  kill -15 $(cat "$PIDFILE") && rm -f "$PIDFILE"
  echo 'Service stopped' >&2
}

uninstall() {
  echo -n "Are you sure you want to uninstall this service? That cannot be undone [yes|no]: "
  local SURE
  read SURE
  if [ "$SURE" = "yes" ]; then
    stop
    rm -f "$PIDFILE"
    echo "Notice: log file was not removed: $LOGFILE" >&2
    update-rc.d -f "$NAME" remove
    rm -fv "$0"
  else
    echo "Aborting..."
  fi
}

status() {
    printf "%-50s" "Checking <NAME>..."
    if [ -f "$PIDFILE" ] && [ -s "$PIDFILE" ]; then
        PID=$(cat "$PIDFILE")
            if [ -z "$(ps axf | grep ${PID} | grep -v grep)" ]; then
                printf "%s\n" "The process appears to be dead but pidfile still exists"
            else    
                echo "Running, the PID is $PID"
            fi
    else
        printf "%s\n" "Service not running"
    fi
}

disable() {
    printf "Disabling service from boot..."
    printf "This will cause your service not running on boot and stopping it right now"
    stop
    update-rc.d -f "$NAME" remove
    printf "Service correctly disabled"
}

enable_again() {
    printf "Enabling service..."
    printf "This will cause your service running on boot and restarting it right now"
    stop
    start
    update-rc.d "$NAME" defaults
    printf "Service correctly enabled"
}


case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
    status
    ;;
  uninstall)
    uninstall
    ;;
  restart)
    stop
    start
    ;;
  disable)
    disable
    ;;
  enable)
    enable_again
    ;;
  *)
    echo "Usage: $0 {start|stop|status|restart|uninstall|disable|enable}"
esac

# vim: syntax=sh ts=4 sw=4 sts=4 sr noet
