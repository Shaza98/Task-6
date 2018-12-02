import csv
with open('file.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL) 
    w.writerow(["name", "email", "mobile", "university", "major"])

    while (1):
        name = input()
        if(name== "STOP"): break
        email = input()
        if(email== "STOP"): break
        mobile = int(input())
        if(mobile== "STOP"): break
        university = input()
        if(university== "STOP"): break
        major = input()
        if(major == "STOP"): break
        w.writerow([name, email, mobile, university, major, "\n"])
