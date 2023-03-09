import re

pattern = re.compile(r'[a-zA-Z]')

with open('input_text_cleaned.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open('si1.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        len1 = len(line.split())
        print(len1)
        if len1<20:
            line=line
        else:
            line=''
        if pattern.search(line):
            line=''
        line = line.strip()
        line = line.replace('"', '')
        if line:
            file.write(line + '\n')

