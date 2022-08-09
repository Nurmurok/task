import re
text = input()
pattern = r'^0'

result = re.sub(pattern,"+996",text)
print(result)