import json
import requests
import os

with open("./course_db.json", "r") as fl:
    course_list = json.loads(fl.read())

#curl 'https://academics1.iitd.ac.in/Academics/GenerateExcel.php?page=excel&secret=07d5ba2560b6586a955ec6153ec85ac0a07534d7&uname=2015CS10262' -H 'Cookie: _ga=GA1.3.1716513787.1485603351' -H 'Origin: https://academics1.iitd.ac.in' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.8,hi;q=0.6' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: https://academics1.iitd.ac.in/Academics/index.php?page=ListCourseN&secret=fc93f3c5a0584122f7339d6e19a3b45d05fbc051&uname=2015CS10262' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'submit=Download+Data+in+CSV+File&EntryNumber=COL100&UserID=2015CS10262' --compressed

cookies = {
    '_ga': 'GA1.3.1716513787.1485603351',
}

headers = {
    'Origin': 'https://academics1.iitd.ac.in',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://academics1.iitd.ac.in/Academics/index.php?page=ListCourseN&secret=fc93f3c5a0584122f7339d6e19a3b45d05fbc051&uname=2015CS10262',
    'Connection': 'keep-alive',
    'DNT': '1',
}

params = (
    ('page', 'excel'),
    ('secret', '07d5ba2560b6586a955ec6153ec85ac0a07534d7'),
    ('uname', '2015CS10262')
)

data = {
    'submit': 'Download Data in CSV File',
    'EntryNumber': 'XXXXXX',
    'UserID': 'XXXXXXXXXXX',
}

CSV_DIR = "./csv_files"
os.makedirs("./csv_files", exist_ok=True)

students = {}
courses = {}
for course in course_list:
    code = course["code"].upper()
    slot = course["slot"].upper()
    if (code not in courses):
        courses[code] = {}
    courses[code][slot] = course
    courses[code][slot]["students"] = []

course_codes = list(set([x["code"].upper() for x in course_list]))
course_codes.sort()

def clean_string(s):
    return " ".join(s.upper().split())
for idx,code in enumerate(course_codes):
    print("processing course: %s , %d of %d" %(code,idx+1,len(course_codes)))
    try:
        data["EntryNumber"] = code
        response = requests.post('https://academics1.iitd.ac.in/Academics/GenerateExcel.php',
                                 headers=headers, params=params, cookies=cookies, data=data, verify=False)

        if(response.status_code == 200):
            csv_content = response.content.decode('utf-8').upper()
            with open(os.path.join(CSV_DIR, code + ".csv"), "w") as fl:
                fl.write(csv_content)
            student_data = csv_content.splitlines()[4:]
            student_data = [[clean_string(p) for p in d.split(',')] for d in student_data]
            data_json = [{"name": d[2], "entry":d[1], "group":d[3],
                         "audit_withdraw":d[4], "slot":d[5]} for d in student_data]
            for student in data_json:
                courses[code][student["slot"]]["students"].append(student)
            for student in data_json:
                if student["entry"] not in students:
                    students[student["entry"]] = {
                        "name": student["name"], "courses": []}
                main_course = courses[code][student["slot"]].copy()
                del(main_course["students"])
                student_data = student.copy()
                del(student_data["name"])
                del(student_data["entry"])
                main_course.update(student_data)
                students[student["entry"]]["courses"].append(main_course)
    except Exception as e:
        print("Error occurred in course ", course["code"])
        print(e)

with open("student_data.json", "w") as fl:
    fl.write(json.dumps(students, indent=4, sort_keys=True))
with open("course_data.json", "w") as fl:
    fl.write(json.dumps(courses, indent=4, sort_keys=True))
