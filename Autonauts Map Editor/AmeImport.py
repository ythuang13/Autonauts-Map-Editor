import os
from pathlib import Path
import PySimpleGUI as sg
from AmeMap import launchMap


def main():
    sg.theme("BlueMono")

    layout = [[sg.Text("Autonauts Map Import")],
              [sg.InputText("Import file path, world saves are named World.txt", disabled=True, key="-IN-"),
               sg.FileBrowse("import", file_types=(("Word.txt", "*.txt"),),
                             initial_folder = str(Path.home()) + r"\AppData\LocalLow\Denki Ltd\Autonauts\Saves"),
               sg.Button("load")]
             ]

    importWindow = sg.Window("Autonauts Map Editor - import", layout)

    
    while True:
        event, values = importWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "import":
            pass
        elif event == "load":
            importWindow.close()
            launchMap(values["-IN-"])
            

    importWindow.close()

if __name__ == "__main__":
    main()
