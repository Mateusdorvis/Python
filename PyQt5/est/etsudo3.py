from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl 

aplication = QApplication([])
janela =  QMainWindow()
navegador  = QWebEngineView()
navegador.setUrl(QUrl('https://www.youtube.com'))#redenrizando a página html externo
janela.setCentralWidget(navegador)
janela.show()
aplication.exec_()

