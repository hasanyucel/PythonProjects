from gtts import gTTS
#from playsound import playsound

ses = 'ses.mp3'
dil = 'tr'

txt = gTTS(text='Selam Batuhan',lang=dil,slow=False)

txt.save(ses)
#playsound(ses)