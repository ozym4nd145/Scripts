import urllib2
import re
from xml.etree import ElementTree as ET

name = open("name","w")
word=""
page = urllib2.urlopen("http://www.cse.iitd.ac.in/index.php/2011-12-29-23-14-30/faculty")
for line in page:
	word += line
srchobj = re.findall('<td\s(?:class="pic"|align="left"|valign="top"|\s|width="346")+?>[\s\n]*?<p>\s?<a href=".*?">(?:\s|\n|<strong>)*?([a-zA-Z\.\s]+?)(?:</strong>|\s|\n)*?</a>',word)
for names in srchobj:
	name.write(names+"\n")
	#print srchobj.group()
