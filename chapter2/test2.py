import re 
text = " Python Exercises "
pattern = r' '
res = re.findall(pattern,text)
result = re.sub(pattern, '', text)
print(result)
# TNN is largest Analytics community of the World