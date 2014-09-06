#!/usr/bin/python

# user_input.py
import random
import urllib2, string
from urllib2 import Request, urlopen

quote_dictionary = {1:":D great to see you", 2:":) Nice day seeing ya", 3:"Wats up man, ho's'it goin?"}
quote = random.randint(1, 3)
print(" Welcome to the PacPac Helper ! {0} !".format(quote_dictionary[quote]))

def weather():
	url1='h'
