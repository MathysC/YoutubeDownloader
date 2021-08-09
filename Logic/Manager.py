
from IHM.IHMError import IHMError
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from pytube import exceptions
from pytube import YouTube
import os 


class Manager():

	def __init__(self):
		"""
		Constructor of Manager
		initialize 'folder' and 'url' as str 
		"""
		self.folder = os.getcwd() 
		self.url = ""


	def download(func):
		"""
		Decorator pattern used for downloading the YouTube url
		:param func: the function to download the YouTube url
		:type func: function
		:return wrapper: the wrapper function
		:rtype wrapper: function
		"""
		def wrapper(self,url):
			"""
			The wrapper of this part and the other function depends on the type of download
			:param url: the url of the YouTube video
			:type url: str
			:return val: the 'other' function used in wrapper
			:rtype val: function
			:raise exceptions.VideoUnavailable: the video is unavailable
			:raise exception: if another type of exception raises, create a random advert
			.. seealso:: self.download_MP3
			.. seealso:: self.download_MP4
			.. seealso:: IHMError
			"""
			self.url = url
			if self.verify():
				try:
					yt = YouTube(self.url) # By creating a Youtube, if the video is unavailable on YouTube raise a videoUnavailable error
					val = func(self=self,yt=yt) # Call the correct download function
				except exceptions.VideoUnavailable:
					IHMError('videoUnavailable_Error')
				except:
					IHMError('random')
					return None
				finally:
					return val
		return wrapper

	@download
	def download_MP4(self,yt):
		"""
		This function use the Decorator 'download' to... download mp4
		:param yt: the YouTube object to download
		:type yt: pytube.YouTube
		:return file: the absolute path of the created file
		:rtype file: str
		:raise exception: if another type of exception raises, create a random advert

		.. seealso:: IHMError
		"""
		file = ""
		try:
			# Download the video at its highest resolution
			stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
			file = stream.download(output_path=self.folder)
		except:
			IHMError('random')
		finally:
			# A message appears when the download is complete
			msg = QMessageBox()
			msg.setWindowTitle("Téléchargement...")
			msg.setText("Téléchargement terminé !")
			msg.setInformativeText(f"Veuillez trouver votre vidéo dans le dossier : {self.folder}")
			msg.setIcon(QMessageBox.information)
			msgPop = msg.exec_()
			return file
	@download
	def download_MP3(self,yt):
		"""
		This function use the Decorator 'download' to... download mp3
		:param yt: the YouTube object to download
		:type yt: pytube.YouTube
		:return file: the absolute path of the created file
		:rtype file: str
		:raise exception: if another type of exception raises, create a random advert
		
		.. seealso:: IHMError
		"""
		file = ""
		try:
			yt = YouTube(self.url) # By creating a Youtube, if the video is unavailable on YouTube raise a videoUnavailable error
			stream = yt.streams.filter(only_audio=True).first()
			file = stream.download(output_path=self.folder)
			pre, ext = os.path.splitext(file)
			os.rename(file,pre + '.mp3')
		except:
			IHMError('random')
		finally:
			# A message appears when the download is complete
			msg = QMessageBox()
			msg.setWindowTitle("Téléchargement...")
			msg.setText("Téléchargement terminé !")
			msg.setInformativeText(f"Veuillez trouver votre fichier audio dans le dossier : {self.folder}")
			msg.setIcon(QMessageBox.Information)
			msgPop = msg.exec_()
			return file

	def select_folder(self,ui):
		"""
		:param ui: ui of the MainWindow
		:type ui: PyQt5 object
		Change the folder by the chosen one in the directory dialog
		"""
		folder = QtWidgets.QFileDialog.getExistingDirectory(ui.MainWindow, 'Select Folder')
		self.folder = folder  if folder != '' else self.folder # If the user press "Cancel" use the precedent value
		if self.verify_folder():
			ui.l_currentFolder.setText(self.folder)

	def verify_folder(self):
		"""
		:return path_match: true if the folder exists
			A messageBox appears if false
		:rtype: bool
		:raise folder_Error: if the folder path isn't correct
		"""
		path_match = os.path.isdir(self.folder)
		if not path_match:
			IHMError("folder_Error")

		return path_match

	def verify_link(self):
		"""
		:return: True if the url is a YouTube URL.
		:rtype: bool
		:raise URL_Error: if the url isn't correct (regex return false)
			..seealso:: https://stackoverflow.com/questions/4705996/python-regex-convert-youtube-url-to-youtube-video/19161373
		"""
		import re
		youtube_regex = (
			r'(https?://)?(www\.)?'
			'(youtube|youtu|youtube-nocookie)\.(com|be)/'
			'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

		youtube_regex_match = re.match(youtube_regex, self.url)

		if not youtube_regex_match:
			IHMError("URL_Error")
			return False
		return True

	def verify_file(self):
		"""
		:return: True if the file can be create
		:rtype: bool
		:raise FileExistsError: if the file already exists 
		"""

		# Currently we check if the file exists no matter the extension
		import glob
		try:
			if glob.glob(self.folder + "\\" + YouTube(self.url).title + ".*"):
				raise FileExistsError
		except FileExistsError:
			IHMError("fileExistsError_Error")
			return False
		return True

	def verify(self):
		"""
		:return: True if 
			the file can be create,
			the url is a YouTube URL,
			the folder exists
		:rtype: bool
		"""

		return self.verify_file()  == self.verify_link() == self.verify_folder()

           
