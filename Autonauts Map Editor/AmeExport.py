import os
from pathlib import Path
import PySimpleGUI as sg

def exportMain(world):
    sg.theme ("BlueMono")

    layout = [[sg.Text("Autonaunts Map Export")],
              [sg.InputText("Select folder path to save as", disabled=True, key="-OUT-"),
               sg.FolderBrowse("path", initial_folder = str(Path.home()) + r"\AppData\LocalLow\Denki Ltd\Autonauts\Saves"), sg.Button("save as")]
             ]

    exportWindow = sg.Window("Autonaunts Map Editor - export", layout)
    
    while True:
        event, values = exportWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "save as":
            world.exportWorld(values["-OUT-"])

    exportWindow.close()

