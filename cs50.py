import bs4
import requests
import os
import sys
import json
from cStringIO import StringIO
import zipfile


os.chdir(#your base directory)

html = open(#file containing html source code of http://cs50.tv/2015/fall/,"rb")
try:
	cs50_soup = bs4.BeautifulSoup(html.read(),"lxml")
except:
	html.close()
	print "Net Problem"
	sys.exit()
html.close()

basic_links = {}
basic_links['lectures'] = cs50_soup.select("#tab-lectures")[0].select(".tree > ul")[0]
basic_links['sections'] = cs50_soup.select("#tab-sections")[0].select(".tree > ul")[0]
basic_links['problems'] = cs50_soup.select("#tab-psets")[0].select(".tree > ul")[0]
basic_links['walkthroughs'] = cs50_soup.select("#tab-walkthroughs")[0].select(".tree > ul")[0]
basic_links['shorts'] = cs50_soup.select("#tab-shorts")[0].select(".tree > ul")[0]
basic_links['seminars'] = cs50_soup.select("#tab-seminars")[0].select(".tree > ul")[0]

for key in basic_links.keys():
	file = open(key+".html","w")
	file.write(basic_links[key].prettify().encode("utf-8"))
	file.close()

try:
	os.mkdir("Lectures")
except:
	pass

for num,week in enumerate(basic_links['lectures'].contents):
	print num
	try:
		os.mkdir("Lectures/Week_"+str(num))
	except:
		pass
	base_path = "Lectures/Week_"+str(num)+"/"
	days = [l.contents[1] for l in week.contents[1].contents]
	for num_day,day in enumerate(days):
		if num_day==0:
			try:
				os.mkdir(base_path+"Wednesday")
			except:
				pass
			path = base_path+"Wednesday/"
		else:
			try:
				os.mkdir(base_path+"Friday")
			except:
				pass
			path = base_path+"Friday/"
		info = {}
		try:
			info['audio'] = day.find_all(class_="title",string="Audio")[0].parent.parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['audio']=None
		try:
			info['links'] = [[q.string.encode("ascii"),q.get("href").encode("ascii")] for q in day.find_all(class_="title",string="Links")[0].parent.parent.find_all("a")]
		except:
			info['links'] = None
		try:
			info['notes'] = day.find_all(class_="title",string="Notes")[0].parent.parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['notes'] = None
		try:
			info['slides'] = day.find_all(class_="title",string="Slides")[0].parent.parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['slides'] = None
		try:
			info['source_code'] = day.find_all(class_="title",string="Source Code")[0].parent.parent.find("a",string="ZIP").parent.find("a",string="download").get("href").encode("ascii")
		except:
			info['source_code'] = None
		try:
			info['subs'] = day.find_all(class_="title",string="Subtitles")[0].parent.parent.find_all("a",string="English")[0].parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['subs'] = None
		try:
			info['syllabus'] = day.find_all(class_="title",string="Syllabus")[0].parent.parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['syllabus'] = None
		try:
			info['transcript'] = day.find_all(class_="title",string="Transcripts")[0].parent.parent.find_all("a",string="English")[0].parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['transcript'] = None
		try:
			info['video_360p'] = day.find_all("a",string="360p")[0].parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['video_360p'] = None
		try:
			info['video_720p'] = day.find_all("a",string="720p")[0].parent.find_all("a",string="download")[0].get("href").encode("ascii")
		except:
			info['video_720p'] = None

		info_file = open(path+"info.json","w")
		info_file.write(json.dumps(info,sort_keys=True,indent=4, separators=(',', ': ')))
		info_file.close()
		print "info done"

		print "notes"
		try:
			link = requests.get(info['notes'])
			link.raise_for_status()
		except:
			print "notes_failed"
			pass
		else:
			link_file = open(path+"Notes.pdf","wb")
			link_file.write(link.content)
			link_file.close()

		print "slides"
		try:
			link = requests.get(info['slides'])
			link.raise_for_status()
		except:
			print "slides_failed"
			pass
		else:
			link_file = open(path+"Slides.pdf","wb")
			link_file.write(link.content)
			link_file.close()

		print "source"
		try:
			link = requests.get(info['source_code'])
			link.raise_for_status()
		except:
			print "source_failed"
			pass
		else:
			link_str = StringIO(link.content)
			link_file = zipfile.ZipFile(link_str,"r")
			link_file.extractall(path=path)
			link_file.close()
		

		print "syllabus"
		try:
			link = requests.get(info['syllabus'])
			link.raise_for_status()
		except:
			print "syllabus_failed"
			pass
		else:
			link_file = open(path+"Syllabus.pdf","wb")
			link_file.write(link.content)
			link_file.close()
		
		print "transcript"
		try:
			link = requests.get(info['transcript'])
			link.raise_for_status()
		except:
			print "transcript_failed"
			pass
		else:
			link_file = open(path+"Transcripts.txt","wb")
			link_file.write(link.content)
			link_file.close()

		print "subs"
		try:
			subs = requests.get(info['subs'])
			subs.raise_for_status()
		except:
			print "subs failed"
			pass
		else:
			subs_file = open(path+os.path.split(info['subs'])[1].rpartition(".")[0],"wb")
			subs_file.write(subs.content)
			subs_file.close()
#######################################################################################################################################

try:
	os.mkdir("Problem_Sets")
except:
	pass

for num,pset in enumerate(basic_links['problems'].contents):
	try:
		os.mkdir("Problem_Sets/ProblemSet_"+str(num))
	except:
		pass
	base_path = "Problem_Sets/ProblemSet_"+str(num)+"/"
	name = pset.find(class_="title").string.encode("ascii").replace(":","")
	


	try:
		std = pset.find(class_="title",string="standard edition").parent.parent
	except:
		std_url=None
		std_dist = None
	else:
		std_url = std.find("a",string="PDF").parent.find("a",string="download").get("href").encode("ascii")
		try:
			std_dist = std.find("a",string="ZIP").parent.find("a",string="download").get("href").encode("ascii")
		except:
			std_dist = None
	
	try:
		hacker = pset.find(class_="title",string="Hacker Edition").parent.parent
	except:
		hacker_url = None
		hacker_dist = None
	else:
		hacker_url = hacker.find("a",string="PDF").parent.find("a",string="download").get("href").encode("ascii")
		try:
			hacker_dist = hacker.find("a",string="ZIP").parent.find("a",string="download").get("href").encode("ascii")
		except:
			hacker_dist = None
	

	try:
		hacker_file = requests.get(hacker_url)
		hacker_file.raise_for_status()
	except:
		print "hacker_failed"
		pass
	else:
		hack = open(base_path+name+"_Hacker.pdf","wb")
		hack.write(hacker_file.content)
		hack.close()

	try:
		std_file = requests.get(std_url)
		std_file.raise_for_status()
	except:
		print "std_failed"
		pass
	else:
		stand = open(base_path+name+"_Standard.pdf","wb")
		stand.write(std_file.content)
		stand.close()

	try:
		hacker_dist_file = requests.get(hacker_dist)
		hacker_dist_file.raise_for_status()
	except:
		print "hacker_dist Failed"
		pass
	else:
		dist_str = StringIO(hacker_dist_file.content)
		dist = zipfile.ZipFile(dist_str,"r")
		dist.extractall(path=base_path)
		dist.close()

	try:
		std_dist_file = requests.get(std_dist)
		std_dist_file.raise_for_status()
	except:
		print "std_dist Failed"
		pass
	else:
		dist_str = StringIO(std_dist_file.content)
		dist = zipfile.ZipFile(dist_str,"r")
		dist.extractall(path=base_path)
		dist.close()
##################################################################################################################################################
