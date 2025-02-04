from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, Button, Input
from textual.containers import VerticalScroll


class Register(VerticalScroll):

    def compose(self) -> ComposeResult:
        yield Input(placeholder="WAS DEIN vorname DIGGI?!", classes="name_in")
        yield Input(placeholder="ALDA GIB nachname!", classes="name_in")

class MainSelection(VerticalScroll):

    def compose(self) -> ComposeResult:
        yield Button("Registrieren", id="reg", variant="success")
        yield Button("Anmelden", id="anm", variant="primary")
        yield Button("Beenden", id="bee", variant="error")

                
                



class Main(App):
    CSS_PATH="style.css"
    def compose(self) -> ComposeResult:
        yield Header()
        
        yield Label("""
 /$$   /$$           /$$ /$$           /$$
| $$  | $$          | $$| $$          | $$
| $$  | $$  /$$$$$$ | $$| $$  /$$$$$$ | $$
| $$$$$$$$ /$$__  $$| $$| $$ /$$__  $$| $$
| $$__  $$| $$$$$$$$| $$| $$| $$  \ $$|__/
| $$  | $$| $$_____/| $$| $$| $$  | $$    
| $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/ /$$
|__/  |__/ \_______/|__/|__/ \______/ |__/""", id="mod")
        
        yield MainSelection()

        yield Footer()
        return super().compose()
    

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case 'reg':
                self.query("MainSelection").remove()
                self.mount(Register())
            case 'anm':
                self.query("MainSelection").remove()
                
            case _:
                pass
    
    



if __name__ == "__main__":
    app = Main()
    app.title="FitnessFirst"
    app.run()