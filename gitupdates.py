#!/usr/bin/env python
# Name:     gitupdates
# Purpose:  Creates a list of git repos, checks for updates and asks if you want to update them.
# By:       Jerry Gamblin
# Date:     22.05.15
# Modified  22.05.15
# Rev Level 0.5
# -----------------------------------------------

import os
import re
import time
import sys
import fileinput
import subprocess
import commands


def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text

    return '\x1b[%dm%s\x1b[0m' % (color_code, text)


def red(text):
    return color(text, 31)

def blue(text):
    return color(text, 34)

searchspace = os.path.expanduser("~")

gitlists = []
outofdategits =[]
gitlists=list(set(gitlists))	
gits=gitlists

for dirname, dirnames, filenames in os.walk(searchspace):
	for subdirname in dirnames:
	    if '.git' in dirnames:
	    	d = (os.path.join(dirname))			
		gitlists.append(d)

for git in gits:
	os.chdir(git)
	command = ("git status -uno | grep -ci 'Your branch is behind'")
	ood = commands.getoutput(command)
	if ood is '1':
			dd = git
			outofdategits.append(dd)


if not outofdategits:
	print'All Repos are up-to-date!'
	sys.exit()

if outofdategit:
	print 'The following repos are out of date:'
	print "\n".join(outofdategits)


	for outofdategit in outofdategits:
		resp = raw_input('\nDo You Want To Update The Repos? (Y/N): ')

		if resp.lower() in ["yes", "y"]:
			print('\nOk, Lets do this!')
			os.chdir(git)
			print ('Updating Repo' + outofdategit)
			updategit = ("git pull'")
			print commands.getoutput(updategit)
			print'\n'
			
		else:
			print('NO? Ok Have Fun!')


