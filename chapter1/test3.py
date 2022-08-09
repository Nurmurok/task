import re  
# 3. Написать программу с использованием регулярного выражения, которая найдет слово,
# начинающееся на цифру 42.
import re

pattern = r"42.+"
text = """23 street
42 meaning of life
"""
res = re.search(pattern, text)
print(res.group())





