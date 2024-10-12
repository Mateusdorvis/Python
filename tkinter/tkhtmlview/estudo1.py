import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
root.title('Rederizando um conteúdo html com tkinter')
html_conteudo = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body bgcolor="red">
    <h1>Olá meu nome é Mateus e estou redenrizano pela primeira vez a página html na biblioteca tkinter (python)</h1>
    
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. In, sunt vitae architecto quam voluptatibus dolorem aliquam? Fugit error voluptates nam esse, rem laborum. Magni nesciunt animi necessitatibus exercitationem velit dolorem.</p>
   
   
</body>
</html>
'''
pagina = HTMLLabel(root, html=html_conteudo)#redenriza um conteúdo html dentro de uma label
pagina.pack()
root.mainloop()