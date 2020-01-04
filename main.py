import pyttsx3
from flask import Flask,render_template,request
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os,random
import subprocess, sys

#tts engine sapi5 to take voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)

#app = Flask(__name__)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine.setProperty('voice','english+f1')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

#Some basic queries

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def WishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good morning Boss")
	elif hour>=12 and hour<=18:
		speak("Good After Noon Boss")
	else:
		speak("Good Evening Boss")
	speak("I am Jarvis at your service")

def takeCommand():
	#it will take input from the user and return the string output
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Jarvis is listening please Speak")
		r.pause_threshold = 1
		audio = r.listen(source) 

		try:
			print("Recognization successfull")
			query= r.recognize_google(audio,language='en-in')
			print("User has some query:",query)


		except Exception as e:
				#print(e)
				print("Reenter the query")

	return query


if __name__ == "__main__":
	#speak('Hi I am suman')
	WishMe()
	while True:
		query= takeCommand().lower()
		#writing logic for executing query
		if 'wikipedia' in query:
			speak('Getting into wikipedia')
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query,sentences=3)
			speak("Accroding to Wikipedia")
			print(results)
			speak(results)
		elif 'open google' in query:
			speak("Getting into Google")
			webbrowser.open("google.com")
		elif 'open flipkart' in query:
			speak("Getting into Google")
			webbrowser.open("flipkart.com")
		elif 'open amazon' in query:
			speak("Getting into Google")
			webbrowser.open("amazon.com")

		elif 'play music' in query:
			speak("Searching for music in your device")
			music_dir= "/home/suman/Important/Master_chatbot/music"
			#songs = os.listdir(music_dir)
			songs = random.choice(os.listdir(music_dir))
			print(songs)
			opener ="open" if sys.platform == "darwin" else "xdg-open" 
			subprocess.call([opener, songs])    
			#webbrowser.open(songs[0])
			# os.startfile(os.path.join(music_dir, songs[0]))			

		elif 'open stackoverflow' in query:
			speak("Searching for stackoverflow")
			webbrowser.open("stackoverflow.com")

		elif 'open geeksforgeeks' in query:
			speak("Searching for geeksforgeeks")
			webbrowser.open("geeksforgeeks.com")

		elif 'open github' in query:
			speak("searching for github")
			webbrowser.open("github.com")

		# elif 'play music' in query:
		# 	music_dir = ''
		# 	webbrowser.open("youtube.com")

		elif 'open youtube' in query:
			speak("searching for youtube")
			webbrowser.open("youtube.com")
		# elif  'weather' in query and 'weather' in cmd5:
		# 	owm = pyowm.OWM('YOUR_API_KEY')
		# 	observation = owm.weather_at_place('Bangalore, IN')
		# 	observation_list = owm.weather_around_coords(12.972442, 77.580643)
		# 	w = observation.get_weather()
		# 	w.get_wind()
		# 	w.get_humidity()
		# 	w.get_temperature('celsius')
		# 	print(w)
		# 	print(w.get_wind())
		# 	print(w.get_humidity())
		# 	print(w.get_temperature('celsius'))
		# 	speak(w.get_wind())
		# 	# engine.runAndWait()
		# 	speak('humidity')
		# 	# engine.runAndWait()
		# 	speak(w.get_humidity())
		# 	# engine.runAndWait()
		# 	speak('temperature')
		# 	# engine.runAndWait()
		# 	speak(w.get_temperature('celsius'))
		# 	# engine.runAndWait()


		elif 'thank you' in query:
			speak("My pleasure")
			exit()
		



	
