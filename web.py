#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web per ww.udl.cat

@author: pedrocalero@ieslallitera.com
'''
import urllib2


class Client(object):
	def get_web(self, page):
		"""descarga la pagina web"""
		f = urllib2.urlopen(page)
		html = f.read()
		f.close()
		return html

	def main(self):
		web = self.get_web('http://www.udl.cat/')
		# buscar el texto
		# imprimir resultados
		print web

if __name__ == "__main__":
	client = Client()
	client.main()
