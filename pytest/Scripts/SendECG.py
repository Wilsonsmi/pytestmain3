import requests, time

class SendECG():

	def sendECGWithFileNaemAndDeviceID(self, fileName, deviceID):
		print("Please wait, sending ECG...")
		i = 0
		while i < 9:
			try:
				file = open(fileName, "rb")
				files = {'ecgFile': file}
				payload = {'deviceId': deviceID, 'timestamp': '1525057958', }
				resp = requests.post('http://cloud-uat2.tricogapps.com/helium/api/1/ecg', data=payload, files=files)
				if resp.status_code == 200 :
					print("Successfully sent ECG file")
					i = 200
				else:
					print("Sending ECG file failed, trying again")
					i+=1
			except requests.ConnectionError:
				print("Sending ECG file failed")
				i+=1
		return i

	def sendScannedECG(self, fileName, patientID):
		print("Please wait, sending ECG...")
		file = open(fileName, "rb")
		files = {'ecgFile': file}
		payload = {'deviceId': deviceID, 'timestamp': '1525057958', }
		resp = requests.post('http://cloud-uat2.tricogapps.com/helium/api/1/ecg', data=payload, files=files)
		print(resp.status_code)
		return resp.status_code
		time.sleep(30)