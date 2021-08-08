from PyQt5.QtWidgets import QMessageBox

class IHMError():

	def __init__(self,typeError):
		"""
		:param typeError: the type of error
		:type typeError: str
		"""
		try:
			self.msg = QMessageBox()
			self.msg.setWindowTitle("Erreur")
			error = getattr(self,typeError) # Get the message for the corresponding error
			self.msg.setText(error())
			self.msg.setIcon(QMessageBox.Warning)
		except KeyError:
			return None
		finally:
			msgPop = self.msg.exec_()

	def URL_Error(self):
		return "L'URL fournie n'est pas valide!"

	def folder_Error(self):
		return "Le dossier fourni n'est plus valide!"
