#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web per ww.udl.cat

@author: pedrocalero@ieslallitera.com
'''
import urllib2
from bs4 import BeautifulSoup


class Client(object):
	def get_web(self, page):
		"""descarga la pagina web"""
		f = urllib2.urlopen(page)
		html = f.read()
		f.close()
		return html

	# buscar el texto
	def search_text(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		elements = soup.find_all("div", "featured-links-item")
		resultats = []
		for element in elements:
			resultats.append(element.find("time")["datetime"])
		return resultats

	def main(self):
		web = self.get_web('http://www.udl.cat/')
		resultat = self.search_text(web)
		# TODO: imprimir resultados
		print resultat

if __name__ == "__main__":
	client = Client()
	client.main()
