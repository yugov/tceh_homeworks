# Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.

import re
import requests

r = requests.get('https://habrahabr.ru')
links = re.findall(r'"https?:\/\/\S+\w"', str(r.content))
print(links)
