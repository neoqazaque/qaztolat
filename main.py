# Выставляем кодировку UTF-8 для поддержки кириллицы
# -*- coding: utf-8 -*-
# Для начала устанавливаем пакет requests через pip
# pip install requests
# Затем ее можно импортить в наш код
# Импорт пакета requests
import requests
# Для того чтобы создать бота для телеграм необходимо его создать через @BotFather

token = '506700618:AAHhIoyhw_GS7VirwkleTblXyILdzhpVp54'
url = 'https://api.telegram.org/bot{}/'.format(token)
description = 'Вас приветствует бот QazToLat! Для перевода текста просто отправьте его мне.'

def translate(text):
    alphabet = {
        u'а': u'a',
        u'ә': u'a\'',
        u'б': u'b',
        u'в': u'v',
        u'г': u'g',
        u'д': u'd',
        u'е': u'e',
        u'ё': u'yo',
        u'ф': u'f',
        u'ғ': u'g\'',
        u'х': u'h',
        u'һ': u'h',
        u'і': u'i',
        u'и': u'i\'',
        u'й': u'i\'',
        u'ж': u'j',
        u'к': u'k',
        u'л': u'l',
        u'м': u'm',
        u'н': u'n',
        u'ң': u'n\'',
        u'о': u'o',
        u'ө': u'o\'',
        u'п': u'p',
        u'қ': u'q',
        u'р': u'r',
        u'с': u's',
        u'ш': u's\'',
        u'ч': u'c\'',
        u'т': u't',
        u'ұ': u'u',
        u'ү': u'u\'',
        u'ы': u'y',
        u'у': u'y\'',
        u'з': u'z',
        u'я': u'ya',
        u'ь': u'',
        u'ъ': u'',
        u'ц': u'ts',
        u'щ': u's\'',
        u'ю': u'i\'y\'',
        u'э': u'eh',
        u'A': u'A',
        u'Ә': u'A\'',
        u'Б': u'B',
        u'В': u'V',
        u'Г': u'G',
        u'Д': u'D',
        u'Е': u'E',
        u'Ё': u'Yo',
        u'Ф': u'F',
        u'Ғ': u'G\'',
        u'Х': u'H',
        u'Һ': u'H',
        u'І': u'I',
        u'И': u'I\'',
        u'Й': u'I\'',
        u'Ж': u'J',
        u'К': u'K',
        u'Л': u'L',
        u'М': u'M',
        u'Н': u'N',
        u'Ң': u'N\'',
        u'О': u'O',
        u'Ө': u'O\'',
        u'П': u'P',
        u'Қ': u'Q',
        u'Р': u'R',
        u'С': u'S',
        u'Ш': u'S\'',
        u'Ч': u'C\'',
        u'Т': u'T',
        u'Ұ': u'U',
        u'Ү': u'U\'',
        u'Ы': u'Y',
        u'У': u'Y\'',
        u'З': u'Z',
        u'Я': u'Ya',
        u'Ц': u'Ts',
        u'Щ': u'S\'',
        u'Ю': u'I\'y\'',
        u'Э': u'Eh',
        u'Ь': u'',
        u'Ъ': u''
    }
    translated_text = ''
    for character in text:
        if character in alphabet:
            character = alphabet[character]
        translated_text += character

    return translated_text


def get_updates_json(url, offset = None):
    url += 'getUpdates?timeout=100&allowed_updates=message'
    if offset:
        url += "&offset={}".format(offset)
    response = requests.get(url)
    return response.json()



def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    if not update_ids:
        return None
    else:
        return max(update_ids)


def main():
    offset = None
    while True:
        updates =  get_updates_json(url, offset)
        offset = get_last_update_id(updates)
        if offset is not None:
            offset += 1
        for item in updates['result']:
            message = item['message']
            chat_id = message['chat']['id']
            if 'text' in message:
                if message['text'] == u'/start':
                    send_mess(chat_id, description)
                elif u'/stickers' in  message['text']:
                    send_mess(chat_id, 'https://t.me/addstickers/qaztolatpack')
                else:
                    translated = translate(message['text'])
                    send_mess(chat_id, translated)


if __name__ == '__main__':
    main()



