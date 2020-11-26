
import boto3
import os
import time
  
access_key = 'Amazon AWS key'
access_secret = 'AWS secret key'
region ='eu-west-1'
queue_url = 'https://sqs.eu-west-1.amazonaws.com/917185725508/RPiQueue002'
  

  
def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)
    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
  
client = boto3.client('sqs', aws_access_key_id = access_key,
                      aws_secret_access_key = access_secret,
                      region_name = region)
  
waittime = 20
client.set_queue_attributes(QueueUrl = queue_url,
                            Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})
  
time_start = time.time()
while (True):
                      print("Checking...")
                      try:
                          message = pop_message(client, queue_url)
                          print(message)
                          if message == "on":
                              os.system("python /home/pi/LEDScripts/LED_on.py")
                          elif message == "off":
                              os.system("python /home/pi/LEDScripts/LED_off.py")
                          elif message == "zero":
                              os.system("python /home/pi/LEDScripts/counter_0.py")
                          elif message == "one":
                              os.system("python /home/pi/LEDScripts/counter_1.py")
                          elif message == "two":
                              os.system("python /home/pi/LEDScripts/counter_2.py")
                          elif message == "three":
                              os.system("python /home/pi/LEDScripts/counter_3.py")
                          elif message == "four":
                              os.system("python /home/pi/LEDScripts/counter_4.py")
                          elif message == "five":
                              os.system("python /home/pi/LEDScripts/counter_5.py")
                          elif message == "six":
                              os.system("python /home/pi/LEDScripts/counter_6.py")
                          elif message == "seven":
                              os.system("python /home/pi/LEDScripts/counter_7.py")
                          elif message == "eight":
                              os.system("python /home/pi/LEDScripts/counter_8.py")
                          elif message == "nine":
                              os.system("python /home/pi/LEDScripts/counter_9.py")
                      except:
                          pass
