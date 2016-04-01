#!/usr/bin/python2.7

import requests,sys,os,bs4

def get_manga(url,chapter):
	try:
		manga_http=requests.get(url)
		manga_http.raise_for_status()
		manga_page = bs4.BeautifulSoup(manga_http.text,"lxml")
	except:
		print "Unable to open page - " + url
		print "Exiting"
		sys.exit()

	manga_links = manga_page.select("tr td a")
	if len(manga_links) == 0:
		print "Page structure changed! Rewrite the program!"
		sys.exit()

	chapters = {}

	for elem in manga_links:
		chapters[str(elem.text.split()[0])] = elem.get("href")


	try:
		manga_link = chapters[chapter]
	except:
		print "Manga not yet out! :("
		sys.exit()


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
			sys.exit()
		iteration+=1
		if iteration%30 == 0:
			confirmation = raw_input("The manga"+chapter+"seems to be greater than "+ iteration+" pages. Do you want to continue? (y/n)").lower()
			if confirmation in ["yes","y","yup"]:
				print "Continuing"
				iteration = 0
			else:
				print "Exiting"
				sys.exit()

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
				sys.exit()

		page_name = "{0:0>3d}.".format(iteration)+os.path.basename(image_link).split(".")[-1]
		print page_name
		image_file = open(page_name,"wb")
		for content in image.iter_content(100000):
			image_file.write(content)
		image_file.close()

if __name__=="__main__":
	url = "http://mangastream.com/manga/one_piece"
	if len(sys.argv) == 1:
		print "Usage: {0} <chapter number>".format(sys.argv[0])
		sys.exit()
	get_manga(url,sys.argv[1])
