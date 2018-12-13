import requests
import time
import os
import webbrowser
import settings

choice = '0'
os.system('cls')
while (choice != '4'):
	choice = input('Exit application = 0\nAdd channel = 1\nRemove channel = 2\nChange date:time settings = 3\nCheck daily video uploads = 4\n').rstrip() 
	if(choice == '0'):
		exit()
	if(choice == '1'):
		subschoice = 1
		while(subschoice != '0'):
			os.system('cls')
			data = open('yt_auto_update.config', 'a+')
			subschoice = input('Please enter "channelID = <ID>", the name of the channel or "0" to exit to the menu\n(e.g. channelID = UC18YhnNvyrG2ATwCyj9p5ag or CrazyRussianHacker)\n').rstrip()
			if(subschoice == '0'):
				pass
			elif(subschoice[0:12] == 'channelID = '):
				try:
					req = requests.get('https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId=' + subschoice[12:]  + '&key=' + settings.APIKEY )
					json_data = req.json()
					data.write(subschoice[12:].rstrip() + ' = ' + json_data['items'][0]['snippet']['channelTitle'])
					data.write('\n')
					print('Succesfuly saved ' + '\x1b[1;37;41m' + json_data['items'][0]['snippet']['channelTitle'] + '\x1b[0m' + ' to the channel list!')
					time.sleep(3)
				except:
					print('\x1b[0;37;41m' + "Error: couldn't find name for ID!" + '\x1b[0m')
					time.sleep(3)
			else:
				try:
					req = requests.get('https://www.googleapis.com/youtube/v3/search?part=id%2Csnippet&q=' + subschoice + '&type=channel&key=' + settings.APIKEY)
					json_data = req.json()
					data.write(json_data['items'][0]['snippet']['channelId'] + ' = ' + subschoice)
					data.write('\n')
					print('Succesfuly added ' + '\x1b[1;37;41m' + subschoice + '\x1b[0m' + ' to the channel list!')
					time.sleep(3)
				except:
					print('\x1b[0;37;41m' + "Error: couldn't find ID for name!" + '\x1b[0m')
					time.sleep(3)
			data.close()
	if(choice == '2'):
		subschoice = 1
		while (subschoice != '0'):
			os.system('cls')
			i = 0
			data = open('yt_auto_update.config', 'r+')
			read_lines = data.readlines()
			os.system('cls')
			for line in read_lines:
				i = i + 1
				if(i < 10):
					print(str(i) + '    '  + line, end='')
				else:
					print(str(i) + '   ' + line, end='')
			data.close()
			if(i == 0):
				print('\x1b[0;37;41m' + 'No channelIds available!' + '\x1b[0m')
				time.sleep(3)	
			else:
				print('\nPlease select the channelId you want to remove or "0" to exit to the menu')
				subschoice = input().rstrip()
				i = 1
				data = open('yt_auto_update.config', 'w+')
				for line in read_lines:
					if(subschoice != str(i)):
						data.write(line)
					i = i + 1
				data.truncate()
				data.close()
	if(choice == '3'):
		subschoice = 1
		os.system('cls')
		print('1    Last 24 hours\n2    Today\n3    Last 7 days\n\nEnter 0 to exit to the menu\n\n')
		print("Please select the date setting you want to use")
		subschoice = input().rstrip()
		if(subschoice == '1'):
			data = open('yt_auto_update_datetime.config', 'w+')
			data.write('Last 24 hours')
			print('Succesfuly saved date setting: ' + '\x1b[1;37;41m' + 'Last 24 hours' + '\x1b[0m' + '!')
			data.close()
			time.sleep(3)
		elif(subschoice == '2'):
			data = open('yt_auto_update_datetime.config', 'w+')
			data.write('Today')
			print('Succesfuly saved date setting: ' + '\x1b[1;37;41m' + 'Today' + '\x1b[0m' + '!')
			data.close()
			time.sleep(3)
		elif(subschoice == '3'):
			data = open('yt_auto_update_datetime.config', 'w+')
			data.write('Last 7 days')
			print('Succesfuly saved date setting: ' + '\x1b[1;37;41m' + 'Last 7 days' + '\x1b[0m' + '!')
			data.close()
			time.sleep(3)
		elif(subschoice == '0'):
			pass
		else:
			print('\x1b[0;37;41m' + 'Error: please select a legitimate option!' + '\x1b[0m')
			time.sleep(3)
	os.system('cls')
os.system((os.path.dirname(os.path.abspath(__file__)) + '/' + 'yt_auto_update2.py').replace("\\", "/"))