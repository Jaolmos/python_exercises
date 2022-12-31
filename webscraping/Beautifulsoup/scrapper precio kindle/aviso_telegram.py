import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '1814663478:AAFqocTZ0ySjcZgYgeQ9xum0PQ0k1zC6IBw'
    bot_chatID = '1354565595'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Hola!! esto es una prueba!!")
 #print(test)