#criando um arquivo pdf com a extensão da biblioteca PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen  import canvas

#criando um arquivo
meu_canvas = canvas.Canvas('arquivo_criado2.pdf', pagesize=letter)

meu_canvas.drawString(x=0, y=600, text='Imagem com texto!') #colocando o texto em uma posição determinada com as coordenadas x e y
meu_canvas.drawImage(image=r'C:\xampp\htdocs\progr\python\ARTE\skylite\oi.jpg', x=0, y=0, width=300, height=300)
meu_canvas.save()
print('Arquivo criado com sucesso !')