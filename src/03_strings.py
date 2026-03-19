# string functions

#len
s = "MILIND"
print(len(s))


#Q1
name = input("Enter your name: ")
print(f"Entered name is: {name}")

letter = '''
Dear <Name>,
You are selected  !
<Date>
'''
print(letter.replace("<Name>", name).replace("<Date>", "19 March"))

print(letter.find("  "))
print(letter.replace("  ", " "))