import PySimpleGUI as sg


class Toolbar:

    def __init__(self):
        sg.theme("BlueMono")
        self.toolsLayout = self.toolbarLayoutSetup()
        self.colorLayout = self.colorLayoutSetup()
        self.layout = [[sg.Frame("Tools", self.toolsLayout), sg.VerticalSeparator(), sg.Frame("Tile types", self.colorLayout)]]


    def toolbarLayoutSetup(self) -> list:
        temp = [[sg.Button("brush"), sg.Button("exit/save"), sg.Button("Screenshot")],
                [sg.Slider(range=(1, 5), default_value=2, orientation="h"), sg.Button("clear map")]
                ]
        return temp


    def colorLayoutSetup(self) -> list:
        temp = [[sg.Button("green"), sg.Button("brown"), sg.Button("yellow")],
                [sg.Button("blue"), sg.Button("black"), sg.Button("grey")]
                ]
        return temp


    def launchToolbar(self):
        self.toolbarWindow = sg.Window("Toolbar", self.layout, keep_on_top=True)
        
        running = True
        while running:
            event, values = self.toolbarWindow.read()
            if event == sg.WIN_CLOSED:
                break


if __name__ == "__main__":
    t1 = Toolbar()
    t1.launchToolbar()