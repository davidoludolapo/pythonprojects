from credentials import mobile_number

import requests
import schedule
import time

def send_text():
    res = requests.post('http://textbelt.com/text', {
        'phone': mobile_number,
        'message': "Hello Dolapo!, you're doing great. God loves you so much",
        'key': 'textbelt'
    })
    print(res.json())

# schedule.every().day.at('06:00').do(send_text)

schedule.every(10).seconds.do(send_text)

while True:
    schedule.run_pending()
    time.sleep(1)