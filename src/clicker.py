import keyboard
import pyautogui
import threading
import colorama
import time


class Clicker:
    def __init__(self, thread, stop, enable_disable) -> None:
        colorama.init()
        self.thread = thread
        self.stop = stop
        self.enable_disable = enable_disable
        self.running = True
        self.enable = False

        keyboard.on_press_key(self.enable_disable, self.toggle_enable)


    def toggle_enable(self, event):
        self.enable = not self.enable
        print(colorama.Fore.YELLOW, f"[!] Auto clicker {'enabled' if self.enable else 'disabled'}")
            

    def __auto_click(self) -> None:
        while self.running:
            if keyboard.is_pressed(self.stop):
                self.running = False
                break

            if self.enable:
                pyautogui.click()

            time.sleep(0.01)


    def start(self) -> None:
        for _ in range(self.thread):
            thread = threading.Thread(target=self.__auto_click)
            thread.start()
