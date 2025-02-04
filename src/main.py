from typing import final, override
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Input
from textual.containers import VerticalScroll

#class MOD(VerticalScroll):
#    def __init__(self, mod: str, **kwargs):
#        super().__init__(**kwargs)
#
#        self.mod: str = mod
#
#    @override
#    def compose(self) -> ComposeResult:
#        yield Label(self.mod)
#        return super().compose()

class Register(VerticalScroll):

    def compose(self) -> ComposeResult:
        yield Label("""
 /$$   /$$                        
| $$$ | $$                        
| $$$$| $$  /$$$$$$  /$$  /$$  /$$
| $$ $$ $$ /$$__  $$| $$ | $$ | $$
| $$  $$$$| $$$$$$$$| $$ | $$ | $$
| $$\  $$$| $$_____/| $$ | $$ | $$
| $$ \  $$|  $$$$$$$|  $$$$$/$$$$/
|__/  \__/ \_______/ \_____/\___/ 
""", classes="mod")

        yield VerticalScroll(
            Input(placeholder="WAS DEIN vorname DIGGI?!", classes="name_in upper"),
            Input(placeholder="ALDA GIB nachname!", classes="name_in upper"),
            Button("Abbrechen", id="back", variant="error"),
            classes="mainG",
        )


class MainSelection(VerticalScroll):

    @override
    def compose(self) -> ComposeResult:
        yield Label("""
 /$$   /$$           /$$ /$$           /$$
| $$  | $$          | $$| $$          | $$
| $$  | $$  /$$$$$$ | $$| $$  /$$$$$$ | $$
| $$$$$$$$ /$$__  $$| $$| $$ /$$__  $$| $$
| $$__  $$| $$$$$$$$| $$| $$| $$  \ $$|__/
| $$  | $$| $$_____/| $$| $$| $$  | $$    
| $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/ /$$
|__/  |__/ \_______/|__/|__/ \______/ |__/
""", classes="mod")

        yield VerticalScroll(
            Button("Registrieren", id="reg", variant="success", classes="upper"),
            Button("Anmelden", id="anm", variant="primary", classes="upper"),
            Button("Beenden", id="bee", variant="error"),
            classes="mainG"
        )

@final
class Main(App):
    CSS_PATH = "style.css"

    @override
    def compose(self) -> ComposeResult:
        yield Header()

        yield MainSelection()

        yield Footer()
        return super().compose()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "reg":
                self.query("MainSelection").remove()
                self.mount(Register())
            case "anm":
                self.query("MainSelection").remove()
            case "back":
                self.query("Register").remove()
                self.mount(MainSelection())
            case _:
                pass


if __name__ == "__main__":
    app = Main()
    app.title = "FitnessFirst"
    app.run()
