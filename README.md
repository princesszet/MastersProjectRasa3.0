# Software Engineering Masters Project
For my Masters project I aim to explore how people interact with social robots based on their appearance and behaviour. 
I compare two robots, Pepper and Furhat. NLU is handled by RASA. This version works with RASA 3.

**Running instructions**

To run RASA Open Source, make sure you follow the instructions to install RASA on your machine (https://rasa.com/docs/rasa/installation/).
In the IDE of your choice (I recommend PyCharm) open three terminals. 

In one of them, run **rasa run**

In the secon one, run **rasa run actions**

Once the server is running, run in the third one **ngrok http 5005**

If you don't have ngrok installed, follow the instructions: https://ngrok.com/download
