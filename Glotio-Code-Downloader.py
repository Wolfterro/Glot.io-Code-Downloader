#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
from urllib2 import urlparse

import os
import sys
import json
import urllib2

version = "1.2"

# Checking, Creating and Accessing the Main Directory
# ===================================================
def main_directory():
	if os.path.exists("Codes"):
		os.chdir("Codes")
	else:
		print("[Glot.io Code Downloader] Creating directory 'Codes' ...")
		os.makedirs("Codes")
		os.chdir("Codes")

# Checking, Creating and Accessing the Code's Directory
# =====================================================
def code_directory(snippet_dir, get_id):
	if os.path.exists(snippet_dir + "-[" + get_id + "]"):
		os.chdir(snippet_dir + "-[" + get_id + "]")
	else:
		print("[Glot.io Code Downloader] Creating directory '" + snippet_dir + "-[" + get_id + "]" + "' ...")
		os.makedirs(snippet_dir + "-[" + get_id + "]")
		os.chdir(snippet_dir + "-[" + get_id + "]")

# Creating the Code Files
# =======================
def get_snippet_codes(num_codes):
	for x in range(0, num_codes):
		get_filename = config["files"][x]["name"].replace("/", "-")
		
		print("[Glot.io Code Downloader] Creating file '" + get_filename + "' ...", end="")
		file_code = open(get_filename, "wb")
		file_code.write(config["files"][x]["content"].encode('utf-8'))
		file_code.close()
		print(" OK!")

# Getting Information About the Snippet From it's JSON Data
# =========================================================
def get_snippet_json(url, api_url):
	global config
	
	try:
		response = urllib2.urlopen(api_url).read().decode('utf-8')
	except Exception:
		print("[Glot.io Code Downloader] Error! Could not open URL '" + url + "'!")
		print("[Glot.io Code Downloader] Check the URL or Internet connection and try again!")
		sys.exit(1)

	config = json.loads(response)

	get_title = config["title"].encode('utf-8')
	num_codes = len(config["files"])
	snippet_dir = get_title.replace("/", "-")

	return [get_title, num_codes, snippet_dir]

# Main Method
# ===========
def main():
	main_directory()

	print("=====================================")
	print("Glot.io Code Downloader - Version %s" % (version))
	print("=====================================\n")
 
	url = raw_input("Insert the Snippet's URL: ")
	url_split = urlparse.urlsplit(url)

	print(" ")
	if str(url_split[1]) != "glot.io" and str(url_split[1]) != "snippets.glot.io":
		print("[Glot.io Code Downloader] Error! Wrong website! Check the URL and try again!")
		sys.exit(1)
	else:
		get_id = os.path.basename(url)
		api_url = "https://snippets.glot.io/snippets/" + get_id

		get_title, num_codes, snippet_dir = get_snippet_json(url, api_url)

		code_directory(snippet_dir, get_id)
		get_snippet_codes(num_codes)

# Initializing Program
# ====================
if __name__ == "__main__":
	main()
