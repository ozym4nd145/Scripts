import json,bs4,requests

l = open("Home Ideas - Decorating and DIY Advice for the Home.html","r")
soup = bs4.BeautifulSoup(l.read())
l.close()

info = []

articles = soup.select(".landing-feed--story")

for article in articles:
	dic = {}
	dic['imgURL'] = article.select(".landing-feed--story-image .swap-image")[0].get("data-src")
	dic['title'] = article.select(".landing-feed--story-title")[0].text
	dic['link'] = article.select(".landing-feed--story-title")[0].get("href")
	dic['description'] = article.select(".landing-feed--story-abstract .abstract-text")[0].text
	try:
		dic['author'] = article.select(".landing-feed--story-abstract .byline--author .byline--author-name")[0].text
	except:
		dic['author']=None
	dic['tags'] = ["home","ideas","home ideas"]
	try:
		tag = article.select(".landing-feed--story-section-name")[0].text
	except:
		pass
	else:
		if not tag.lower in dic['tags']:
			dic['tags'].append(tag)
	info.append(dic)


for num,inf in enumerate(info):
	try:
		for x in xrange(5):
			try:
				a = requests.get(inf['link'])
				a.raise_for_status()
			except:
				time.sleep(10)
			else:
				break
		soup = bs4.BeautifulSoup(a.content)
		ads = soup.find_all(class_=["module-inline-collection","ad-article-breaker","ad-gpt-breaker-container","comments-container--wrap","comments-container--standard-article"])
		for ad in ads:
			ad.extract()
		inf['content']=""
		body = soup.select(".standard-article-body--text")
		if len(body) == 0:
			body = soup.select(".listicle--item")
		for sec in body:
			for img in sec.find_all("img"):
				try:
					img['src'] = img['data-src']
				except:
					pass
			if 'listicle--lead-image' in sec['class']:
				inf['content'] += sec.find(class_='listicle--body-text').prettify()
			else:
				inf['content'] += sec.prettify()
	except:
		inf['content'] = None
		print num
