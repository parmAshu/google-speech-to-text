import pyaudio
import wave_handler 
import time
import audioop
import math
import json
import struct
from datetime import datetime


# Recording parameters
# Record in chunks of 1024 samples
chunk = 1024
# 16 bits per sample
sample_format = pyaudio.paInt16  
# number of channels to record from
channels = 1
# Record at 16000 samples per second (optimum for google cloud speech processing)
fs = 16000 
#the listening time for recording
seconds=60

# this function gives the rms silence level
def getSilence(data,sampwidth):
  
  if len(data)<sampwidth:
    print("insufficient length of audio input")
    return -1

  #data is a chunk of audio data with sample width passed as an integer - sampwidth
  num_samples=len(data)/sampwidth

  #if data length has integer number of samples
  if num_samples%1==0.0:
    
    #creating the format string
    format_string="h"*int(num_samples)
    
    #getting the list of integers
    audio_list=struct.unpack(format_string,data)
    
    #determining the rms silence level
    total=0
    for s in audio_list:
      total=total+(s*s)
    total=total/len(audio_list)
    level=int(math.sqrt(total))

    #returning the silence level
    return level
  else:
    print("invalid length of audio bytes")
    return -1

print("Make sure that you have the speech_google_config.txt file in the same directory as this program")
time.sleep(3)
#print("Enter the calibration time")


#calibration function
try:
  # Create an interface to PortAudio
  p = pyaudio.PyAudio()  
 
  #getting the size of sample  
  width=p.get_sample_size(sample_format) 
  
  stream = p.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)

  # Initialize array to store frames
  frames = [] 

  print("recording started")
    
  for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
  
  print("stopped recording")

  # Stop and close the stream  
  stream.stop_stream()
  stream.close()
  # Terminate the PortAudio interface
  p.terminate()

except:
  print("failed")
else:
  #getting the silence level
  _THRESHOLD=getSilence(b''.join(frames),width)
  print("threshold value - {}".format(_THRESHOLD))

  if _THRESHOLD==-1:
    print("failed")
  else:
    fl1=open("speech_google_config.txt",'r')
    content=json.loads(fl1.read())
    fl1.close()
    #setting the threshold value
    content["audio threshold"]=_THRESHOLD
    fl1=open("speech_google_config.txt","w")
    fl1.write(json.dumps(content))
    fl1.close()
    print("done")
