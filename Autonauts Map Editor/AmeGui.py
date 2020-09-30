import PySimpleGUI as sg
import os
from pathlib import Path
import AmeFunctions as ame
import AmeMap as am


def main():
    sg.theme("BlueMono")

    layout = [[sg.Text("Autonaunts Map Editor")],
              [sg.InputText("input file path", disabled=True, key="-IN-"),
               sg.FileBrowse("import",
                             initial_folder = str(Path.home()) + r"\AppData\LocalLow\Denki Ltd\Autonauts\Saves"),
               sg.Button("load", size=(5, 0))],
              [sg.InputText("export file path", disabled=True, key="-OUT-"), sg.FileSaveAs("export"), sg.Button("export")],
             ]

    window = sg.Window("Autonaunts Map Editor", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "import":
            print("Select import file path")
        elif event == "export":
            print("Select export file path")
        elif event == "load":
            am.launchMap(ame.worldTxtLoad(values["-IN-"]))
            
            

    window.close()

if __name__ == "__main__":
    main()