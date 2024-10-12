from rich.text import Text
from rich.console import Console
terminal = Console()
texto_modiifcado = Text('Olá mundo !, este texto está com a cor de fundo amarelo', style='on yellow')#aplica o estilo ativando (on) a cor de fundo

print('Texto normal : ',texto_modiifcado)
terminal.print('Texto modificado com rich : ',texto_modiifcado)