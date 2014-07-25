#!/usr/bin/python
#image parser module by sayf_piratos
####################################
from HTMLParser import HTMLParser

class imgHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag=="img":
			self.images_src[dict(attrs)["alt"]] = dict(attrs)["src"]
