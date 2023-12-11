import os
import json
import zipfile
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def listMods():
    with open('mods.json', 'r') as openfile:
        json_object = json.load(openfile)

    for x, item in enumerate(json_object):
        if item != "game":
            print(x, ".", item)

    return json_object

def installMods(modsDirs):
    modNames = filedialog.askopenfilenames(title="Select mods to install.", filetypes=[('zip files', '*.zip')])
    for fileName in modNames:
        if json.load(open('mods.json', 'r')).get(os.path.basename(fileName).replace(".zip","")) != None:
            print("[X] " + os.path.basename(fileName).replace(".zip","") + " is already installed.")
            continue
        newEntry = {fileName:[]}
        
        with zipfile.ZipFile(fileName, 'r') as zip_ref:
            for item in zip_ref.namelist():
                if "." in item:
                    newEntry[fileName] = newEntry[fileName] + [item]
                    break

            if (newEntry[fileName])[0].split("/")[0] not in modsDirs and (newEntry[fileName])[0].split("/")[1] in modsDirs:
                for item in zip_ref.infolist():
                    if item.is_dir():
                        continue
                    item.filename = (item.filename).replace((newEntry[fileName])[0].split("/")[0], "")
                    zip_ref.extract(item, json.load(open('mods.json', 'r')).get("game"))

            elif (newEntry[fileName])[0].split("/")[0] in modsDirs:
                zip_ref.extractall(path=json.load(open('mods.json', 'r')).get("game"))

            else:
                print("Bad zip hierarchy, mod not installed.")
                return 1

            newEntry = {os.path.basename(fileName).replace(".zip",""):[]}
            for item in zip_ref.infolist():
                if item.is_dir():
                    continue
                newEntry[os.path.basename(fileName).replace(".zip","")] = newEntry[os.path.basename(fileName).replace(".zip","")] + [item.filename]
        
        write2JsonFile(newEntry)
        print("[OK] " + os.path.basename(fileName).replace(".zip","") + " installed.")

def uninstallMods():
    jsonMods = listMods()
    lstMods = [""]
    for item in jsonMods:
        if item != "game":
            lstMods.append(item)

    print("Select a mod or mods separated by a comma, to uninstall.")
    option = input("> ")
    toUninstall = option.split(",")
    for index in toUninstall:
        if index.isdigit() and index != "0" and int(index) < len(lstMods):
            for file in jsonMods.get(lstMods[int(index)]):
                if file[0] != "/":
                    file = "/" + file
                try:
                    os.remove(json.load(open('mods.json', 'r')).get("game") + file)
                except:
                    pass
            removeFromJsonFile(lstMods[int(index)])
            print(lstMods[int(index)] + " files removed.")

def write2JsonFile(new_data, filename='mods.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data
        file_data[list(new_data.keys())[0]] = new_data.get(list(new_data.keys())[0])
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def removeFromJsonFile(bye, filename='mods.json'):
    with open(filename,'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # pop bye
        file_data.pop(bye)
        with open(filename,'w') as file2:
            # convert back to json.
            json.dump(file_data, file2, indent = 4)

def startJsonFile():
    if not os.path.exists("mods.json"):
        game_path = filedialog.askdirectory(title="Select game installation folder.")
        toWrite = '{"game":"' + game_path + '"}'
        with open("mods.json", "w") as outfile:
            outfile.write(toWrite)
    elif json.load(open('mods.json', 'r')).get("game") == None:
        exit("Game directory not found inside mods.json")


if __name__ == '__main__':
    startJsonFile()
    # adjust root directories depending of the game
    modsDirs = ["archive", "bin", "engine", "mods", "r6", "red4ext", "tools"]
    running = True

    while running:
        # DISPLAY MENU
        print("Installing mods under: "+ json.load(open('mods.json', 'r')).get("game"))
        print("0. Exit")
        print("1. List installed mods in installation order")
        print("2. Install mod(s)")
        print("3. Uninstall mod(s)")

        # PROCESS USER INPUT
        userInput = input("> ")
        match userInput:
            case "0": # exit
                exit()
            case "1": # list mods
                listMods()
            case "2": # install mods
                installMods(modsDirs)
            case "3": # uninstall mods
                uninstallMods()
        input("Press enter to continue...\n")
        os.system('cls')