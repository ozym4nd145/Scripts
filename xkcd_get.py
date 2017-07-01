import requests,bs4,os,sys

try:
	os.makedirs('/media/500_GB/xkcd')
except OSError:
	pass

os.chdir('/media/500_GB/xkcd')

try:
	last_file = open("last_file.txt","r")
	last_file = int(last_file.read().split("\n")[0])+1
except IOError:
	print "error"
	last_file=1

base_url = "http://www.xkcd.com/"

while True:
	print "Requesting Page-%d" %last_file
	page = requests.get(base_url+str(last_file));
	
	try:
		page.raise_for_status()
	except:
		last = open("last_file.txt","w")
		last_file-=1
		last.write(str(last_file))
		last.close()
		sys.exit()

	pageSoup = bs4.BeautifulSoup(page.text,"lxml")
	try:
		imageSoup= pageSoup.select("#comic img")[0]
		image_link= imageSoup.get("src")
		image = requests.get("http:"+image_link)
	except:
		print "Error in -%d" %last_file
		last_file += 1
		continue
	else:
		name=(str(last_file)+"_"+os.path.basename(image_link)).encode('utf-8')
		print name
		
		print "Writing Image"
		image_file = open(name,"wb")
		for content in image.iter_content(100000):
			image_file.write(content)
		image_file.close()
		print "Image Written"

		print "Writing Title"
		title = imageSoup.get("title")
		if not title==[]:
			os.system("exif -c --ifd='EXIF' -t='UserComment' \""+name+"\" --set-value=\""+title.encode('utf-8')+"\" -o=\""+name+"\"")
		print "Title Written"

		last_file+=1
