# coding: utf-8
import vladi_commons
from scripts import toDO

wikipages_filename = r'..\temp\AWBwikipage.txt'
text = vladi_commons.file_readtext(wikipages_filename)
text = toDO.convert_sections(text)
vladi_commons.file_savetext(wikipages_filename, text)