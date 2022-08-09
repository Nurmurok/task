import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
username = input('введите имя:')
password = input("введите пароль: ")
result = re.findall(pattern, password)
if (result):
        print ("вы успешно зазегистрированы!")
else:
        print ("Пароль должен быть длиннее 8 символов и содержать спец символы, цифры, большые и прописные латинские буквы")