from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
from alien_invasion import run_game
class LoginDemo(QWidget):
	def __init__(self):
		super().__init__()
		
		self.L_input = QLineEdit()
		self.L_password = QLineEdit()
		reg = QRegExp("[a-zA-Z0-9]+$")
		pValidator = QRegExpValidator(self)
		pValidator.setRegExp(reg)
		
		self.L_input.setValidator(pValidator)
		self.L_input.setMaxLength(16)
		self.L_password.setEchoMode(QLineEdit.Password)
		self.L_input.setMaxLength(16)
		flo = QFormLayout()
		flo.addRow('帐号:',self.L_input)
		flo.addRow('密码',self.L_password)
		self.bt1 = QPushButton('登陆')
		self.bt1.clicked.connect(self.btnPress1)
		self.bt2 = QPushButton('注册')
		self.bt2.clicked.connect(self.btnPress2)
		flo.addRow(self.bt1,self.bt2)
		self.setLayout(flo)
	def btnPress1(self):
		print(self.L_input.text())
		print(self.L_password.text())
		filename = r'f:\PYTHON\json\user.json'
		with open(filename) as f_obj:
			username = json.load(f_obj)
		if self.L_input.text() in username.keys():
			if username[self.L_input.text()] == self.L_password.text():
				print('登陆成功')
				dialog = QDialog()
				l1 = QLabel(dialog)
				l1.setText('登陆成功')
				l1.move(50,50)
				l1.setAlignment(Qt.AlignCenter)
				l1.setFont(QFont('Arial',13))
				bt1 = QPushButton('开始游戏！',dialog)
				bt1.move(50,80)
				dialog.setWindowTitle('OK')
				dialog.setWindowModality(Qt.ApplicationModal)
				
				bt1.clicked.connect(self.begin_game)
				dialog.exec_()
				sys.exit()
			else:
				print('密码错误')
		else:
			print('不存在该用户')
	def begin_game(self):
		run_game()
	def btnPress2(self):
		print(self.L_input.text())
		print(self.L_password.text())
		filename = r'f:\PYTHON\json\user.json'
		with open(filename) as f_obj:
			username = json.load(f_obj)
		if self.L_input.text() in username.keys():
			print("该账户已经存在")
		else:
			username[self.L_input.text()] = self.L_password.text()
			with open(filename,'w') as f_obj:
				json.dump(username,f_obj)
			print("注册成功")
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = LoginDemo()
	win.show()
	sys.exit(app.exec_())