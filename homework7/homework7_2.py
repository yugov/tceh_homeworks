# Реализовать следующую логику: получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/,
# выводить в консоль все пары "ключ-значение", сохранять полученный json в файл.
import json
import requests

r = requests.get('https://jsonplaceholder.typicode.com/')
for k, v in r.headers.items():
    print(k, ' - ', v)
file = open('placeholder.txt', 'w')
file.write(json.dumps(dict(r.headers)))
file.close()
