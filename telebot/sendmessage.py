import requests
from .models import TeleSetting


# token = '5581105914:AAG2_TVMlHM3eUVGx1iM2d47cKn9dJr8cmE'
# chat_id = '-714920627'
# text = 'Test 2'


def sendTelegram(tg_name, tg_phone):
    if TeleSetting.objects.get(pk=1):
        settings = TeleSetting.objects.get(pk=1)
        token = settings.tg_token
        chat_id = settings.tg_chat
        text = settings.tg_message
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):

            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]

            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slise = text
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Jo\'natilishda xatolik')
            elif req.status_code == 500:
                print('Xatolik 500')
            else:
                print('Muvaffaqiyatli jo\'natildi')
    else:
        pass
