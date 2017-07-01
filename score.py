import pynotify, time, requests

pynotify.init("Ind VS NZ T20 World Cup")


while True:
	while True:
		raw_score = requests.get("http://cricapi.com/api/cricketScore/",params={'unique_id':'951339'})
		try:
			raw_score.raise_for_status()
		except:
			time.sleep(5)
		else:
			score = raw_score.json()['score']
			break
	notify = pynotify.Notification("IND VS NZ",score)
	print score
	notify.show()
	time.sleep(60)