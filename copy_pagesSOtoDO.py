#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import mwparserfromhell
import pywikibot
import toDO
import vladi_commons

listpages_filename = 'listpages.txt'  # список страниц для обработки
site = pywikibot.Site('ru', 'wikisource')
error_pages = set()

def pagetitle_target(title):
	""" Форматер названия второй страницы """
	# Строка ниже создаёт:
	# 'Страница:Lobachevsky (Syn otechestva).djvu:ВТ/3' → 'Страница:Lobachevsky (Syn otechestva).djvu/3'
	# 'Страница:Lobachevsky (Syn otechestva).djvu:ВТ' → 'Страница:Lobachevsky (Syn otechestva).djvu'
	npages = r'(/\d+)$'
	if re.search(npages, title):
		title_new = re.sub(npages, r':ВТ\1', title)
	return title_new

listpages = vladi_commons.file_readlines_in_set(listpages_filename)
for title_do in listpages:
	if title_do == '': continue

	# Открытие страниц
	page_do = pywikibot.Page(site, title_do)

	title_so = pagetitle_target(title_do)
	page_so = pywikibot.Page(site, title_so)
	try:
		text_so_with_sections = page_so.get()
	except:
		print('no page: ' + title_so)
		error_pages.add(title_so)
		continue

	# Конвертинг
	page_do.text = toDO.convert_sections(text_so_with_sections)

	# Запись страниц
	edit_comment_do = 'сконвертировано в ДО из ' + '[[' + title_so + ']]'
	page_do.save(edit_comment_do)

for p in error_pages:
	print('no page: ' + p)
