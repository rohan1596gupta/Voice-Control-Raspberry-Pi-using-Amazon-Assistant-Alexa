#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:11:28 2019

@author: rohankumar
"""

import boto3
  
# Below you need to add in your access key, access secret, rgion and sqs queue url
  
access_key = 'AWS access key'
access_secret = 'AWS secret key'
region ='eu-west-1'
queue_url = 'https://sqs.eu-west-1.amazonaws.com/917185725508/RPiQueue002'
  
# you should not need to change the following unless you know what your doing.
  
def build_speechlet_response(title, output, reprompt_text, should_end_session):
   return {
       'outputSpeech': {
           'type': 'PlainText',
           'text': output
       },
       'card': {
           'type': 'Simple',
           'title': "SessionSpeechlet - " + title,
           'content': "SessionSpeechlet - " + output
       },
       'reprompt': {
           'outputSpeech': {
               'type': 'PlainText',
               'text': reprompt_text
           }
       },
       'shouldEndSession': should_end_session
   }
def build_response(session_attributes, speechlet_response):
   return {
       'version': '1.0',
       'sessionAttributes': session_attributes,
       'response': speechlet_response
   }
def post_message(client, message_body, url):
   response = client.send_message(QueueUrl = url, MessageBody= message_body)
def lambda_handler(event, context):
   client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
   intent_name = event['request']['intent']['name']
  
# The following needs to be customised
# The intent names shown below are linked with intents created in the custom Alexa Skill.
# The 'post_message' relates to the SQS queue 
# The 'message' line is the message/response that Alexa will speak back to you  
  
   if intent_name == "LightsOn":
       post_message(client, 'on', queue_url)
       message = "Lights will now turn on"
   elif intent_name == "LightsOff":
       post_message(client, 'off', queue_url)
       message = "Lights will now turn off"
   elif intent_name == 'displayzero':
       post_message(client, 'zero', queue_url)
       message = "sure Rohan!"
   elif intent_name == 'displayone':
       post_message(client, 'one', queue_url)
       message = "sure Rohan!"
   elif intent_name == 'displaytwo':
       post_message(client, 'two', queue_url)
       message = "Okay Rohan!"
   elif intent_name == 'displaythree':
       post_message(client, 'three', queue_url)
       message = "Alright!"
   elif intent_name == 'displayfour':
       post_message(client, 'four', queue_url)
       message = "Fantastic four!"
   elif intent_name == 'displayfive':
       post_message(client, 'five', queue_url)
       message = "High Five!"
   elif intent_name == 'displaysix':
       post_message(client, 'six', queue_url)
       message = "sure Rohan!"
   elif intent_name == 'displayseven':
       post_message(client, 'seven', queue_url)
       message = "sure Rohan!"
   elif intent_name == 'displayeight':
       post_message(client, 'eight', queue_url)
       message = "sure Rohan!"
   elif intent_name == 'displaynine':
       post_message(client, 'nine', queue_url)
       message = "Definitely !"
   else:
       message = "Sorry but I do not understand that request"
  
   speechlet = build_speechlet_response("Mirror Status", message, "", "true")
   return build_response({}, speechlet)
0
