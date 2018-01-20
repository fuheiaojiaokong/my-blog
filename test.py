import string,re
r = "b.e"
if re.match(r,"baoyue"):
    name = re.match(r,"baoyue")
    print(name.group())
else:
    print("Wrong")