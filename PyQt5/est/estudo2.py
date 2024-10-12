from PyQt5.QtWidgets import *
aplication = QApplication([])

janela =  QWidget()
janela.setWindowTitle('Minha primeira aplicação com pyqt')

layout_v =  QVBoxLayout()

label =  QLabel('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body{
        background-color: red;
    }
</style>
<body>
    <h1>Olá mundo</h1>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime alias maiores tenetur ipsum! Ullam, dolorem! Quaerat dolore magnam quis laudantium itaque assumenda dicta aut veniam, quo voluptatem. Ipsum, quia a!</p>
</body>
</html>
''')
layout_v.addWidget(label)

janela.setLayout(layout_v)

janela.show()
aplication.exec_()

