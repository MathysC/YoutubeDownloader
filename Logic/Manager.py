
from IHM.IHMError import IHMError
from PyQt5 import QtWidgets
from pytube import YouTube
import re # Regular Expression
import os 


class Manager():

	def __init__(self):
		self.path = "" 
		self.url = ""

	def download_MP4(self,url):
		self.url = url
		if self.verify_folder() and self.verify_link():
			try:
				yt = YouTube(self.url)
			except VideoUnavailable:
				IHMError('videoUnavailable_Error')
				return None
			finally:
				print("début du téléchargement")
				stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
				downloadpath = stream.download(output_path=self.path)
				print(downloadpath)

	def download_MP3(self):
		pass		


	def select_folder(self,ui):
		"""
		:param self.path: the Folder used for the OutCome
		:type self.path: str
		:return path_match: true if the folder exists
		:rtype: bool
		"""
		self.path = QtWidgets.QFileDialog.getExistingDirectory(ui.MainWindow, 'Select Folder')
		if self.verify_folder():
			ui.l_currentFolder.setText(self.path)

	def verify_folder(self):
		"""
		:param self.path: the Folder used for the OutCome
		:type self.path: str
		:return path_match: true if the folder exists
			A messageBox appears if false
		:rtype: bool
		"""
		path_match = os.path.isdir(self.path)
		if not path_match:
			IHMError("folder_Error")

		return path_match

	def verify_link(self):
		"""
		:param self.url: the 'possible' YouTube URL
		:type self.url: str
		:return youtube_regex_match: true if the url is a YouTube URL.
			A messageBox appears if false
		:rtype: bool
			..seealso:: https://stackoverflow.com/questions/4705996/python-regex-convert-youtube-url-to-youtube-video/19161373
		"""
		youtube_regex = (
			r'(https?://)?(www\.)?'
			'(youtube|youtu|youtube-nocookie)\.(com|be)/'
			'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

		youtube_regex_match = re.match(youtube_regex, self.url)

		if not youtube_regex_match:
			IHMError("URL_Error")
		return youtube_regex_match