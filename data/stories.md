## website creation straight path yes
* greet
  - utter_greet
* create_website_request{"request": "website"}
  - utter_website_options
* look_for_website_type
  - action_website_options
  - utter_do_you_like
* ask_if_liked{"response": "yes"}
  - action_liked_or_not
* goodbye
  - utter_goodbye

## website creation straight path no one iter
* greet
  - utter_greet
* create_website_request{"request": "website"}
  - utter_website_options
* look_for_website_type
  - action_website_options
  - utter_do_you_like
* ask_if_liked{"response": "no"}
  - action_liked_or_not
  - utter_do_you_like
* ask_if_liked{"response": "yes"}
  - action_liked_or_not
* goodbye
  - utter_goodbye

<!-- ## website creation straight path no two iter
* greet
  - utter_greet
* create_website_request{"request": "website"}
  - utter_website_options
* look_for_website_type
  - action_website_options
  - utter_do_you_like
* ask_if_liked{"response": "no"}
  - action_liked_or_not
  - utter_do_you_like
* ask_if_liked{"response": "no"}
  - action_liked_or_not_iter2
  - utter_do_you_like
* ask_if_liked{"response": "yes"}
  - action_liked_or_not
* goodbye
  - utter_goodbye
 -->

## New Story

* greet
    - utter_greet
* create_website_request{"request":"website"}
    - utter_website_options
* create_website_request{"type":"business"}
    - action_website_options
    - utter_do_you_like
* ask_if_liked{"response":"yes"}
    - action_liked_or_not
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* create_website_request{"request":"website"}
    - utter_website_options
* create_website_request{"type":"education"}
    - action_website_options
    - utter_do_you_like
* ask_if_liked{"response":"yes"}
    - action_liked_or_not
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* create_website_request{"request":"website"}
    - utter_website_options
* create_website_request{"type":"restaurant"}
    - action_website_options
    - utter_do_you_like
* ask_if_liked{"response":"yes"}
    - action_liked_or_not
* goodbye
    - utter_goodbye
