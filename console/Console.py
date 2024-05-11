import curses
import time
import sys
import os
import threading
import subprocess

screen = curses.initscr()

curses.noecho()
curses.start_color()
curses.use_default_colors()
curses.init_color(1, 100, 100, 100)
# curses.init_color(curses.COLOR_GREY, 100, 100, 100)
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
curses.init_pair(2, 1, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

windows = []

def init():
    screen.clear()
    ROWS, COLS = screen.getmaxyx()
    sizRow = int((ROWS-1)/3)
    sizCol = int((COLS-1)/2)

    global curdir
    global windows
    global oldCOut
    curdir = os.getcwd()
    oldCOut = f"NfConsole:{str(curdir)}>"
    windows = []
    leftWin = curses.newwin(sizRow*2, sizCol, 0, 0)
    rightWin = curses.newwin(sizRow*2, sizCol, 0, sizCol+1)
    bottWin = curses.newwin(sizRow, sizCol*2, sizRow*2+1, 0)
    windows.append(leftWin)
    windows.append(rightWin)
    windows.append(bottWin)
    leftWin.scrollok(True)
    rightWin.scrollok(True)
    bottWin.scrollok(True)
    line1 = curses.newwin(sizRow*2, 1, 0, sizCol)
    line2 = curses.newwin(1, sizCol*2, sizRow*2, 0)
    windows.append(line1)
    windows.append(line2)

    leftWin.bkgd(' ', curses.color_pair(2))
    rightWin.bkgd(' ', curses.color_pair(2))
    bottWin.bkgd(' ', curses.color_pair(3))
    line1.bkgd(' ', curses.color_pair(1))
    line2.bkgd(' ', curses.color_pair(1))
    
    bottWin.addstr(0, 0, oldCOut)

def checkConsole(currCommand, currWin, pressedKey):
    global oldCOut
    global Running
    global curdir
    
    if pressedKey == 10:
        if currCommand == "exit":
            Running = False
        elif currCommand == "clear":
            oldCOut = f"NfConsole:{str(curdir)}>"
            windows[currWin].clear()
        elif currCommand[:2] == "cd":
            try:
                os.chdir(currCommand[3:])
                curdir = os.getcwd()
            except:
                oldCOut += f"Error: {currCommand[3:]} is not a valid directory\n"
        elif currCommand[:4] == "echo":
            if len(currCommand[5:].split(">>")) == 2:
                try:
                    with open(currCommand[5:].split(">>")[1], "a") as file:
                        file.write(currCommand[5:].split(">>")[0])
                except:
                    oldCOut += f"Error: {currCommand[5:].split('>>')[1]} is not a valid file\n"
            else:
                oldCOut += f"{currCommand[5:]}\n"
        elif currCommand[:2] == "ls":
            try:
                oldCOut += "\n"
                for file in os.listdir(curdir):
                    oldCOut += f"{file}\n"
            except:
                oldCOut += f"Error: {curdir} is not a valid directory\n"
        elif currCommand[:4] == "nano":
            try:
                with open(currCommand[5:], "w") as file:
                    file.write("")
                subprocess.run(["nano", currCommand[5:]])
            except:
                oldCOut += f"\nWindows cannot use nano\n"
        elif currCommand[:2] == "rm":
            try:
                os.remove(currCommand[3:])
            except:
                oldCOut += f"Error: {currCommand[3:]} is not a valid file\n"
        oldCOut += f"{currCommand}\nNfConsole:{str(curdir)}>"
        currCommand = ""
    elif pressedKey == 8:
        currCommand = currCommand[:-1]
    else:
        currCommand += chr(pressedKey)
    cOut = oldCOut + currCommand
    windows[currWin].clear()
    windows[currWin].addstr(0, 0, str(cOut))
    windows[currWin].refresh()
    return currCommand

def changeColor(currWin):
    windows[currWin].bkgd(' ', curses.color_pair(2))
    windows[currWin].refresh()
    currWin = (currWin+1)%3
    windows[currWin].bkgd(' ', curses.color_pair(3))
    windows[currWin].refresh()
    return currWin

def main():
    global windows
    global oldCOut
    global curdir
    global Running
    currCommand = ""
    
    for win in windows:
        win.refresh()
    Running = True
    currWin = 2
    while Running:
        try:
            pressedKey = windows[currWin].getch()
            if pressedKey:
                windows[currWin].refresh()
                if pressedKey == 9:
                    currWin = changeColor(currWin)
                elif pressedKey == 27:
                    Running = False
                    break
                elif currWin == 2:
                    currCommand = checkConsole(currCommand, currWin, pressedKey)
            # time.sleep(0.1)
        except KeyboardInterrupt:
            Running = False
            break
        
init()
main()