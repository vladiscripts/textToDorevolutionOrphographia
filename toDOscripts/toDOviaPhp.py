# coding: utf-8
import requests
import re
import vladi_commons


def convert(text):
	r = requests.post("http://scripts.my/toDO/toDOraw.php", data={'text': text})
	conv_txt = r.text
	# коррекция слов, которые не надо конвертировать
	conv_txt = re.sub(r"(\n''\w+)ъ(\.'')", r"\1\2", conv_txt)   # ''Критъ.'', ''Сокръ.''
	# conv_txt = re.sub(r"\b([Сс]равн)ъ\.", r"\1.", conv_txt)   # сравнъ.
	return conv_txt

def convert_sections(text):
	# конвертация текста внутри секций
	sections = re.findall(r'<section begin="([^"]+)"[ /]+>(.*?)<section end="\1"', text, re.DOTALL)
	for section in sections:
		conv_txt = convert(section[1])
		text = text.replace(section[1], conv_txt)
	return text
