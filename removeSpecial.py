import re

path = 'C:\\Users\\losl\\Desktop\\losl\\Projects\\FYPJ\\2017P4\\testData.txt'
fp = open(path, 'r')
line = fp.readline()
while line:
    print(line.strip())
    print(re.sub(r'([^\s\w]|_)+', '', line))
    line = fp.readline()

fp.close()
