f = open("demofile.txt","a")
f.write("hip")
f.close()

f = open("demofile.txt","r")
print(f.read())

print("Helow")