# this code only works on Ubuntu 14.04
from naoqi import ALProxy
import json
# from json import JSONDecodeError
import requests
import time

def main():
    # pepper = "192.168.8.162"
    pepper = "pepper.local"
    tts = ALProxy("ALTextToSpeech", pepper, 9559)

    # this variable has to be changed every time you run ngrok
    ngrok = "617e-130-209-157-51"
    url_receive = "http://" + ngrok + ".ngrok.io/webhooks/pepper_robot/webhook"
    url_health = "http://" + ngrok + ".ngrok.io"

    tts.say("My name is Pepper, and I'm a social robot. Hi there!")

    # asr stands for automatic speech recognition
    asr = ALProxy("ALSpeechRecognition", pepper, 9559)
    asr.pause(True)
    asr.setLanguage("English")
    vocabulary = ["hey", "hello", "hi", "hiya", "hello there", "good morning", "good evening", "hey there",
    "let's go", "hey dude", "good afternoon", "how are you", "and you", "I'm good, how are you",
    "good, thank you, how are you", "not bad, how are you doing", "I'm ok, and you", "how's your day",
    "I'm great and how are you", "I'm good, how about you?", "I'm sad, how about you",
    "not good, and how is your day", "bad, how are you", "thanks for asking, I'm good, and how are you",
    "cu", "good by", "see you later", "good night", "bye", "goodbye", "have a nice day", "see you around",
    "bye bye", "who are you", "what are you", "what is your purpose", "what's your name", "what is your goal",
    "what are you trying to accomplish", "are you human", "are you a robot", "are you real", "yes",
    "yes, please", "yup", "I said yes", "I do", "I am", "Yeah I do", "indeed", "of course", "that sounds good",
    "correct", "yeah", "sure", "ok", "okay", "it is", "I do", "it does", "I did", "no", "I said no", "I don't",
    "I do not", "I'm not", "no, I'm not", "nope", "no thanks", "never", "nah", "not really", "it isn't",
    "it is not", "I don't", "it doesn't", "I didn't", "perfect", "great", "amazing", "I'm ok", "I'm fine",
    "nice to meet you too", "you too", "wonderful", "I am feeling very good", "I am great", "I am amazing",
    "so good", "so perfect", "my day was horrible", "I am sad", "I don't feel very well", "I'm dissapointed",
    "super sad", "I'm so sad", "sad", "very sad", "unhappy", "not good", "not very good", "extremely sad",
    "so sad", "I'm bored", "I don't even know", "I don't have energy", "I'm feeling mellow",
    "boredom is killing me", "I have nothing to do", "I'm not doing anything", "I'm feeling weary", "so bored",
    "I want some entertainment", "are you a bot", "are you a human", "am I talking to a bot",
    "am I talkig to a human", "what is your purpose", "who designed you", "who is your creator", "who are you",
    "what do you do", "when were you created", "what is your goal", "what do you want",
    "what do you want to know", "it was good", "my day was good", "was ok", "it was great", "my day was good",
    "my day isn't bad, thanks", "yeah it's ok, thanks", "it is bad", "my day is not good", "my day wasn't good",
    "is not ok", "it is awful", "my day was awful", "my day was bad, unfortunately", "I study literature",
    "I study computer science", "I study politics", "I do economics", "I do maths", "I do anthropology",
    "computing science", "computer science", "software engineering", "engineering", "medicine", "arts",
    "literature", "maths", "physics", "law", "history", "language", "politics", "psychology", "economics",
    "social sciences", "journalism", "education", "United Kingdom", "I'm from United Kingdom", "I'm from Scotland",
    "I'm from Greece", "I am from Egypt", "I am from Poland", "from the States", "from France", "Scotland",
    "England", "the UK", "United Kingdom", "Europe", "Asia", "China", "the States", "United States", "Poland",
    "France", "Germany", "Italy", "Greece", "Romania", "Bulgaria", "Egypt", "Spain", "it's nice", "it's ok",
    "I don't mind", "I like the culture", "it's my home", "I like it", "very good", "I love it", "great",
    "amazing", "it's not bad", "I guess it's ok", "it's a great place", "I don't like it",
    "it does not appeal to me", "it's not a good place", "it's not a nice location", "I hate it",
    "it's not the best country", "I don't like it at all", "it's very unpleasant", "that's not what I meant",
    "I meant something different", "you misunderstood me", "you misheard me", "that was not my intention",
    "that's not what I was implying", "you misread what I was saying", "you mistook my meaning",
    "I had a different meaning in mind", "can I repeat what I said", "let me repeat", "that's not what I said",
    "pizza", "my favourite food is pizza", "spaghetti", "burgers", "my favourite food is a burger", "salad",
    "soup", "my favourite food is a soup", "cookies", "cake", "meatballs", "I like meatballs the most", "curry",
    "curry is my favourite food", "burrito", "tacos", "mac and cheese", "sushi", "I like sushi the most", "ramen",
    "skiing", "cooking", "reading", "music", "movies", "sport", "gym", "writing", "singing", "dancing", "hiking",
    "bouldering", "to dance", "to read", "I think the guitar", "I think the electgric guitar",
    "I would play the piano", "I would play the saxophone", "I always wanted to learn how to play the violin",
    "I always wanted to learn how to play the piano", "I guess the drums", "guitar", "piano", "violin",
    "electric guitar", "drums", "flute", "bass", "saxophone", "cello", "clarinet", "thank you", "thanks", "cheers",
    "sincerely grateful", "I appreciate that", "you really helped me", "thank you for this", "I'm grateful",
    "I'm not sure what to say", "I don't know what to say", "what should I say", "I'm at a loss for words",
    "I'm stumped", "I don't have the right words", "I don't know the answer", "I don't know how to answer",
    "I don't know", "I'm not sure", "I don't know how to answer this", "I'm clueless", "don't know, sorry",
    "I'm not certain", "nice to meet you too", "it was great to meet you", "it was great talking to you",
    "I enjoyed our conversation", "I enjoyed talking to you", "I liked getting to know you", "thanks for the chat",
    "rock", "rock music", "jazz", "hip hop", "hip hop is great", "pop", "pop music", "heavy metal", "metal", "folk",
    "folk music", "blues", "country", "electronic", "dance", "I like rock", "I like dance", "I like rock music",
    "I like hip hop", "I think electronic music is my favourite", "I think pop music is my favourite",
    "probably hip hop", "I think pop", "I prefer eating out", "I prefer ordering food", "ordering food",
    "ordering food is my choice", "eating out is the best", "eating out", "I like going to restaurants",
    "I like eating at home", "I don't usually order food", "I don't enjoy ordering food", "the city",
    "I prefer living in a city", "city", "I like living in a city", "city is my first choice",
    "living in a city is the best", "I would never move out of a city", "this city is the best", "I prefer cities",
    "I like big cities", "I think in a city", "a city", "the countryside", "countryside",
    "I prefer living in the countryside", "I like living in the countryside", "countryside is my favourite",
    "countryside is my first choice", "living in the countryside is the best",
    "I would never move out of the countryside", "the countryside is the best", "I prefer the countryside",
    "I like the countryside", "I think in the countryside", "a countryside", "I prefer board games",
    "I like board games", "board games", "board games are my favourite", "I like playing board games the most",
    "my preference is playing board games", "I prefer to play board games", "I enjoy playing board games",
    "I prefer video games", "I like video games", "video games", "video games are my favourite",
    "I like playing video games the most", "my preference is playing video games", "I prefer to play video games",
    "I enjoy playing video games", "clue", "monoploy", "scrabble", "battleship", "risk", "exploding kittens",
    "stratego", "I like scrabble the most", "exploding kittens is my favourite game", "my favourite game is catan",
    "jenga", "jenga is my favourite", "catan", "minecraft", "gta", "fortnite", "the legend of zelda", "the witcher",
    "call of duty", "the last of us", "world of warcraft", "wii", "animal crossing", "star wars", "overwatch",
    "counter strike", "blue", "black", "red", "white", "purple", "green", "yellow", "orange", "pink", "grey",
    "grey is my favourite colour", "my favourite colour is blue", "I think purple", "I think green",
    "probably yellow colour", "probably red", "I think green is my favourite colour", "I prefer black",
    "I prefer orange colour", "I like brown", "I like orange colour", "why not", "go ahead", "my name is", "I'm",
    "I am", "my name's", "it was bad", "my name is Aidan", "I'm Marios", "my name's Juli", "yeah, sure", "Glasgow",
    "Scotland", "here"]

    asr.setVocabulary(vocabulary, False)
    pepper_response = ""
    while pepper_response != "Bye":
        pepper_response = dialogue(pepper, url_receive, asr, tts)

def dialogue(pepper, url_receive, asr, tts):

    asr.subscribe("Test_ASR")
    memProxy = ALProxy("ALMemory", pepper, 9559)
    memProxy.subscribeToEvent("WordRecognized", pepper, "wordRecognized")
    asr.pause(False)
    time.sleep(5)
    asr.unsubscribe("Test_ASR")

    data = []
    data = memProxy.getData("WordRecognized")
    answer = data[0]
    print(answer)

    if answer == "":
        tts.say("I don't think you said anything. Could you please repeat?")
        answer = asr.subscribe("Test_ASR")
        asr.pause(False)
        time.sleep(5)
        asr.unsubscribe("Test_ASR")
        if answer == "":
            tts.say("I still can't hear you, I'm sorry. Maybe we could talk another day!")
            sys.exit("User didn't say anything to Pepper.")

    data = {"sender": "pepper", "message": answer}
    post = requests.post(url_receive, data=json.dumps(data), verify=False)
    try:
        response = post.json()[0].get("text")
    except KeyError:
        response = "I don't understand what you said. Could you please repeat?"
    # except JSONDecodeError:
    #     response = "I'm not sure if I understood you - could you please repeat?"

    str_response = str(response)
    tts.say(str_response)
    return response

if __name__ == "__main__":
    main()