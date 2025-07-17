from textual.app import App, ComposeResult
from textual.widgets import Button, Digits, Footer, Header
from textual.containers import HorizontalGroup, VerticalGroup, VerticalScroll

from make_music import *
from play_music import *

class StartMenu(VerticalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "exit":
            # For now just quit the app; can add other logic here before quitting
            self.app.exit()


    def compose(self) -> ComposeResult: # Just filler for now to see how this looks
        """Create child widgets of a stopwatch."""
        yield Button("Resume", id="resume", variant="primary")
        yield Button("New Game", id="new_game", variant="primary")
        yield Button("Chill Mode", id="chill_mode", variant="primary")
        yield Button("Credits", id="credits", variant="primary")
        yield Button("Exit", id="exit", variant="error")

class LofiText():
    TEXT = '''
 _          _____ _ 
| |    ___ |  ___(_)
| |   / _ \| |_  | |
| |__| (_) |  _| | |
|_____\___/|_|   |_|
    '''

    

class TimelessLoFi(App):
    CSS_PATH = "padding.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield HorizontalGroup(StartMenu())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = TimelessLoFi()
    app.run()
    # make_music()
    # play_music()
