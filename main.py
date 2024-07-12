import wx, sys

...

from gui.windows import (MainWindow, 
    SettingsWindow)


def check_path_in_args() -> bool:
    args = sys.args( )

def main():
    app = wx.App()

    

    app.MainLoop()


if __name__ == "__main__":
    main()