import requests
import datetime
import os
import webbrowser
import settings
import time

data = open('yt_auto_update_datetime.config', 'r+')
data_time_config = data.readline()
data.close()
date_time_adjusted = ''
if data_time_config is None:
	os.system('cls')
	print('\x1b[0;37;41m' + 'Error: date setting is missing!' + '\x1b[0m')
	input('Hit enter to exit application')
	exit()
if(data_time_config == 'Last 24 hours'):
	date_time_adjusted = str(datetime.datetime.today())
	if(date_time_adjusted[8:10] != '01'):
		date_time_adjusted = date_time_adjusted[0:8] + str(int(date_time_adjusted[8:10]) - 1) + date_time_adjusted[10:]
if(data_time_config == 'Today'):
	date_time_adjusted = str(datetime.date.today()) + ' 00:00:00.0'
if(data_time_config == 'Last 7 days'):
	date_time_adjusted = str(datetime.datetime.today())
	if(int(date_time_adjusted[8:10]) > 6):
		date_time_adjusted = date_time_adjusted[0:8] + str(int(date_time_adjusted[8:10]) - 7) + date_time_adjusted[10:]
date_time_adjusted = date_time_adjusted.replace(' ', 'T', 1).replace(':', '%3A') + 'Z'
data = open('yt_auto_update.config', 'r+')
list_ids = data.readlines()
os.system('cls')
print('NEW VIDEO UPLOADS!!\n\n---------------------------------------------------------------------------------------------------------------')
print('\007')
json_data_list = []
for elements in list_ids:
	elements = elements.split(' ', 1)[0]
	json_data = requests.get('https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults=' + str(settings.MAXRESULTS)  + '&channelId=' + elements + '&publishedAfter=' + date_time_adjusted + '&key=' + settings.APIKEY).json()
	json_data_list.append(json_data)
	if(json_data['pageInfo']['totalResults'] > 0): 
		print('\x1b[0;30;47m' + json_data['items'][0]['snippet']['channelTitle'] + '\x1b[0m'+ ' UPLOADED NEW VIDEO(S) ' + data_time_config.upper() + ': \n')
		temp_title = []
		for numbz in range (0, len(json_data['items'])):
			temp_title.append(json_data['items'][numbz]['snippet']['title'])
			if(temp_title.count(temp_title[numbz]) < 2):
				print('o    "' + temp_title[numbz] + '"')
		print('\n---------------------------------------------------------------------------------------------------------------\n')
data.close()
title_inp = input('Type the first 10-20 words of a title without the quotation marks to open it in chrome (case sensitive!)\nHit enter to exit the application \n')
if(len(title_inp) < 10):
	print('\x1b[1;37;44m' + 'CYA!' + '\x1b[0m')
	time.sleep(3)
	exit()
if(len(title_inp) > 20):
	title_inp = title_inp[0:20]
vidoe_Id = ''
for json_data in json_data_list:
	if(json_data['pageInfo']['totalResults'] > 0): 
		for numbz in range (0, len(json_data['items'])):
			if(json_data['items'][numbz]['snippet']['title'][0:len(title_inp)] == title_inp):
				vidoe_Id = json_data['items'][numbz]['snippet']['thumbnails']['default']['url'].replace('https://i.ytimg.com/vi/', '').replace('/default.jpg', '')
if(vidoe_Id == ''):
	os.system('cls')
	print('\x1b[0;37;41m' + "Error: the title is either wrong or doesn't exist!" + '\x1b[0m')
	input('Hit enter to exit the application')
	exit()
webbrowser.get(settings.CHROME_PATH).open('https://www.youtube.com/watch?v=' + vidoe_Id)
os.system('cls')
print('\x1b[1;37;44m' + 'HAVE FUN, CYA!' + '\x1b[0m')
time.sleep(10)
