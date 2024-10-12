from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

terminal = Console()

# Criando um layout
layout = Layout()
#craindo um layout na coluna
layout.split_column(
      Layout(Panel('Painel 1', style='on red'), ratio=1), #criando uma painel dentro de um layout
      Layout(Panel('Painel 2', style='on blue'), ratio=2)
)

terminal.print(layout)