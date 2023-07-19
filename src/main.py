from clicker import Clicker
import sys
import colorama
import os
import time
import random


banner = """
               _____          __           _________ .__  .__        __                 
              /  _  \  __ ___/  |_  ____   \_   ___ \|  | |__| ____ |  | __ ___________ 
             /  /_\  \|  |  \   __\/  _ \  /    \  \/|  | |  |/ ___\|  |/ // __ \_  __ \\
            /    |    \  |  /|  | (  <_> ) \     \___|  |_|  \  \___|    <\  ___/|  | \/
            \____|__  /____/ |__|  \____/   \______  /____/__|\___  >__|_ \\\___  >__|   
                    \/                             \/             \/     \/    \/       
        """

color_list = [colorama.Fore.BLUE, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.LIGHTMAGENTA_EX,
            colorama.Fore.YELLOW, colorama.Fore.RED, colorama.Fore.LIGHTGREEN_EX, colorama.Fore.LIGHTYELLOW_EX,
            colorama.Fore.LIGHTCYAN_EX, colorama.Fore.MAGENTA, colorama.Fore.LIGHTRED_EX]


def random_color() -> str:
    return color_list[random.randint(0, len(color_list) - 1)]


def print_banner() -> None:
    print(random_color(), "==================================================================================================================")
    print(random_color(), banner)
    print(random_color(), "==================================================================================================================")


def print_menu() -> None:
    string = " ┎──────────────────────[Menu]───────────────────────"
    colored_string = ""
    for char in string:
        colored_string += random_color() + char

    print(colored_string)

    print(random_color(), "│ [0] Exit")
    print(random_color(), "│ [1] Start")
    print(random_color(), "│ [2] Credit")
    print(random_color(), "┕───────────────────────────────────────────────────")

def main() -> None:
    """
        Auto Clicker script.
        https://github.com/Silme94
    """

    try:

        os.system("cls")

        print_banner()

        time.sleep(2)

        print_menu()
        
        loop = True

        while loop:
            choice = input(f"{random_color()} >> ")
            match choice:
                case "0":
                    print(random_color(), "bye !")
                    sys.exit(0)

                case "1":
                    thread_num = int(input(f"{random_color()} Threads numbers >> "))
                    exit_key = input(f"{random_color()} Exit key >> ")
                    enable_disable = input(f"{random_color()} Enable/Disable key >> ")

                    for i in range(20):
                        print("\r", random_color(), "[!] Starting...", sep='', end='', flush=True)
                        time.sleep(0.2)

                    loop = False

                    os.system("cls")

                    print_banner()
                    print(random_color(), f"[!] Press {exit_key} to stop auto clicker.")
                    print(random_color(), f"[!] Press {enable_disable} to enable/disable auto clicker.")

                    autoClicker = Clicker(thread_num, exit_key, enable_disable)
                    autoClicker.start()

                case "2":
                    print(random_color(), "[!] GitHub : https://github.com/Silme94")
                    
                case "help":
                    print_menu()
                    
                case _:
                    print(random_color(), "[!] To get help on command, try 'help'.")
                



    except Exception as ex:
        print(ex)
        main()


if __name__ == "__main__":
    colorama.init()

    for i in range(20):
        print("\r", random_color(), "[!] Launching...", sep='', end='', flush=True)
        time.sleep(0.2)

    main()