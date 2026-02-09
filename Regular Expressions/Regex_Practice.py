import re

#1
# Given="Items: ABC-1234, XY-99, DEF-5678, GHI-90120"
#
# pattern=re.compile(r'[A-Za-z]+-\d{4}\b')
#
# matches=pattern.finditer(Given)
#
# for match in matches:
#     print(match.group())

#2

# address="Server 1 is at 192.168.1.1 and Server 2 is at 10.0.0.255. Ignore 999.999."
# pattern=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# matches=pattern.finditer(address)
# for match in matches:
#     print(match.group(0))


#3
# string='var x = "First string"; var y = "Second string";'
# pattern=re.compile(r'"[^"]*"')
# matches=pattern.search(string)
# print(matches)

#4
# email="Contact support@google.com, admin@site.org, or fake@address.net"
# pattern=re.compile(r'[\w.-]+@[\w.-]+(\.com|\.org)\b')
# matches=pattern.finditer(email)
#
# for match in matches:
#     print(match.group(0))

#5
#
# typo="I went to to the store and and bought milk."
# pattern=re.compile(r'\b(\w+) \1\b')
# matches=pattern.finditer(typo)
# for match in matches:
#     print(match)

#6
# hex_colours="Colors: #FFF, #abC, #123456, #000000 ,#rbc1232. Invalid: #RG, #1234, #1234567"
# pattern=re.compile(r'#([a-z0-9]{3}|[a-z0-9]{6})\b',re.I)
# matches=pattern.finditer(hex_colours)
# for match in matches:
#     print(match.group(0))

#7
# Target_String="background.jpg, profile.PNG, data.txt, icon.gif, script.js"
# pattern=re.compile(r'\w+\.(jpg|png|gif)',re.IGNORECASE)
# matches=pattern.finditer(Target_String)
# for match in matches:
#     print(match.group(0))

#8
# Price="Price: $50, $1,200.50, $9.99, 500 dollars, $200"
# pattern=re.compile(r'\$\d+(\.\d+|,\d+)*')
# matches=pattern.finditer(Price)
# for match in matches:
#     print(match)

#9
# proper_noun="Alice and Bob went to Paris. The quick brown fox."
# pattern=re.compile(r'[A-Z][a-z]+')
# matches=pattern.finditer(proper_noun)
# for match in matches:
#     print(match)

#10
# double_letter="I will look for a book and an apple."
# pattern=re.compile(r'\b\w+(\w)\1\w*\b')
# matches=pattern.finditer(double_letter)
# for match in matches:
#     print(match)
