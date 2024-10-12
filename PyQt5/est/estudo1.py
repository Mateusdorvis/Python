from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class App(QWidget): #herda todos os atributos da classe QWidget, dessa forma criando uma janela
    def __init__(self):
        super().__init__()
        
        # Configurações da janela
        self.setWindowTitle('PyQt5 Example') #titulo da janela
        self.setGeometry(100, 100, 280, 80) #geometria da janela
        # Layout
        layout = QVBoxLayout() #cria  uma layout
        # Cria um botão e adiciona ao layout
        button = QPushButton('Click Me') #instancia a classe button
        button.clicked.connect(self.on_click)
        layout.addWidget(button) #adiciona o layout button
        # Configura o layout da janela
        self.setLayout(layout)
    #função
    def on_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show() #mostra a janela
    app.exec_()#executa 
