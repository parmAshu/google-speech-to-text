import pyaudio
import wave_handler
from audio_player import *
import speech_google
import time
import audioop
import math
import json
import struct
import os
from datetime import datetime

fl=open("speech_google_config.txt","r")
content=json.loads(fl.read())
_THRESHOLD=content["audio threshold"]
_KEY=content["api key"]
languages=content["languages"]
fl.close()

# Recording parameters
# Record in chunks of 1024 samples
chunk = 1024
# 16 bits per sample
sample_format = pyaudio.paInt16  
# number of channels to record from
channels = 1
# Record at 16000 samples per second (optimum for google cloud speech processing)
Framerate = 16000 


#this function listens to voice, sends it to the server and gets back the text
#the program will hear for a minimum of 10 seconds
#each extension is of 5 senconds 
def getSpeech(language="english",seconds=10,extension=5):
  try:
    Play(os.getcwd()+"/sounds/pop.wav")

    # Create an interface to PortAudio

    p = pyaudio.PyAudio()  
 
    #getting the size of sample  
    width=p.get_sample_size(sample_format) 
  
    stream = p.open(format=sample_format,channels=channels,rate=Framerate,frames_per_buffer=chunk,input=True)

    # Initialize array to store frames
    frames = [] 

    #recording for the minimum time
    for i in range(0, int(Framerate / chunk * seconds)):
      data = stream.read(chunk)
      frames.append(data)

    count=0
    while count<=extension:
      _frames=[]
      #check for silence for 4 seconds 
      for i in range(0, int(Framerate / chunk * 4)):
        data = stream.read(chunk)
        _frames.append(data)

      if isSilence(b''.join(_frames),width):
        break
      else:
        # if the frames where not silent then add those to the main list of audio frames
        frames=frames+_frames
        count=count+1
      
    #print("recording time is {}".format(seconds+count*4))
    Play(os.getcwd()+"/sounds/ting.wav")

    # Stop and close the stream  
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
   
  except:
    return 0
  else:
    # Save the recorded audio in WAV format
    wd = wave_handler.Wave_write(channels,width,Framerate)
    waveaudio=wd.writeframes(b''.join(frames))

  
    if language in languages.keys():
      code=languages[language]

    #send the saved wave audio to google cloud server for speech recognition
    voice=speech_google.speech(_KEY,code)
    speech_text=voice.sendAudio(waveaudio)

    if type(speech_text) is not int:
      return speech_text
    else:
      return 0
  


# this function checks whether the recorded audio is silent or not
def isSilence(data,sampwidth):

  if len(data)<sampwidth:
    return -1

  #data is a chunk of audio data with sample width passed as an integer - sampwidth
  num_samples=len(data)/sampwidth

  #if data length has integer number of samples
  if num_samples%1==0.0:
  
    #creating the format string
    format_string="h"*int(num_samples)

    #getting the list of integers
    audio_list=struct.unpack(format_string,data)
    
    total=0
    for s in audio_list:
      total=total+(s*s)
    total=total/len(audio_list)
    level=int(math.sqrt(total))

    if level>_THRESHOLD:
      return 0
    else:
      return 1

  else:
    return -1
