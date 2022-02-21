import random
from typing import Any, Text, Dict, List

import time
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class GetJokesFromAPI(Action):
    def name(self) -> Text:
        return "action_tell_a_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = {'Accept': 'application/json'}
        joke = requests.get("https://icanhazdadjoke.com/", headers=headers).json().get("joke")
        dispatcher.utter_message(text=joke + "... Hmm, that's the best I can think about! Did you find this funny?")

        return []

class GetNumberFactsFromAPI(Action):
    def name(self) -> Text:
        return "action_tell_a_fact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = {'Accept': 'application/json'}
        fact = requests.get("http://numbersapi.com/random/trivia?json", headers=headers).json().get("text")
        dispatcher.utter_message(text="Ok! Let's see what I can think about... Oh, this one is cool... " + fact +
                                 " I find it fascinating, I like remembering random facts... So, how is your day?")

        return []

class GetWeatherFromAPI(Action):
    def name(self) -> Text:
        return "action_tell_the_weather_ask_what_do_you_study"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = {'Accept': 'application/json'}
        weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=55.86&lon=4.25&exclude=current,"
                               "minutely,hourly,alert&units=metric&appid=3fad370ca36820a3b8f1c3794a75c4ce",
                               headers=headers).json()

        day_temp = weather.get("daily")[0].get("temp").get("day")
        night_temp = weather.get("daily")[0].get("temp").get("night")
        max_temp = weather.get("daily")[0].get("temp").get("max")
        min_temp = weather.get("daily")[0].get("temp").get("min")
        dispatcher.utter_message(text="Let me check... Ok, I got it! Tomorrow in Glasgow it will be " + str(day_temp) +
                                 " degrees Celsius during the day, and " + str(night_temp) + " during the night. The "
                                 "minimum temperature will be " + str(min_temp) + " and the  maximum one " +
                                 str(max_temp) + " degrees. I hope that's helpful! Anyway, what do you study?")

        return []

class ReactToTheCountryFrom(Action):
    def name(self) -> Text:
        return "action_confirm_the_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot("country")
        dispatcher.utter_message(text="I think you said that you're from " + country + ", is that correct?")

        return []

class TellRandomHistoricalFact(Action):
    def name(self) -> Text:
        return "action_tell_random_historical_fact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        random_facts = ["The Mayans were worshipping turkeys as gods.", "The fine arts used to be included in the "
                        "Olympics due to the ancient tradition.", "Napoleon Bonaparte was once attacked by 3000 bunnies.",
                        "Before 1908, women were banned from smoking in public in New York.", "Cleopatra was not actually "
                        "born in Egypt. She was from Greece.", "Ketchup used to be sold as medicine.", "The light bulb "
                        "was not actually invented by Thomas Edison. It was Warren de la Rue who first came up with this "
                        "idea."]

        fact = random.choice(random_facts)
        dispatcher.utter_message(text="Here's might be something you don't know yet: " + fact + " History is not something"
                                 "I'm personally very passionate about, but I can rememeber as many random things as my "
                                 "memory size allows! What do you like doing in your free time?")

        return []

class DifferentReactionsToMisunderstanding(Action):
    def name(self) -> Text:
        return "action_different_reactions_to_misunderstanding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        random_reactions = ["Oh no, I'm sorry for misunderstanding you! Could you please repeat?", "I'm sorry for not"
                            "understanding what you said. Could you repeat it?", "Oh, I see! Could you please say it "
                            "again?", "Sorry for that! Can you please repeat what you said?", "Ups, sorry I "
                            "misunderstood! Could you please repeat?", "Ahh I'm sorry for mishearing you - please "
                            "repeat it!"]

        reaction = random.choice(random_reactions)
        dispatcher.utter_message(text=reaction)

        return []

class AskTheUserToRephrase(Action):
    def name(self) -> Text:
        return "action_ask_the_user_to_rephrase"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        random_requests = ["I'm sorry, I didn't quite understand that. Could you rephrase?", "I'm sorry, I'm not sure "
                           "if I understood you. Could you please repeat that?", "Sorry, I didn't catch that! Could you "
                           "please say it again?", "Could you rephrase? I didn't catch what you said!", "Could you "
                           "repeat what you said? I'm afraid I didn't understand you!"]

        request = random.choice(random_requests)
        dispatcher.utter_message(text=request)

        return []

class ReactToColourAskAboutInstruments(Action):
    def name(self) -> Text:
        return "action_react_to_colour_ask_about_instruments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        colour = tracker.get_slot("colour")
        print(colour)

        if colour == "blue":
            text = "Good choice, blue is the most common favourite colour in the world... And, do you play any " \
                   "instruments?"
        elif colour == "black":
            text = "Cool, wearing black makes a person appear more powerful... And, do you play any instruments?"
        elif colour == "orange":
            text = "Interesting, the word 'orange' was first used to describe a fruit, then the colour was named after " \
                   "it... And, do you play any instruments?"
        elif colour == "green":
            text = "Good choice, green is considered the colour of peace... And, do you play any instruments?"
        elif colour == "red":
            text = "Cool, red is actually the first colour a baby sees... And, do you play any instruments?"
        elif colour == "brown":
            text = "Interesting, brown is one of the most commonly used colours in art... And, do you play any " \
                   "instruments?"
        elif colour == "white":
            text = "Good choice, white is an achromatic colour as it lacks hue... And, do you play any instruments?"
        elif colour == "purple":
            text = "Cool, purple is beautiful, but some people are scared of it which is called porphyrophobia... And, " \
                   "do you play any instruments?"
        elif colour == "yellow":
            text = "Interesting, yellow is considered a lucky colour in China... And, do you play any instruments?"
        elif colour == "pink":
            text = "Good choice, pink is proved to have a calming effect... And, do you play any instruments?"
        elif colour == "grey":
            text = "Cool, grey is considered a neutral, calming colour... And, do you play any instruments?"
        else:
            text = "That is a beautiful colour, good choice! And, do you play any instruments?"

        dispatcher.utter_message(text=text)

        return []