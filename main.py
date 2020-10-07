from PyQt5.QtWidgets import *
import random

dic = ["Contrary" 
,"to"
,"popular" 
,"belief"
,"LoremIpsum"
,"is"
,"not"
,"simply"
,"random"
,"text"
,"It"
,"has"
,"roots"
,"in"
,"a"
,"piece"
,"of"
,"classical"
,"Latin"
,"literature"
,"from"
,"45"
,"BC"
,"making"
,"it"
,"over"
,"2000"
,"years"
,"old"
,"Richard"
,"McClintock"]
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
lbl = QLabel('Start')

layout.addWidget(lbl)
e4 = QLineEdit()
def changeWord():
	newint = random.randint(0, len(dic))
	lbl.setText(dic[newint])


def textchanged(text):
	print ("contents of text box: "+text)
	if text == lbl.text():
		e4.setText('')
		changeWord()
e4.textChanged.connect(textchanged)
layout.addWidget(e4)

window.setLayout(layout)
window.show()
app.exec_()


