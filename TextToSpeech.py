import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('voice', voices[2].id)
engine.say('Hello, this is generated with the voice id of two')
engine.runAndWait()


##TODO:
#i've thought about using a test file and use "emotions" to control the complexity of
#speed, tempo and volume
#this will however require some really weird functions to make 
#the voices sound more natural by using the volume funciton