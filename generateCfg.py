import os

url=input("Please input url:")
fileName=input("Please input output file name(default:config.json):")

if(fileName==""):
	fileName="config.json"

s=os.popen("python vmess2json.py "+url,'r')
json=s.read()
s.close()


f=open(fileName,'w')
f.write(json)
f.close()

print("Complited")
#print(json)
os.system("pause")