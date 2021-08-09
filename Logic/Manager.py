
from IHM.IHMError import IHMError
from PyQt5 import QtWidgets, QtCore
from pytube import exceptions
from pytube import YouTube
import re # Regular Expression
import os 


class Manager():

	def __init__(self):
		self.folder = "" 
		self.url = ""


	def download(func):
		def wrapper(self,url):
			self.url = url
			if self.verify():
				try:
					yt = YouTube(self.url) # By creating a Youtube, if the video is unavailable on YouTube raise a videoUnavailable error
					val = func(self=self,yt=yt)
				except exceptions.VideoUnavailable:
					IHMError('videoUnavailable_Error')
					return None
				finally:
					return val
		return wrapper

	@download
	def download_MP4(self,yt):
		try:
			stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
			file = stream.download(output_path=self.folder)
			return file
		except:
			IHMError('random')

	@download
	def download_MP3(self,yt):
		try:
			yt = YouTube(self.url) # By creating a Youtube, if the video is unavailable on YouTube raise a videoUnavailable error
			stream = yt.streams.filter(only_audio=True).first()
			file = stream.download(output_path=self.folder)
			pre, ext = os.path.splitext(file)
			os.rename(file,pre + '.mp3')
		except:
			IHMError('random')

	def select_folder(self,ui):
		"""
		:param self.folder: the Folder used for the OutCome
		:type self.folder: str
		:return path_match: true if the folder exists
		:rtype: bool
		"""
		self.folder = QtWidgets.QFileDialog.getExistingDirectory(ui.MainWindow, 'Select Folder')
		if self.verify_folder():
			ui.l_currentFolder.setText(self.folder)

	def verify_folder(self):
		"""
		:param self.folder: the Folder used for the OutCome
		:type self.folder: str
		:return path_match: true if the folder exists
			A messageBox appears if false
		:rtype: bool
		"""
		path_match = os.path.isdir(self.folder)
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
			return False
		return True

	def verify(self):
		fileMP3 = self.folder + "\\" + YouTube(self.url).title + ".mp3"
		fileMP4 = self.folder + "\\" + YouTube(self.url).title + ".mp4"
		b = False
		try:
			if os.path.isfile(fileMP3) or os.path.isfile(fileMP4):
				raise FileExistsError
			else:
				b = True	
		except FileExistsError:
			IHMError("fileExistsError_Error")
		finally:
			return b  == self.verify_link() == self.verify_folder()

           
