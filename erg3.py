keimeno=input("dwse keimeno \n")
telkeimeno=""
for i in range(len(keimeno))
	t=keimeno[i]
	if ((ord(t)<78 and ord(t)>64) or (ord(t)>96 and ord(t)<110):
		t=chr(ord(t)=13)
	elif ((ord(t)>77 and ord(t)<91) or (ord(t)>109 and ord(t)<123)):
		t=chr(ord(t)-13)
	telkeimeno+=t
print(telkeimeno)