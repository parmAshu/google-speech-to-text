import sounddevice as sd
import soundfile as sf



#this function will play the audio file
def Play(filename):
  try:
    data,fs=sf.read(filename,dtype='float32')
    sd.play(data,fs)
    sd.wait()
  except:
    return 0
  else:
    return 1
      
     


