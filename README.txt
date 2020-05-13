author- Ashutosh Singh Parmar
github ID- parmAshu
email- ashutoshsingh291999@gmail.com
url- https://github.com/parmAshu/google-speech-to-text.git
start date- 10/April/2020 
target - GOOGLE CLOUD PLATFORM SPEECH RECOGNITION API

status- .................................................................................. 
system tested on- unbuntu 16 LTS, Raspbian, Ubuntu 18 LTS (windows and macos tests pending)

project layout-

google-speech-to-text/
|
|___project/
|         |
|         |___linux/ {source code}
|         
|          
|
|___docs/
|      |
|      |___
|
|
|___examples/
|          |
|          |___speechexample.py
|          
|
|___README.txt
|
|___HOW_TO_CONTRIBUTE.txt
|
|__install/
         |
         |___linux/ {installation scripts}
         |
         |___windows/ {under development and testing}
         |
         |___macos/ {under development and testing}


IMPORTANT INFORMATION:

This project contains python3 modules that can be used with your own code to perform speech recognition using GOOGLE CLOUD PLATFORM's 
SPEECH API. The google cloud speech api requires just an api key for authentication. We can generate this api key on the cloud platform after
which we provide it the required permissions on the google cloud platform. Having generated the API key we can copy it into the 'speech_google
_config.txt' file against the 'api key' field.

  PREPARING THE LINUX SYSTEMS:
    1. Having cloned the respository navigate into the install directory.
    2. Now navigate to the linux directory inside the install directory.
    3. You will find two files inside it.
    4. Open a bash terminal on your system.
    5. Provide exeutable priviledges to the install_dependencies.sh script by using the following command:
       $ chmod +x install_dependencies.sh
    6. Now execute install_dependencies.sh script using the following command
       $ ./install_dependencies.sh
    7. If the script shows device offline then, ensure an internet connection before continuind with the step 6 again.
    8. Navigate into the project directory and then your respective os directory in that.
    9. Now, store the speech api key in the accompanying 'speech_google_config.txt' file against the corresponding field.
       (Fore more information on api keys and how to generate and use them, refer to the google cloud platform speech api documentation)
   10. Here run the audioCalibrate.py script by using the following command
       python3 audioCalibrate.py
       (Ensure that the sound levels during the calibration are same as that during normal conditions) 
   11. Now, the system is prepared to run the module with python3.

   

  PREPARING THE WINDOWS SYSTEMS:
  --under development/testing--

  PREPARING THE MAC SYSTEMS:
  --under development/testing--

 
