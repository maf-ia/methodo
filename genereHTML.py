#!/usr/bin/python

import markdown
import codecs
from os import listdir
from os.path import isfile, join

dirfiles = [ f for f in listdir(".") if isfile( join( ".", f ) ) and f[-3:] == ".md" ]
for f in dirfiles:
    with codecs.open( f, mode="r", encoding="utf-8" ) as mdfic:
	text = mdfic.read()
	html = markdown.markdown(text)
	with codecs.open( "./html/" + f[:-2] + "html", "w", encoding="utf-8" ) as htmlfic:
	    htmlfic.write(html)
