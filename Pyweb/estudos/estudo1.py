import webview


def ola_mundo():
    return 'Olá mundo'

conteudo_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body >
    <h1>Olá meu nome é Mateus e estou redenrizano pela primeira vez a página html na biblioteca tkinter (python)</h1>
    
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. In, sunt vitae architecto quam voluptatibus dolorem aliquam? Fugit error voluptates nam esse, rem laborum. Magni nesciunt animi necessitatibus exercitationem velit dolorem.</p>
   
   
</body>
</html>
'''

# Cria uma janela
window = webview.create_window('Minha Aplicação', hmtm = conteudo_html) #redenriza uma página hmtml

# Define a API que pode ser chamada pelo JavaScript
webview.start()


