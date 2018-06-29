#!/usr/bin/python #2.7
import os
import boto3
import json
from botocore.vendored import requests

bot_id = "YOUR TELEGRAM BOT TOKEN ID"
base_url = "https://api.telegram.org/{}}".format(bot_id)

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        # Structure for inline keyboards
        if 'callback_query' in data:
            message = data['callback_query']['data']
            message_id = data['callback_query']['message']['message_id']
            chat_id = data['callback_query']['message']['chat']['id']
            from_id = data['callback_query']['message']['from']['id']
            callback_query_id = data['callback_query']['id']

            if "cf_metrics" in message:
                url = base_url + "/answerCallbackQuery"
                bot_message = {"callback_query_id": callback_query_id, "text": "Getting CloudFront Metrics", "show_alert":"false"}
                requests.post(url, bot_message)
                response = "Sorry {}, I'm not able to get the metrics".format(first_name)
                bot_message = {"text": response, "chat_id": chat_id, "message_id": message_id}
                url = base_url + "/editMessageText"
                requests.post(url, bot_message)
                
            if "elb_metrics" in message:
                url = base_url + "/answerCallbackQuery"
                bot_message = {"callback_query_id": callback_query_id, "text": "Getting ELB Metrics", "show_alert":"false"}
                requests.post(url, bot_message)
                response = "Sorry {}, I'm not able to get the metrics".format(first_name)
                bot_message = {"text": response, "chat_id": chat_id}
                url = base_url + "/sendMessage"
                requests.post(url, bot_message)
        else:
            #Structure for controlling message response
            message = data["message"]["text"]
            chat_id = data["message"]["chat"]["id"]
            first_name = data["message"]["chat"]["first_name"]
            response = "Please /start, {}".format(first_name)
            bot_message = {"text": response, "chat_id": chat_id}
        
        if "start" in message:
            response = "Hello {}, what do you want to see?".format(first_name)
            keyboard = [['CloudFront Metrics', 'ELB Metrics', 'S3 Metrics']]
            bot_message = {"text": response, "chat_id": chat_id, "reply_markup": json.dumps({'keyboard': keyboard })}
            
        if "help" in message:
            response = "Can I help you, {}? Type /start in order to reach the Menu".format(first_name)
            bot_message = {"text": response, "chat_id": chat_id}
            
        if "CloudFront Metrics" in message:
                response = "Sorry {}, I'm not able to get the metrics".format(first_name)
                bot_message = {"text": response, "chat_id": chat_id}
        if "ELB Metrics" in message:
                response = "Sorry {}, I'm not able to get the metrics".format(first_name)
                bot_message = {"text": response, "chat_id": chat_id}
        if "S3 Metrics" in message:
                response = "Sorry {}, I'm not able to get the metrics".format(first_name)
                bot_message = {"text": response, "chat_id": chat_id}
            
        url = base_url + "/sendMessage"
        requests.post(url, bot_message)

    except:
        return {"statusCode": 500}

    return {"statusCode": 200}
    