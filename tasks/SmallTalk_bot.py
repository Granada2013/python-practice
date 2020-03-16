import json
import apiai
from colorama import init
init()
from colorama import Fore, Style

def send_message(message):
    request = apiai.ApiAI('f117e60869df4528b17451e674ce1418').text_request()
    request.lang = 'en'
    request.session_id = 'session_id'
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    #print(response)
    print(Fore.YELLOW, response['result']['fulfillment']['speech'], Fore.RESET)
    return response['result']['action']

print('Input your message here')
message = input()
while True:
    action = send_message(message)
    if action == 'smalltalk.greetings.bye':
        break
    message = input()



