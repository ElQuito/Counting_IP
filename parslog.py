import re
import http
import lxml.etree as ET
from os import listdir

dir = 'log_ip//'
files_in = (listdir(dir))

files_out = open('new_text.txt', 'w')

for file_one in  files:
	file = open(dir + file_one, 'r', encoding='utf8')
	result = re.findall(r'[0-9]+(?:\.[0-9]+){3}', file.read())
	test = dict((x, result.count(x)) for x in set(result) if result.count(x) > 0)
	genexp = ((k, test[k]) for k in sorted(test, key=test.get, reverse=True))
	for k, v in genexp:
		print(k, v)
		files_out.write(str(k) + ' ' + str(v) + '\n')

files_out.close()