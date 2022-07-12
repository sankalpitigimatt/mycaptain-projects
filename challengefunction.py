
def most_frequent(st):
    d={}
    for ch in st:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
    for key in d:
        print(key,":",d[key])
    print(dict(sorted(d.items(),key=lambda item: item[1],reverse=True)))
st=input("please enter a string::")

most_frequent(st)

