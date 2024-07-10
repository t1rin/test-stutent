import dearpygui.dearpygui as dpg

from gui.windows import MainWindow
from gui.windows import SettingsWindow


def show_window():
    dpg.configure_item("hidden", show=True)

def main():
    dpg.create_context()
    dpg.create_viewport(title='Test Student', width=640, height=360)

    # main_window = MainWindow()
    # settings_window = SettingsWindow()
    
    # main_window.register()
    # settings_window.register()

    with dpg.window(tag="Window", width=200):
        dpg.add_button(tag="button", label="Show window", callback=show_window)


    with dpg.window(tag="hidden", width=200, show=False, pos=[100, 100]):
        dpg.add_text("This is hidden window")
    
    dpg.setup_dearpygui()
    dpg.show_viewport()

    # dpg.set_primary_window("Main Window", True)
    # dpg.set_primary_window("Settings Window", True)

    dpg.set_primary_window("hidden", True)
    dpg.set_primary_window("Window", True)

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()