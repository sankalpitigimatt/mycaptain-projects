
a=input("enter file name: ")
n=a.split(".")
if n[-1]=="py":
    print("the extension is PYTHON")
elif n[-1]=="c":
    print("The extension is C")
elif n[-1]=="java":
    print("The extension is JAVA")
elif n[-1]=="html":
    print("The extension is HTML")
else:
    print("The extension does not exists")

