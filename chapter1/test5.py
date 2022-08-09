import re
# Из URL localhost:8888/ilovepython извлекаем ilovepython

text = 'localhost:8888/ilovepython'
p = re.compile(r'[^localhost:8888/].+')
res = p.findall(text)
print(res)