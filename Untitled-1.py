import csv
with open('file.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL) 
    w.writerow(["name", "email", "mobile", "university", "major"])

    while (1):
        name = input()
        email = input()
        mobile = int(input())
        university = input()
        major = input()
        w.writerow([name, email, mobile, university, major, "\n"])
        if(name or email or mobile or university or major == "STOP"): break
