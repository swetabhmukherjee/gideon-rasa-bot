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
# webbrowser.open_new_tab('file://' + os.path.realpath(url_business)); message = 'Do you like this template?'

#         return []

from typing import Any, Text, Dict, List
import time
from sys import platform
import webbrowser
import pyautogui
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

url_business = 'startbootstrap-agency-business/index.html'
url_greyscale = 'startbootstrap-grayscale/index.html'
url_project = 'startbootstrap-landing-page/index.html'


class ActionSearchRestaurant(Action):

    def name(self) -> Text:
        return "action_website_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        entities = tracker.latest_message['entities']
        print(entities)
        for e in entities:
        	if e['entity'] == 'type':
        		name = e['value']
     
        	if name == 'business':
        	    webbrowser.open_new_tab('file://' + os.path.realpath(url_business)) #; time.sleep(1); pyautogui.keyDown('cmd','r'); message = 'Do you like this template?' if platform == 'darwin' else webbrowser.open_new_tab('file://' + os.path.realpath(url_business)); time.sleep(1); pyautogui.keyDown('ctrl','r'); message = 'Do you like this template?'
        	if name == 'education':
        		webbrowser.open_new_tab('file://' + os.path.realpath(url_greyscale))#; time.sleep(1); pyautogui.keyDown('cmd','r'); message = 'Do you like this template?' if platform == 'darwin' else webbrowser.open_new_tab('file://' + os.path.realpath(url_greyscale)); time.sleep(1); pyautogui.keyDown('ctrl','r'); message = 'Do you like this template?'
        	if name == 'restaurant':
        		webbrowser.open_new_tab('file://' + os.path.realpath(url_project))#; time.sleep(1); pyautogui.keyDown('cmd','r'); message = 'Do you like this template?' if platform == 'darwin' else webbrowser.open_new_tab('file://' + os.path.realpath(url_project)); time.sleep(1); pyautogui.keyDown('ctrl','r'); message = 'Do you like this template?'
        	
        # dispatcher.utter_message(message)

        return []

class ActionNotLiked(Action):

    def name(self) -> Text:
        return "action_liked_or_not"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      entities = tracker.latest_message['entities']
      print(entities)
      a = ActionSearchRestaurant()
      print(a.name())


      for e in entities:
        if e['entity'] == 'response':
            response = e['value']
            
            if response == 'yes':
                dispatcher.utter_message(text='Awesome! We have stored your preferences. Thanks for using Gideon. This is actions.py response')
            if response == 'no':
                webbrowser.open_new_tab('file://' + os.path.realpath(url_greyscale))
              
class ActionNotLiked2(Action):         

    def name(self) -> Text:
        return "action_liked_or_not_iter2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      entities = tracker.latest_message['entities']
      print(entities)
      a = ActionSearchRestaurant()
      print(a.name())


      for e in entities:
        if e['entity'] == 'response':
            response = e['value']
            
            if response == 'yes':
                dispatcher.utter_message(text='Awesome! We have stored your preferences. Thanks for using Gideon. This is actions.py response')
            if response == 'no':
                webbrowser.open_new_tab('file://' + os.path.realpath(url_project))
              





        # dispatcher.utter_message(text=message)