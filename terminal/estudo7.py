from textual.app import App
from textual.widgets import Header, Footer, Label
x = input('Escreva algo :')
class Mateus(App):
    """A Textual app to manage stopwatches."""



    def compose(self):
        """Create child widgets for the app."""
       
        yield   Header()
        yield   Footer()
        yield Label(x)
if __name__ == "__main__":
    app = Mateus()
    app.run()