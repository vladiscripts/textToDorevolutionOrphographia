# coding: utf-8
import requests
import re
# from lxml import etree, html
import vladi_commons

wikipages_filename = r'..\temp\AWBwikipage.txt'
text = vladi_commons.file_readtext(wikipages_filename)

# для тестов
# text = """<section begin="Эвтидем" /><!-- {{№|B}}{{№|C}}{{№|D}} -->один <section end="Эвтидем" /><noinclude>"""

# простой ковертинг
# r = requests.post("http://scripts.my/toDO/toDO.php", data = {'text': text})
# text = r.text

# конвертинг секций
sections = re.findall(r'<section begin="([^"]+)"[ /]+>(.*?)<section end="\1"', text, re.DOTALL)
for section in sections:
	section_txt = section[1]
	r = requests.post("http://scripts.my/toDO/toDO.php", data={'text': section_txt})

	# коррекция слов, которые не надо конвертировать
	conv_txt = r.text
	conv_txt = re.sub(r"(\n''\w+)ъ(.'')", r"\1\2", conv_txt)   # ''Критъ.'', ''Сокръ.''

	text = text.replace(section_txt, conv_txt)

vladi_commons.file_savetext(wikipages_filename, text)