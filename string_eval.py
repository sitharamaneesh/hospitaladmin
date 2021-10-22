import re
s=input("Enter string alteast 8 character:")
up,num,sp,sub=0,0,0,0
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
fla=True
if len(s)<8:
    print("minimum 8 character required")
elif(len(s)>8):
    for i,j in enumerate(s):
        if j.isupper():
            up+=1
            if up<1:
                fla=False
        if j.isnumeric():
            num+=1
            if num<1:
                fla=False
        if(special_char.search(s) != None):
            sp+=1
            if sp<1:
                fla=False
    if (s.find("qwerty") == -1) or (s.find("Qwerty") == -1) or (s.find("123")==-1) or (s.find("abc")==-1):
        sub+=1
        if(sub>1):
            fla=False
    if(fla):
        print("True")
    else:
        print("False")

