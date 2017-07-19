import json
import requests

with open("./course_db.json", "r") as fl:
    courses = json.loads(fl.read())

cookies = {
    '_ga': 'GA1.3.1716513787.1485603351',
    'SESS1f002926bf876664ed5383994cb4c1de': 'XXXXXXXXXXXXXXXXXXXXXXXXXX',
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
    'Referer': 'https://academics1.iitd.ac.in/Academics/index.php?page=ListCourseN&secret=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&uname=XXXXXXXXXXX',
    'Connection': 'keep-alive',
    'DNT': '1',
}

params = (
    ('page', 'excel'),
    ('secret', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'),
    ('uname', 'XXXXXXXXXXX'),
)

data = {
    'submit': 'Download Data in CSV File',
    'EntryNumber': 'XXXXXX',
    'UserID': 'XXXXXXXXXXX',
}

students = {}
for course in courses:
    print("processing course: ",course["code"])
    try:
        data["EntryNumber"]=course["code"].upper()
        response = requests.post('https://academics1.iitd.ac.in/Academics/GenerateExcel.php',
                    headers=headers, params=params, cookies=cookies, data=data, verify=False)
        if(response.status_code==200):
            student_data = response.content.decode('utf-8').upper().splitlines()[4:]
            student_data = [d.split(',') for d in student_data]
            data_json = [{"name":d[2],"entry":d[1],"group":d[3],"audit_withdraw":d[4],"slot":d[5]} for d in student_data]
            course["students"] = data_json
            for student in course["students"]:
                if student["entry"] not in students:
                    students[student["entry"]]={"name":student["name"],"courses":[]}
                main_course = course.copy()
                del(main_course["students"])
                student_data = student.copy()
                del(student_data["name"])
                del(student_data["entry"])
                main_course.update(student_data)
                students[student["entry"]]["courses"].append(main_course)
    except Exception as e:
        print("Error occurred in course ",course["code"])
        print(e)

with open("student_data.json","w") as fl:
    fl.write(json.dumps(students,indent=4,sort_keys=True))
with open("course_data.json","w") as fl:
    fl.write(json.dumps(courses,indent=4,sort_keys=True))


