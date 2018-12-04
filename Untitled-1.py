import csv
data = []
with open('file.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL) 
    w.writerow(["Name", "Email", "Mobile", "University", "Major"])
    
while True:
    name = input()
    if(name== "STOP"): break 
    data.append(name)   
    email = input()
    if(email== "STOP"): break
    data.append(email)
    mobile = int(input())
    if(mobile== "STOP"): break
    data.append(mobile)
    university = input()
    if(university== "STOP"): break
    data.append(university)
    major = input()
    if(major == "STOP"): break  
    data.append(major)  
  
i=0
while True:
    w.writerow([data(i), data(i+1), data(i+2), data(i+3), data(i+4)])
    i+=1
