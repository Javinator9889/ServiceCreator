from service_creator.values import OutputColors


# class Printer:
#    @staticmethod
def cprint(text, color: str = None):
    if color is None:
        print(str(text))
    else:
        print(color + str(text) + OutputColors.END_COLOR)


def prompt_input(text, color: str = None):
    # type: () -> str
    if text is None:
        text = ""
    if color is None:
        user_input = input(text)
        return user_input
    else:
        colored_text = color + text + OutputColors.END_COLOR
        user_input = input(colored_text)
        return user_input


class Animation:
    from threading import Event, Thread

    __animation_values = "|/-\\"

    def __init__(self, duration: float):
        self.__duration = duration
        self.__stop_event = self.Event()
        self.__force_stop_event = self.Event()

    def animate(self, text, text_animation_end: str = None, color: str = None):
        self.__stop_event.clear()
        self.__force_stop_event.clear()

        animation_thread = self.Thread(target=self.__animation, args=(text, text_animation_end, color,))
        animation_thread.setDaemon(True)
        animation_thread.start()

    def __animation(self, text, text_animation_end: str = None, color: str = None):
        import time
        from service_creator.values import OutputColors

        if text_animation_end is None:
            text_animation_end = "OK"
        idx = 0
        if color is None:
            end_color = ""
            color = ""
        else:
            end_color = OutputColors.END_COLOR
        while not self.__stop_event.is_set():
            print(text + " " + color + "[" + self.__animation_values[idx % len(self.__animation_values)] + "]"
                  + end_color, end="\r")
            idx += 1
            time.sleep(self.__duration)
        if self.__force_stop_event.is_set():
            print(text + " " + OutputColors.FAIL + "[FAIL]" + end_color, end="\r")
        else:
            print(text + " " + OutputColors.OK_GREEN + text_animation_end + end_color, end="\r")
        print("\n")

    def stop(self):
        self.__stop_event.set()

    def force_stop(self):
        self.__force_stop_event.set()
        self.__stop_event.set()
