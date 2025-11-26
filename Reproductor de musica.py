from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import pygame,sys

app = QApplication(sys.argv)

pygame.init()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inicio')
        self.move(200, 200)
        self.resize(640, 480)
        
        self.label = QLabel('Reproductor de musica')
        self.label2 = QLabel("Estado:")
        
        self.button1=QPushButton('Iniciar')
        self.button2=QPushButton('Parar')
        self.button3=QPushButton('Pausa')
        self.button4=QPushButton('Resume')
        
        self.button1.clicked.connect(self.play)
        self.button2.clicked.connect(self.stop) 
        self.button3.clicked.connect(self.pause) 
        self.button4.clicked.connect(self.resume)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)
        
    def play(self):
        inicio, ok = QtWidgets.QInputDialog.getText(self, "Hola", "Elige la musica")
        if ok:
            if inicio in inicio:
                pygame.mixer.music.load(f'{inicio}.wav')
                pygame.mixer.music.play()
                print('Song Playing')
        else:
            self.label.setText("Operation cancelled.")
        
    def stop(self):
        pygame.mixer.music.stop()
        self.label2.setText("Estado: Song Stop")
        print('Song Stop')

    def pause(self):
        pygame.mixer.music.pause()
        pausa = "Song PAUSED"
        self.label2.setText(f"Estado: {pausa}")
        print(pausa)

    def resume(self):
        pygame.mixer.music.unpause()
        self.label2.setText("Estado: Song RESUMED")
        print("Song RESUMED")

window = MyWindow()
window.show()
app.exec_()