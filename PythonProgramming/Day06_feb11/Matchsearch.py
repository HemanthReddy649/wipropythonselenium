#match - match returns the exact squence

import re

#o/p match object - matched and span()-start and end index
# checks for a match only at the beginning

text="hello world"
result =re.match("hello",text)
print(result)
#using pattern

test_str ="123566778abcghhhjhjabcABC"
pattern =re.compile("abc")
matches=pattern.finditer(test_str)

#re.finditer() finds all non-overlapping matches of a pattern in a sring and
#returns an iterator of match objects (not a list)
for match in matches:
    print(match)

#search operation searches the entire string
#returns he first occurence

text="python of powerful maths powerful"
result=re.search("powerful",text)
print(result)

# search function -it searches the entire string - find the occurences
#match - beginning only-validate the formats

#raw string for including the special character

a=r"\tHello"
print(a)

#match()-Detemine if the RE matches at the beginning of the string.
#search() - scan through a string,looking for any location where thid RE matches.
#finditre() - Find all substrinng where the RE matchs , and returns them as an iterator.
#findall() - find all the substring where the re matches and returns  a list

#findall()

my_string="abc123ABC123abc"
pattern=re.compile(r'123')
matches=pattern.findall(my_string)

for match in matches:
    print(match)

# methods on match

#group()-Return the string matched by the RE
#start()--return the starting positio of the match
#end(:return the ending position of the match
#span(:return a tuple containing the (start,end)Positions of the match

test_strings ='123abc456789abc123ABC'
pattern = re.compile(r'abc')
matches=pattern.finditer(test_strings)

for match in matches:
    print(match)
    print(match.span(),match.start(),match.end())
    print(match.group()) #return the substring that was by the RE

#special charactes
#meta characters
#regular expressions

#pattern meaning
#abc Matches exact text
#match exact "abc where ever it is appearing

text ="I like abc and abcde"
result=re.findall("abc",text)
print(result)

#[abc] a or b or c- matchs any one of the character
#Match


#[a-z lowercase letters
text="i like abc and ABCGHJHJH"
result =re.findall("[a-z]",text)
print(result)

#[0-9] digits

text ="i like abc and 12345ABCCGHJHJH"


#special characters

'''
Special sequences begin with a backslash \.
Sequence    Meaning    Example
\d  Digit (0–9)    \d\d
\D  Non-digit  \D
\w  Word char (a-z, A-Z, 0-9, _)   \w+
\W  Non-word char  \W
\s  Whitespace \s
\S  Non-whitespace \S
\b  Word boundary  \bcat\b
\B  Not a word boundary    \Bcat
'''

#\d  Digit (0–9)    \d\d
print(re.findall(r"\d","order 123 costs 450"))

#\D  Non-digit  \D
print(re.findall(r"\D","order 123 costs 450"))

#\w  Word char (a-z, A-Z, 0-9, _)   \w+
text="Python_3 version"
print(re.findall(r"\w",text))


#\W  Non-word char  \W
#matches anything that is not a word character
text="Hello@123!"
print(re.findall(r"\W",text))

#\s  Whitespace \s

text="Hello@123\nPython!"
print(re.findall(r"\s",text))

#\S  Non-whitespace \S

text="Hello@123\nPython!"
print(re.findall(r"\S",text))

#\b  Word boundary  \bcat\b

text="cat scatter catalog"
print(re.findall(r"\bcat\b",text))

#\B  Not a word boundary    \Bcat

text="cat scatter catalog"
print(re.findall(r"cat\B",text))



#^ Start of string
text="python is easy"
print(re.findall(r"^python",text))

#$ End of the string

text="python is easy"
print(re.findall(r"easy$",text))

# * 0 or more

text="ab abb abbb a n"
print(re.findall(r"ab*",text))

# + 1 or more
print(re.findall(r"ab+",text))

#? 0 or 1
text="color colour colr"
print(re.findall(r"colou?r",text))

#{n} Exactly n times
text ="111 22 3333 68777"
print(re.findall(r"\d{3}",text))

#{n,} n or more

text="1 22 333 4444"
print(re.findall(r"\d{2,3}",text))

# [] character set

text="Apple banana cat"
print(re.findall(r"[abc]",text))

#( grouping
text="2026-02-11"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})",text))


