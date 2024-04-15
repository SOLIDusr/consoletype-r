from os import system, path, mkdir
import sys
import json
import random
import colorama as col
import time
from datetime import datetime


def clear():
    if sys.platform.startswith('win'):
        system("cls")
    else:
        system("clear")


class App:

    def __init__(self) -> None:

        self.Gui: App.Gui = App.Gui(self)
        self.Game: App.Game = App.Game(self)
        self.Player: App.Player = self.Gui.startPage()
        self.O0: App.O0 = App.O0()

    def gettype():
        valid_chars: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', ' ']
        cmd_keys: list = [b'\x14', b'\x70', b'\x71', b'\x72', b'\x73', b'\x74', b'\x75', b'\x76', b'\x77', b'\x78', b'\x79', b'\x7a']  # TAB, CAPS LOCK, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12

        if sys.platform.startswith('win'):
            import msvcrt
            char = msvcrt.getch()
            if char.decode() in valid_chars:
                return char.decode()
            elif char == b'\x08':  # Check for backspace character (ASCII code 8)
                return "BACKSPACE"
            elif char == b'\x1b':  # Check for ESC character (ASCII code 27)
                return "ESC"
            elif char == b'\x09':   # Check for TAB character (ASCII code 9)
                return "TAB"
            elif char in cmd_keys:
                return "CMD"
            else:
                return "ERROR"
        else:
            import tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                if ch in valid_chars:
                    return ch
                elif ch == '\x7f':  # Check for backspace character (ASCII code 127)
                    return "BACKSPACE"
                elif ch == '\x1b':  # Check for ESC character (ASCII code 27)
                    return "ESC"
                else:
                    return "ERROR"
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # Player object

    class O0:

        class Oo:

            def __init__(self, _OOO:list, _oO:int, _OOo: int) -> None:
                self._O0O = _OOO
                self._o0O = _oO
                self._OO0 = _OOo
                self._oOO = f"\n: {datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}\n"

            def O0o(self) -> bool:
                _Oo0 = 100

                self._oOO += f"W: {self._OO0}\n"
                self._oOO += f"A: {self._o0O}\n"

                match self._OO0:
                    case _OOo if _OOo > 400:
                        _Oo0 -= 90
                    case _OOo if _OOo > 350:
                        _Oo0 -= 80
                    case _OOo if _OOo > 300:
                        _Oo0 -= 70
                    case _OOo if _OOo > 250:
                        _Oo0 -= 20

                match self._o0O:
                    case _oO if _oO in range(0, 61) and self._OO0 < 170:
                        _Oo0 += 50
                    case _oO if _oO in range(61, 81) and self._OO0 < 230:
                        _Oo0 += 30
                    case _oO if _oO in range(81, 91) and self._OO0 < 270:
                        _Oo0 += 10
                self._oOO += f"\n: {datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}\n"
                def _o0o(_OOO):
                    _O0O = random.randint(5, 10)
                    _OoO = [_OOO[i:i+_O0O] for i in range(0, len(_OOO), _O0O)]
                    _oOo = []
                    for _oOO in _OoO:
                        for i in range(1, len(_oOO)):
                            _oO0 = _oOO[i] - _oOO[i-1]
                            _oOo.append(round(_oO0, 3))
                            self._oOO += str(round(_oO0, 4)) + " Val " + "\n" if _oO0 < 0.05 else str(round(_oO0, 4)) + "\n"
                    return _oOo

                _oOo = _o0o(self._O0O)
                if _oOo[0] > 4:
                    _Oo0 -= 10
                else:
                    _Oo0 += 40
                for _oO0 in _oOo:
                    if _oO0 < 0.05:
                        _Oo0 -= 5
                def _check_chunks(_oOo):
                    _chunks = []
                    _temp_chunk = [_oOo[0]]
                    for i in range(1, len(_oOo)):
                        if abs(_oOo[i] - _oOo[i-1]) <= 0.02:
                            _temp_chunk.append(_oOo[i])
                        else:
                            if len(_temp_chunk) > 1:
                                _chunks.append(_temp_chunk)
                            _temp_chunk = [_oOo[i]]
                    if len(_temp_chunk) > 1:
                        _chunks.append(_temp_chunk)
                    return _chunks

                _equal_chunks = _check_chunks(_oOo)
                for _chunk in _equal_chunks:
                    self._oOO += f"\n{len(_chunk)} chunck\n"
                    if len(_chunk) > 5 and self._o0O > 80:
                        _Oo0 -= 4*len(_chunk)
                    elif len(_chunk) > 3 and self._o0O > 80:
                        _Oo0 -= 2*len(_chunk)


                self._oOO += f"\nS {_Oo0}\n"

                if _Oo0 < 30:
                    if not path.exists("rts"):
                        mkdir("rts")
                    _OOOo = open(f"rts/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "w")
                    _OOOo.write(self._oOO)
                    _OOOo.close()
                    return True
                elif _Oo0 < 60:
                    if not path.exists("rts"):
                        mkdir("rts")
                    _OOOo = open(f"rts/un{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "w")
                    _OOOo.write(self._oOO)
                    _OOOo.close()
                    return False
                return False

    class Player():

        def __init__(self, name: str = "Anonimous") -> None:
            self.name: str = name
            if not path.exists("app/profiles"):
                mkdir("app/profiles")
            if not path.exists(f"app/profiles/{self.name}.json"):
                with open(f"app/profiles/{self.name}.json", "w") as file:
                    json.dump({"profile": {"Name": self.name, "BestWPM": {"Easy": 0, "Medium": 0, "Hard": 0}, "BestAccuracy": {"Easy": 0, "Medium": 0, "Hard": 0}, "AverageWPM": {"Easy": 0, "Medium": 0, "Hard": 0}, "AverageAccuracy": {"Easy": 0, "Medium": 0, "Hard": 0}}, "runs": {}}, file, indent=4)

            with open(f"app/profiles/{self.name}.json", "r") as file:
                file: dict = json.load(file)
                self.stats: dict = file["profile"]
                self.runs: dict = file["runs"]

        def fetch(self):
            with open(f"app/profiles/{self.name}.json", "r") as file:
                file: dict = json.load(file)
                self.stats: dict = file["profile"]
                self.runs: dict = file["runs"]

        def update(self):
            with open(f"app/profiles/{self.name}.json", "r") as file:
                runs: dict = json.load(file)["runs"]
                easyAcc: list = []
                mediumAcc: list = []
                hardAcc: list = []
                easyWPM: list = []
                mediumWPM: list = []
                hardWPM: list = []
                for run in runs:
                    if runs[run]["Type"] == 0:
                        easyAcc.append(runs[run]["Accuracy"])
                        easyWPM.append(runs[run]["WPM"])
                    elif runs[run]["Type"] == 1:
                        mediumAcc.append(runs[run]["Accuracy"])
                        mediumWPM.append(runs[run]["WPM"])
                    elif runs[run]["Type"] == 2:
                        hardAcc.append(runs[run]["Accuracy"])
                        hardWPM.append(runs[run]["WPM"])
                self.stats["BestAccuracy"]["Easy"] = max(easyAcc) if easyAcc != [] else 0
                self.stats["BestWPM"]["Easy"] = max(easyWPM) if easyWPM != [] else 0
                self.stats["BestAccuracy"]["Medium"] = max(mediumAcc) if mediumAcc != [] else 0
                self.stats["BestWPM"]["Medium"] = max(mediumWPM) if mediumWPM != [] else 0
                self.stats["BestAccuracy"]["Hard"] = max(hardAcc) if hardAcc != [] else 0
                self.stats["BestWPM"]["Hard"] = max(hardWPM) if hardWPM != [] else 0
                self.stats["AverageWPM"]["Easy"] = round(sum(easyWPM) / len(easyWPM), 2) if easyWPM != [] else 0
                self.stats["AverageWPM"]["Medium"] = round(sum(mediumWPM) / len(mediumWPM), 2) if mediumWPM != [] else 0
                self.stats["AverageWPM"]["Hard"] = round(sum(hardWPM) / len(hardWPM), 2) if hardWPM != [] else 0
                self.stats["AverageAccuracy"]["Easy"] = round(sum(easyAcc) / len(easyAcc), 2) if easyAcc != [] else 0
                self.stats["AverageAccuracy"]["Medium"] = round(sum(mediumAcc) / len(mediumAcc), 2) if mediumAcc != [] else 0
                self.stats["AverageAccuracy"]["Hard"] = round(sum(hardAcc) / len(hardAcc), 2) if hardAcc != [] else 0
                self.save()
                file.close()
                del runs
                del easyAcc
                del mediumAcc
                del hardAcc
                del easyWPM
                del mediumWPM
                del hardWPM

        def save(self):
            with open(f"app/profiles/{self.name}.json", "w") as file:
                json.dump({"profile": self.stats, "runs": self.runs}, file, indent=4)
                file.close()

        # def update(self):
        #     with open(f"app/profiles/{self.name}.json", "w") as file:
                

        def getStats(self):
            stats_dict = {**self.stats, **{"runs": self.runs}}
            return stats_dict

    # So called backend of frontend

    class Gui:
        
        def __init__(self, app) -> None:
            self.app = app

        class Page:

            def __init__(self, title:str, content:list, destination) -> None:
                self.title = title
                self.content = content
                self.destination = destination

            class Article:
                def __init__(self, title:str, content) -> None:
                    self.title = title
                    self.content = content
                
                def load(self):
                    print(f"\n{self.title}")
                    print(self.content)
                    print("\n")

            def load(self):
                clear()
                print(self.title)
                for item in self.content:
                    item.load()
                print("Press Enter To Continue...")
                input()
                clear()
                self.goto()

            def goto(self):
                if self.destination != None:
                    self.destination()

        class Menu:

            class MenuItem:
 
                def __init__(self, title:str, destination) -> None:

                    self._title = title
                    self._destination = destination
                
                def load(self):
                    self._destination()
                
                # Getter for title
                def get_title(self):
                    return self._title

            def __init__(self, title:str, args: list) -> None:
                self._title = title
                self._items = args
            
            def load(self):
                clear()
                print(self._title)
                count = 0
                for item in self._items:
                    count += 1
                    print(f"{count}. {item.get_title()}")
                choise = App.gettype()
                if choise.isdigit() and int(choise) in range(1, len(self._items)+1):
                    self._items[int(choise)-1].load()
                else:
                    self.load()

        # So called frontend

        def mainMenu(self):
            self.Menu("ConsoleType", [self.Menu.MenuItem(title="Play", destination=lambda: self.app.Gui.gameUI()),
                                    self.Menu.MenuItem(title="Statistics", destination=lambda: self.app.Gui.statistics()),
                                    self.Menu.MenuItem(title="Match History", destination=lambda: self.app.Gui.matchHistory()),
                                    self.Menu.MenuItem(title="Force Update Stats", destination=lambda: [self.app.Player.update(), self.app.Gui.mainMenu()]),
                                    self.Menu.MenuItem(title="Exit", destination=lambda: exit())]).load()

        def gameUI(self):
            self.Menu("Play", [self.Menu.MenuItem(title="Simple texts", destination=lambda: self.app.Game.thegame(0)),
                               self.Menu.MenuItem(title="Hard texts", destination=lambda: self.app.Game.thegame(1)),
                               self.Menu.MenuItem(title="Insane texts", destination=lambda: self.app.Game.thegame(2)),
                               self.Menu.MenuItem(title="Back", destination=lambda: self.app.Gui.mainMenu())]).load()

        def endGame(self, wpm, accuracy, mistakes):
            self.Page("Result", [self.Page.Article("Round Is Over", ""),
                                 self.Page.Article("WPM", wpm),
                                 self.Page.Article("Accuracy", accuracy),
                                 self.Page.Article("Overall Mistakes", mistakes)], destination=lambda: self.app.Gui.gameUI()).load()
                
        def statistics(self):
            _stats = self.app.Player.getStats()
            self.Page("Statistics", [self.Page.Article("Best WPM", _stats["BestWPM"]),
                                     self.Page.Article("Best Accuracy", _stats["BestAccuracy"]),
                                     self.Page.Article("Average WPM", _stats["AverageWPM"]),
                                     self.Page.Article("Average Accuracy", _stats["AverageAccuracy"])], destination=lambda: self.app.Gui.mainMenu()).load()

        def matchHistory(self):
            self.Page("Match History", [self.Page.Article("Match History", "\n")]+[self.Page.Article(run, self.app.Player.runs[run]) for run in self.app.Player.runs], destination=lambda: self.app.Gui.mainMenu()).load()

        def startPage(self):
            for i in range(5):
                clear()
                # if i % 4 
                hands = "|/-\\"
                print("Removing System32" + " " + f"[{hands[i % 4]}]")
                time.sleep(0.5)
            return self.loginPage()

        def loginPage(self):
            self.Page("ConsoleType!", [self.Page.Article("Please, log into your account.", "No password needed!")], destination=lambda: None).load()
            return self.app.Player(input("Enter Login > "))

        def cheater(self):
            self.Page("Cheating detected!", [self.Page.Article("This run will not count as you've been cheating during typing", "If it is a error - contact with developer.")], destination=lambda: self.app.Gui.mainMenu()).load()

    # Game 

    class Game:
        def __init__(self, app) -> None:
            self._app = app
        def thegame(self, type: int):
            
            if type == 0:
                with open("resources/texts.json", "r") as file:
                    texts = json.load(file)["texts"]
                    text = texts[random.randint(0, len(texts)-1)]["content"]

            elif type == 1:
                with open("resources/hardTexts.json", "r") as file:
                    texts = json.load(file)["texts"]
                    text = texts[random.randint(0, len(texts)-1)]["content"]

            elif type == 2:
                with open("resources/insaneTexts.json", "r") as file:
                    texts = json.load(file)["texts"]
                    text = texts[random.randint(0, len(texts)-1)]["content"]
 
            inputText = ""
            mistakes = 0
            totalTyped = 0
            startedTime = time.time()
            timings = [startedTime]
            while (text != inputText):
                clear()
                print(text)
                if totalTyped != 0:
                    print("press ESC to exit | WPM: " + str(round((len(inputText.split(" ")) / (time.time() - startedTime)) * 100, 2)) + " | Accuracy: " + str(round((totalTyped - mistakes) / totalTyped, 2) * 100) + "%")
                else:
                    print("press ESC to exit | press TAB to change text")
                displayText = ""
                for i, char in enumerate(inputText):
                    if i < len(text):
                        if char == text[i]:
                            displayText += char
                        else:
                            if char != " ":
                                displayText += col.Fore.RED + char + col.Style.RESET_ALL
                            else:
                                displayText += col.Back.RED + char + col.Style.RESET_ALL
                    else:
                        displayText += col.Fore.RED + char + col.Style.RESET_ALL
                remainingText = text[len(inputText):]
                for char in remainingText:
                    if char == " ":
                        displayText += char
                    else:
                        displayText += col.Fore.RED + char + col.Style.RESET_ALL
                        pass
                print(displayText + col.Style.RESET_ALL)
                inputChar = App.gettype()
                timings.append(time.time())
                totalTyped += 1

                if inputChar == "BACKSPACE":
                    mistakes += 1
                    inputText = inputText[:-1]
                elif inputChar == "ESC":
                    self._app.Gui.gameUI()
                elif inputChar == "TAB":
                    self.thegame(type)
                elif inputChar == "CMD":
                    pass
                elif inputChar == "ERROR":
                    inputChar = ""
                else:
                    inputText += inputChar
            # checking AC
            wpm = round((len(inputText.split(" ")) / (time.time() - startedTime)) * 100, 2)
            accuracy = round((totalTyped - mistakes) / totalTyped, 2) * 100
            verdict = self._app.O0.Oo(timings, accuracy, wpm).O0o()
            if verdict:
                self._app.Gui.cheater()
            else:
                # saving run
                current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
                self._app.Player.runs[current_time] = {"WPM": wpm, "Accuracy": accuracy, "Type": type}
                # updating stats
                self._app.Player.save()
                self._app.Player.update()
                self._app.Player.save()
                # showing end game screen
                self._app.Gui.endGame(wpm, accuracy, mistakes)
