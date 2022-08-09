import re

text = '''
109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"'''
p1 = re.compile(r'\d+\.\d+\.\d+\.\d+')
a1 = p1.findall(text)
print(a1)

p2 = re.compile(r'\d+\/\w+\/\d+\:\d+\:\d+\:\d+ \+\d+')
a2 = p2.findall(text)
print(a2)

p3 = re.compile(r'\d+\.\d+\.\d+\.\d+|\d+\/\w+\/\d+\:\d+\:\d+\:\d+ \+\d+|GET')
a3 = p3.findall(text)
for i in a3:
    if i == 'GET':
        index = int(a3.index('GET'))
        index_date = index - 1
        index_id = index - 2
        print(f'{a3[index_id]} {a3[index_date]} {a3[index]}')
        a3.remove('GET')
    else:
        continue