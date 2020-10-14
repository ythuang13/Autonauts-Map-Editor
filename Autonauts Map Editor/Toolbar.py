import PySimpleGUI as sg


class Toolbar:

    def __init__(self):
        sg.theme("BlueMono")
        self.toolsLayout = self.toolbarLayoutSetup()
        self.colorLayout = self.colorLayoutSetup()
        self.layout = [[sg.Frame("Tools", self.toolsLayout), sg.VerticalSeparator(), sg.Frame("Tile types", self.colorLayout)]]
        self.toolbarWindow = sg.Window("Toolbar", self.layout, keep_on_top=True)


    def toolbarLayoutSetup(self) -> list:
        temp = [[sg.Button("brush"), sg.Button("exit/save", tooltip="exit and save option", k="-exit-"), sg.Button("Screenshot(F12)", tooltip="save a screenshot to your desktop", k="-screenshot-")],
                [sg.Slider(range=(1, 10), default_value=2, orientation="h", k="-brushSize-", relief="raised"), sg.Button("reset", tooltip="reset back to original", k="-reset-")]
                ]
        return temp


    def colorLayoutSetup(self) -> list:
        temp = [[sg.Combo(["0 grass", "1 dirt", "6 coast", "7 ocean", "8 lake", "9 shallow water", "10 sand", "12 swamp", "14 metal ore", "19 clay"], default_value="0 grass", key="-tileTypeSelect-")],
                ]
        return temp


    def quit(self):
        self.toolbarWindow.close()


if __name__ == "__main__":
    t1 = Toolbar()