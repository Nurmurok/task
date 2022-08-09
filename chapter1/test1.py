import re
# 1. Написать программу с использованием регулярного выражения, которая найдет
# строковое значение, в котором есть буква ‘w’.
import re

pattern = r".+w.+"
text = """
The quick brown fox jumps over the lazy dog.
Python Exercises.
"""
res = re.search(pattern, text)
print(res.group())
