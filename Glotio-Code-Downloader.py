#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
from bs4 import BeautifulSoup

import os
import sys
import urllib2

'''
* The MIT License (MIT)
* 
* Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>
* 
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
* 
* The above copyright notice and this permission notice shall be included in all
* copies or substantial portions of the Software.
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
'''

version = "1.0" 

# Checking, Creating and Accessing the Main Directory
# ===================================================
def main_directory():
	if os.path.exists("Codes"):
		os.chdir("Codes")
	else:
		print("[Glotio Code Downloader] Creating directory 'Codes' ...")
		os.makedirs("Codes")
		os.chdir("Codes")

# Checking, Creating and Accessing the Code's Directory
# =====================================================
def code_directory(title_dir):
	if os.path.exists(title_dir):
		os.chdir(title_dir)
	else:
		print("\n[Glotio Code Downloader] Creating directory '" + title_dir + "' ...")
		os.makedirs(title_dir)
		os.chdir(title_dir)

# Downloading the Code
# ====================
def get_codes(url, filenames):
	soup = BeautifulSoup(response, 'html.parser')

	get_first_code = soup.findAll('div', {'class' : 'editor'}, id='editor-1')
	get_second_code = soup.findAll('div', {'class' : 'editor hide'}, id='editor-2') 
	get_third_code = soup.findAll('div', {'class' : 'editor hide'}, id='editor-3')
	get_fourth_code = soup.findAll('div', {'class' : 'editor hide'}, id='editor-4')
	get_fifth_code = soup.findAll('div', {'class' : 'editor hide'}, id='editor-5')
	get_sixth_code = soup.findAll('div', {'class' : 'editor hide'}, id='editor-6')
	codes_list = [get_first_code, get_second_code, get_third_code, get_fourth_code, get_fifth_code, get_sixth_code]

	announcer = "[Glotio Code Downloader] Downloading code '"
	announcer_end = "' ..."

	index_number = 0

	for code in codes_list:
		print(announcer + filenames[index_number] + announcer_end, end="")
		file_code = open(filenames[index_number], "wb")
		try:
			file_code.write(code[0].contents[0].strip())
			print(" OK!")
			file_code.close()
			index_number += 1
		except IndexError:
			print(" No code! Skipping ...")
			file_code.close()
			os.remove(filenames[index_number])
			index_number += 1

# Recovering Some Informations and Returning Them
# =============================================== 
def code_information(url):
	global response

	response = urllib2.urlopen(url).read().decode('utf-8')
	soup = BeautifulSoup(response, 'html.parser')
	
	get_title = soup.title.string
	get_title_dir = get_title.replace("/", "-").split(" - ", 1)[0]

	get_filenames = soup.findAll('span', {'class' : 'filename'})
	filename_list = []
	
	for filename in get_filenames:
		filename_list.append(filename.contents[0].strip().replace("/", "-"))

	return [get_title, get_title_dir, filename_list]

# Main Method 
# ===========
def main():
	main_directory()

	print("=====================================")
	print("Glot.io Code Downloader - Version %s" % (version))
	print("=====================================\n")

	url = raw_input("Insert the Snippet's URL: ")

	title, title_dir, filenames = code_information(url)
	code_directory(title_dir)
	get_codes(url, filenames)

# Initializing Program
# ====================
if __name__ == "__main__":
	main()
