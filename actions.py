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

        for e in entities:
        	if e['entity'] == 'type':
        		name = e['value']
     
        	if name == 'business':
        		message = 'I will help you to create a Business Website'
        	if name == 'education':
        		message = 'I will help you to create an Education Website'
        	if name == 'restaurant':
        		message = 'I will help you to create a Restaurant Website'
        	
        dispatcher.utter_message(text=message)




        return []
