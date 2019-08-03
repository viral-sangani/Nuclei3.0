import pyttsx3



from selenium import webdriver
import wikipediaapi
import urllib.request
import json
import speech_recognition as sr
import sys
import os
import subprocess
from pygame import mixer
import random

def voice_input():
	inputtext = ''	
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("  Say something! : ")
	    audio = r.listen(source)

	try:
	 	inputtext = r.recognize_google(audio)
	except sr.UnknownValueError:
	    print("Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return inputtext


class Text_to_speech():
	def speak(final_string):
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		for voice in voices:
			if voice.languages[0] == b'\x05hi':
				engine.setProperty('voice', voice.id)
				break
		engine.say(final_string)
		engine.runAndWait()

class wiki(Text_to_speech):
	
	def wiki_find(self,text):
		string = ''
		words = text.split()
		for word in words:
			i = 0
			if words[i]=="search" or words[i]=="find":
				for x in range(i+1,len(text.split())):
					i += 1
					string = string + " " + words[i]
					if words[i] == "in":	
						break
					else:
						pass
			break
		final_string = string.rstrip('in').strip()
		try:	
			wikipedia = wikipediaapi.Wikipedia("en")
			page = wikipedia.page(final_string)
			print(page.summary)
			Text_to_speech.speak(page.summary)

		except:
			print("Sorry something went wrong, please try to search something else...")

	def wiki_broswer_open(self,text):
		i = 0
		string = ''
		words = []
		words = text.split()
		print("\t\t\tWait While I Open Browser.")
		Text_to_speech.speak("Wait While I Open Browser.")
		for word in words:
			if words[i]=="open":
				for x in range(i+1,len(text.split())):
					i += 1
					string = string + " " + words[i]
					if words[i] == "in":	
						break
					else:
						pass
				break
			i += 1

		final_string = string.rstrip('in').strip()
		try:	
			wiki = wikipediaapi.Wikipedia("en")
			page = wiki.page(final_string)
			url = page.fullurl
			browser = webdriver.Firefox()
			browser.get(url)		
		except:
			print("Sorry something went wrong, please try to search something else...")

class Google(Text_to_speech):
	
	def google_map_distance(self,text):
		i = 0
		words = []
		origin = ''
		destination = ''
		words = text.split()
		print("\t\t\t\tPlease wait")
		Text_to_speech.speak("Please wait...")
		for word in words:
			if words[i]=="between":
				for x in range(i+1,len(text.split())):
					i += 1
					origin = origin + " " + words[i]
					if words[i] == "and":	
						break
					else:
						pass
				break
			i += 1
		final_origin = 	origin.rstrip("and").strip()

		for word in words:
			if words[i]=="and":
				for x in range(i+1,len(text.split())):
					i += 1
					destination = destination + " " + words[i]
				break
			i += 1
		final_destination = destination.strip()

		endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
		final_origin = final_origin.replace(' ','+')
		final_destination = final_destination.replace(' ','+')
		api_key = 'AIzaSyDMi6tpqRCscJ48MS-5hXjCRNrXGUnyGZ4'
		nav_request = 'origin={}&destination={}&key={}'.format(final_origin,final_destination,api_key)
		url = endpoint + nav_request

		try:	
			response = urllib.request.urlopen(url).read()
			directions = json.loads(response)
			routes = directions['routes']
			legs = routes[0]['legs']
			final_distance = legs[0]['distance']['text']
			speak0 = 'Distance of Your Travel is= {}'.format(final_distance)
			print(speak0)
			Text_to_speech.speak(speak0)

		except:
			print("something went wrong, try again with something else..")

	def google_search(self,text):
		i = 0
		words = []
		words = text.split()
		for word in words:
			if "what" in words or "how" in words or "when" in words:
				print("\t\t\tWait While I Google it.")
				Text_to_speech.speak("Wait While I Google it.")
				browser = webdriver.Firefox()
				formatted_phrase = text.replace(" ","+")
				browser.get("https://www.google.co.in/search?q={}".format(formatted_phrase))
				break

			elif  "want to know about" in text:
				if words[i]=="about":
					for x in range(i+1,len(text.split())):
						i += 1
						string = string + " " + words[i]
						break
				i += 1
				break
				final_string = string.rstrip('in').strip()
				print("\t\t\tWait While I Google it.")
				Text_to_speech.speak("Wait While I Google it.")
				browser = webdriver.Firefox()
				formatted_phrase = final_string.replace(" ","+")
				browser.get("https://www.google.co.in/search?q={}".format(formatted_phrase))

	def all_search(self,text):
		print("\t\t\tWait While I Google it.")
		Text_to_speech.speak("Wait While I Google it.")
		browser = webdriver.Firefox()
		browser.get("https://www.google.co.in/search?q={}".format(text))

def mail():
	Text_to_speech.speak("Opening Gmail..")
	browser = webdriver.Firefox()
	browser.get("https://mail.google.com/mail/u/0/#inbox")

def amazon_page(text):
	i = 0
	string = ''
	words = []
	words = text.split()
	print("\t\t\tWait While I Open Firefox Browser.")
	Text_to_speech.speak("Wait While I Open Firefox Browser.")
	for word in words:
		if "for" in words:
			if words[i]=="for":
				for x in range(i+1,len(text.split())):
					i += 1
					string = string + " " + words[i]
					if words[i] == "in":	
						break
					else:
						pass
				break
			i += 1

		elif "search" in words:
			if words[i]=="search":
				for x in range(i+1,len(text.split())):
					i += 1
					string = string + " " + words[i]
					if words[i] == "in":	
						break
					else:
						pass
				break
			i += 1
		else:
			print("try saying \"search for (product_name) in amazon\"")


	final_string = string.rstrip('in').strip()

	browser = webdriver.Firefox()
	formatted_phrase = final_string.replace(" ","+")
	browser.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}".format(formatted_phrase))


def pass_gen():

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	pw_length = input("Enter Password Length You Need : ")
	pw_length = int(pw_length)
	mypw = ""

	for i in range(pw_length):
	    next_index = random.randrange(len(alphabet))
	    mypw = mypw + alphabet[next_index]

	for i in range(random.randrange(1,3)):
	    replace_index = random.randrange(len(mypw)//2)
	    mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index+1:]

	for i in range(random.randrange(1,3)):
	    replace_index = random.randrange(len(mypw)//2,len(mypw))
	    mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]

	print(mypw)

def sps():
	ROCK, PAPER, SCISSORS = 1, 2, 3
	names = 'ROCK', 'PAPER', 'SCISSORS'

	def beats(a, b):
	    if (a,b) in ((ROCK, PAPER), (PAPER, SCISSORS), (SCISSORS, ROCK)): 
	        return False

	    return True
	print ("Please select: ")
	Text_to_speech.speak("Please select")
	print ("1 - Rock" )
	print ("2 - Paper" )
	print ("3 - Scissors" )

	player = int(input ("Choose from 1-3: "))
	cpu = random.choice((ROCK, PAPER, SCISSORS))
	print()
	if cpu != player:
		if beats(player, cpu):
			print ("You Won")
			Text_to_speech.speak("You won")
		else:
			print ("CPU Won")
			Text_to_speech.speak("CPU won")
	else:
		print ("Its A Tie....!")
		Text_to_speech.speak("Its A Tie")
	print()
	print ("YOU Choose ->",names[player-1])
	print("CPU Choose ->",names[cpu-1])
	
def youtube_search(text):
	url = "https://www.youtube.com/results?search_query="
	i = 0
	string = ''
	words = []
	words = text.split()
	print("\t\t\tOpening Youtube")
	Text_to_speech.speak("Opening Youtube")
	for word in words:
		if words[i]=="search":
			for x in range(i+1,len(text.split())):
				i += 1
				string = string + " " + words[i]
				if words[i] == "in":	
					break
				else:
					pass
			break
		i += 1

	final_string = string.rstrip('in').strip().replace(" ","+")
	try:	
		browser = webdriver.Firefox()
		browser.get(url+final_string)		
	except:
		print("Sorry something went wrong, please try to search something else...")

def facebook_search(text):
	url = "https://www.facebook.com/search/top/?q="
	i = 0
	string = ''
	words = []
	words = text.split()
	print("\t\t\tOpening Facebook")
	Text_to_speech.speak("Opening Facebook")
	for word in words:
		if words[i]=="search":
			for x in range(i+1,len(text.split())):
				i += 1
				string = string + " " + words[i]
				if words[i] == "in":	
					break
				else:
					pass
			break
		i += 1

	final_string = string.rstrip('in').strip().replace(" ","+")
	try:	
		browser = webdriver.Firefox()
		browser.get(url+final_string)		
	except:
		print("Sorry something went wrong, please try to search something else...")

def search(text):
	if "wikipedia" in text:
		w = wiki()
		w.wiki_find(text)

	elif "wikipedia" in text:
		if "open" in text:
			w = wiki()
			w.wiki_broswer_open(text)

	elif "distance" in text:
		if "between" in text:
			google = Google()
			google.google_map_distance(text)

	elif "today" in text and "date" in text:
		os.system('date')
		

	elif "list directories" in text or "show me content of current folder " in text:
		subprocess.call('ls')
	
	elif "play some music" in text:
		subprocess.Popen(['mpg123', '-q','/home/viral/Downloads/[Waploaded]_Taylor_Swift_-_Gorgeous-1517646242.mp3']).wait()

	elif "amazon" in text or "Amazon" in text:
		amazon_page(text)

	elif "what is " in text or "how " in text or "when" in text or "want to know" in text:
		google = Google()
		google.google_search(text)

	elif "email" in text or "mail" in text:
		mail()

	elif "facebook" in text:
		if "search" in text:
			facebook_search(text)

	elif "facebook" in text or "Facebook" in text:
		Text_to_speech.speak("Opening Facebook")
		browser = webdriver.Firefox()
		browser.get("https://www.facebook.com/")

	elif "youtube" in text:
		if "search" in text:
			youtube_search(text)

	elif "youtube" in text:
		Text_to_speech.speak("Opening youtube")
		browser = webdriver.Firefox()
		browser.get("https://www.youtube.com/")

	elif "roll a dice" in text:
		min = 1
		max = 6

		roll_again = "yes"

		while roll_again == "yes" or roll_again == "y":
		    print("Rolling the dices...")
		    Text_to_speech.speak("Rolling the dices")
		    print(random.randint(min, max))
		    break

	elif "generate password" in text or  "generate a password" in text:
		pass_gen()

	elif "getting bored" in text or "bored" in text:
		sps()

	else:
		print("Sorry I did't recognise it\ndo you want me to google it?(Y/N)")
		Text_to_speech.speak("Sorry I did't recognise it")
		Text_to_speech.speak("do you want me to google it?")
		ans = input()
		if ans=="Y" or ans=="y":
			google = Google()
			google.all_search(text)


def main():
	try:	
		a = 0
		while True:
			text = input("\nPlease Enter Your Question...")

			if "speech recognition" in text or "speak" in text:
				while a == 0:	
					
					ans = input("Do You want to continue..? (Y/N)")
					if ans == 'Y' or ans == 'y':
						speech = voice_input()
						if "exit" in speech and "speech recognition" in speech:
							print(speech)
							break

						elif "exit" in speech:
							print(speech)
							sys.exit()

						else:
							print(speech)	
							search(speech)

					elif ans == "N" or ans == "n":
						break		
			
			else:
				if 'exit' in text:
					sys.exit()
				else:
					while a == 0:
						search(text)
						break

	except KeyboardInterrupt:
		print("\nExiting.....\n")
		sys.exit()
main()

