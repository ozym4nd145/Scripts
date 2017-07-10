import json
with open("./course_db.json","r") as fl:
    courses = json.loads(fl.read())
with open("./courses.txt","w") as fl:
    for course in courses:
        fl.write(course["code"].upper()+"\n")

cookies = {
    'SESS1fasdf2926bf876664ed5383994cb4c1de': 'asfdasdfsadfsfsadadfasdf',
}

headers = {
    'Origin': 'https://academics1.iitd.ac.in',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://academics1.iitd.ac.in/Academics/index.php?page=CourseCodeN&secret=sdafsdfasdfasdasdfasdfsadfasdfasdfsadf&uname=2015CS10262',
    'Connection': 'keep-alive',
    'DNT': '1',
}

params = {
    'page': 'ListCourseN',
    'secret': 'asdfasdfsadsadfsadfsaddfsadfsadf',
    'uname': '2015CS10262',
}

data = {
    'EntryNumber': 'HSL212',
    'submit-button': 'Submit',
}

ans2 = requests.post('https://academics1.iitd.ac.in/Academics/index.php',
              headers=headers, params=params, cookies=cookies, data=data, verify=False)
