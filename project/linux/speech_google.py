#importing the necessary modules 
import http.client
import base64
import json


class speech:

#This function initializes the instance variables like URL of google API server, RESOURCE PATH, HEADERs and API keys 
  def __init__(self,apiKey,language="en-IN"):
    
    self.code=language
    
    #the url to send the audio to
    self._URL="speech.googleapis.com"
    self._RESOURCE="/v1/speech:recognize?key="+apiKey
    self._HEADERS={"Content-Type":"application/json"}


#This function sends the base64 encoded string to the google cloud platform and gets back a list of text elements in it
#The function returns values as follows
  def sendAudio(self,audiodata):
  
    audio_encoded=base64.urlsafe_b64encode(audiodata)
    #audioasbase64 a string containing the base64 encoded audio to be sent to google cloud vision api
    audioasbase64=audio_encoded.decode()
    
    #constructing the request body
    jsonbody={ "audio": { "content": audioasbase64}, "config": { "sampleRateHertz":16000, "languageCode":self.code,"model":"default" } }
    self._BODY=json.dumps(jsonbody) 

    #sending the HTTPS request to the cloud iot core
    try:
      conn=http.client.HTTPSConnection(self._URL)
      conn.request("POST",self._RESOURCE,self._BODY,self._HEADERS)
      res=conn.getresponse()
      #getting the response as string
      res=res.read()
      #converting to string object
      res=res.decode()
      self.Result=res
      #print(res)
    except:
      return 0 

    if res.find("error")>=0:
      #print("error response")
      return 0
    else:
      #if there is no error in the response from cloud then, proceed ahead
      (self.response,self.responseString)=processString(res)
      if self.response==["failed"]:
        #print("process error")
        return 0
      else:
        return self.responseString


#This function processes the returned string to obtain the text elements in the image
#This function returns -1 if the response string is not in the right format
#This function returns the list of text elements in the image if the response string is in the right format
def processString(data):
  try:
    #getting the json data in form of python3 dictionary
    jsonData=json.loads(data)
    string=jsonData["results"][0]["alternatives"][0]["transcript"]
    list_of_strings=string.split(" ")
    return (list_of_strings,string)
  except:
    #the function must always return a tuple of two values because there are two recieving variables on the calling side 
    return (["failed"],"failed")

