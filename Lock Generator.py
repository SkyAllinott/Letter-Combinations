Dictionary={}
with open("Dictionary.txt") as Dictionary_File:
    for word in Dictionary_File:
        #Number of character dials
        if len(word.strip())==4:
            Dictionary[word.strip().upper()]= True

#All letters available
a='cgflbptsmd'
b='earthiuoyl'
c='ealtoinsrm'
d='plyamdkesx'

D2={}
for letter1 in a:
    for letter2 in b:
        for letter3 in c:
            for letter4 in d:
                word=(letter1+letter2+letter3+letter4).upper()
                if word in Dictionary:
                    D2[word]=True

print(D2)
while True:
    x = input("Type a word and see if it can be spelled: ").upper()
    if x in D2:
        print(x in D2)


