#!/usr/bin/python2.7
import traceback
import requests,sys,os,bs4,json

def get_manga(url,chapter):
	try:
		manga_http=requests.get(url)
		manga_http.raise_for_status()
		manga_page = bs4.BeautifulSoup(manga_http.text,"lxml")
	except:
		print "Unable to open page - " + url
		print "Exiting"
		return False

	manga_links = manga_page.select("tr td a")
	if len(manga_links) == 0:
		print "Page structure changed! Rewrite the program!"
		return False

	chapters = {}

	for elem in manga_links:
		chapters[str(elem.text.split()[0])] = elem.get("href")


	try:
		manga_link = chapters[chapter]
	except:
		print "Chapter-{} not yet out! :(".format(chapter)
		return False


	path = "/media/500_GB/Manga/One_Piece/"+chapter
	try:
		os.makedirs(path)
	except OSError:
		pass
	os.chdir(path)

	iteration = 0

	print "Download Start"

	while True:
		url_parts = manga_link.split("/")
		if url_parts[-1] == 'end' or url_parts[-3] != chapter:
			print "Done!"
			return True;
		iteration+=1
		if iteration%30 == 0:
			confirmation = raw_input("The manga"+chapter+"seems to be greater than "+ iteration+" pages. Do you want to continue? (y/n)").lower()
			if confirmation in ["yes","y","yup"]:
				print "Continuing"
				iteration = 0
			else:
				print "Exiting"
				return False

		manga_http = requests.get(manga_link)
		manga_http.raise_for_status()
		manga = bs4.BeautifulSoup(manga_http.text,"lxml")

		try:
			manga_link = manga.select(".next a[href]")[0].get("href")
			image_link = manga.select("div .page a img[id]")[0].get("src")
			image = requests.get(image_link)
		except:
			print "Error encountered in page - "+manga_link
			if manga_link != "":
				continue
			else:
				print "Exiting"
				return False

		page_name = "{0:0>3d}.".format(iteration)+os.path.basename(image_link).split(".")[-1]
		print page_name
		image_file = open(page_name,"wb")
		for content in image.iter_content(100000):
			image_file.write(content)
		image_file.close()

if __name__=="__main__":
	url = "http://mangastream.com/manga/one_piece"
	if len(sys.argv) == 1:
		try:
			info_file = open("/media/500_GB/Manga/One_Piece/.info.json","r")
			info = json.loads(info_file.read())
			info_file.close()
			while get_manga(url,str(info['last']+1)):
				info['last'] +=1
				info['chapters'].append(info['last'])
			info_file = open("/media/500_GB/Manga/One_Piece/.info.json","w")
			info_file.write(json.dumps(info))
			info_file.close()
		except Exception as e:
			print "info file not found!"
	else:
		get_manga(url,sys.argv[1])
