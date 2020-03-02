import os
from datetime import datetime

foldername = datetime.now().strftime("%Y%m%d-%H%M%S")

class Utility():

	def __init__(self):
		self.path = os.path.dirname(os.getcwd()) + '/Logs/'
		self.logpath = self.path+foldername

	def createLogFolder(self):
		
		try:  
				os.mkdir(self.logpath)
				
		except OSError:  
   	 			print("Creation of the directory failed")
		else:  
    			print("Successfully created the directory")