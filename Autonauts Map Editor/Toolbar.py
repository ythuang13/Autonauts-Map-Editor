import PySimpleGUI as sg


class Toolbar:

    def __init__(self):
        sg.theme("BlueMono")
        self.toolsLayout = self.toolbarLayoutSetup()
        self.colorLayout = self.colorLayoutSetup()
        self.layout = [[sg.Frame("Tools", self.toolsLayout), sg.VerticalSeparator(), sg.Frame("Tile types", self.colorLayout)]]
        self.toolbarWindow = sg.Window("Toolbar", self.layout, keep_on_top=True)


    def toolbarLayoutSetup(self) -> list:
        temp = [[sg.Button("brush"), sg.Button("exit/save"), sg.Button("Screenshot")],
                [sg.Slider(range=(1, 10), default_value=2, orientation="h", k="-brushSize-", relief="raised"), sg.Button("clear map")]
                ]
        return temp


    def colorLayoutSetup(self) -> list:
        temp = [[sg.OptionMenu(["green", "yellow", "brown"], default_value="green")],
                ]
        return temp


    def quit(self):
        self.toolbarWindow.close()


if __name__ == "__main__":
    t1 = Toolbar()