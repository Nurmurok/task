import re
# 2. Написать программу с использованием регулярного выражения, которая найдет
# строковое значение, в котором есть буква ‘w’ только не в начале слова и не в конце.
import re

pattern = r".+w.+"
text ="""
wonderful
owner
"""
res = re.search(pattern, text)
print(res.group())
