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
			msgPop = self.msg.exec_()
		except (KeyError,AttributeError) as e:
			print(f"Wrong typeError : You used {typeError = }")
			print(e)

	"""
	Functions that returns a specific message for the type of error
	"""
	def URLError(self):
		return "L'URL fournie n'est pas valide!"

	def folder_Error(self):
		return "Le dossier fourni n'est pas valide!"

	def videoUnavailable_Error(self):
		return "Cette vidéo n'est plus disponible!"

	def fileExistsError_Error(self):
		return "Ce fichier existe déjà!"

	def random(self):
		return "Une erreur inconnu est survenue!"