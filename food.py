import requests,os

def send_to_telegram(message):

    apiToken = os.environ.get("TOKEN")
    chatID = '-1001880210379'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

txt = "یادآوری رزرو غذا!\n غذای هفته‌ی بعد خود را رزرو کنید.\n food.vru.ac.ir"
send_to_telegram(txt)
