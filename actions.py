# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_website_options"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#     	entities = tracker.latest_message['entities']
#       	print(entities)
#         message = ''


#         for e in entities:
#         	if e['entity'] == 'type':
#         		name = e['value']
     
#         	if name == 'business':
#         		message = 'I will help you to create a Business Website'
#         	if name == 'education':
#         		message = 'I will help you to create an Education Website'
#         	if name == 'restaurant':
#         		message = 'I will help you to create a Restaurant Website'
        	
#         dispatcher.utter_message(text=message)


#         return []
from typing import Any, Text, Dict, List
import webbrowser
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSearchRestaurant(Action):

    def name(self) -> Text:
        return "action_website_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)
        message = ''
        url_business = 'startbootstrap-agency-business/index.html'
        url_greyscale = 'startbootstrap-grayscale/index.html'
        url_project = 'startbootstrap-landing-page/index.html'
        # url = 'http://greyhathackers.ga'
        for e in entities:
        	if e['entity'] == 'type':
        		name = e['value']
     
        	if name == 'business':
        	    webbrowser.open('file://' + os.path.realpath(url_business)); message = 'Do you like this template?'
        	if name == 'education':
        		webbrowser.open('file://' + os.path.realpath(url_greyscale)); message = 'Do you like this template?'
        	if name == 'restaurant':
        		webbrowser.open('file://' + os.path.realpath(url_project)); message = 'Do you like this template?'
        	
        dispatcher.utter_message(message)




        return []
