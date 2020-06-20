## website creation straight path
* greet
  - utter_greet
* create_website_request{"request": "website"}
  - utter_website_options
* look_for_website_type
  - action_website_options

## story_business
* greet
    - utter_greet
* create_website_request{"type": "business", "request": "website"}
    - action_website_options
* goodbye
    - utter_goodbye

## story_education
* greet
    - utter_greet
* create_website_request{"type": "education", "request": "website"}
    - action_website_options
* goodbye
    - utter_goodbye

## story_restaurant
* greet
    - utter_greet
* create_website_request{"type": "restaurant", "request": "website"}
    - action_website_options
* goodbye
    - utter_goodbye




<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
 -->
<!-- ## bot challenge
* bot_challenge
  - utter_iamabot
 -->

## interactive_story_1
* greet
    - utter_greet
* create_website_request{"request": "website"}
    - utter_website_options
* goodbye{"type": "business"}
    - action_website_options
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* create_website_request{"request": "website"}
    - utter_website_options
* goodbye{"type": "business"}
    - action_website_options
* goodbye
    - utter_goodbye
* stop
