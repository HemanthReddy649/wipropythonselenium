#REGULAR EXPRESSIONS:
#Match - matches the exact  sequence
#match() - Determine if the RE matches at the beginning of the string.
#search() - Scan through a string, looking for any location where this re matches
#finditer() - Find all substrings
import re
text = "helloworld"
result = re.match("hello" ,text)
print(result)

#using patteren
test_str = "123566778abcghhhjhjabcABC"
pattern = re.compile("123")

#re.finditer() finds all non overlapping matches of a patteren in a string and
#return an iterator of match objects (not a list)
matches = pattern.finditer(test_str)
for match in matches:
    print(match)
#search operation searches the entire string
#returns the first occurence


text = "python is powerful so coding is powerful"
pattern = re.search("powerful", text)
print(pattern)


#findall()
my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

#methods on match

#group() - Return the string matched by the RE
#start() - Return the starting position of the match
#end()   - Return the ending position of the match
#span()  - Return a tuple containing the (start, end) positions of the match


test_string = '123abc456789abc123ABC'
pattern = re.compile('abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span())
    print(match.start())
    print(match.end())
    print(match.group())

#special characters
#meta characters
#Regular  expressions

#abc Matches the exact text
#Match the exact "abc" where ever it is appearing
text ="I like abc and abcde"
result = re.findall("abc", text)
print(result)

#[abc] a or b or c -matches any one of th character
#matches the single characters a or b or c
text ="I like abc and abcde"
result = re.findall("[abc]", text)
print(result)

#[a-z] lower caseletter
text ="I like abc and abcdeABCD"
result = re.findall("[a-z]", text)
print(result)

#[0-9] DIGITS
text ="I like abc and 1234abcde"
result = re.findall("[0-9]", text)
print(result)

#'a b'
text ="cat bat rat mat"
result = re.findall("cat|bat", text)
print(result)
#matches eiter cat or bat

#any single character
text = "cat bat rat bob"
result = re.findall("c.t", text)
print(result)

#SPECIAL CHARACTERS
'''
Special sequence begin with a backslash 
\d Digit(0-9) \d\d
\D non-digit \D
\w Word char (a-z, A-Z, 0-9,...)
\W non word char 
\s White space 
\S non White space
\Word boundary
\B not a boundary
'''
#\d Digit(0-9) \d\d
print(re.findall(r"\d", "Order 123 costs 456"))

#\D non-digit \D
print(re.findall(r"\D", "Order 123 costs 456"))

#\w Word char (a-z, A-Z, 0-9,...)
text = "python_3 version"
result = re.findall(r"\w", text)
print(result)

#\W non word char
text = "hello@123!"
result = re.findall(r"\W", text)
print(result)

#\s White space
text = "hello world\nPython"
result = re.findall(r"\s", text)
print(result)

#\S non White space
text = "helloWorld python"
result = re.findall(r"\S", text)
print(result)

#\b \Word boundary
text = "cat scatter catlog"
result  = re.findall(r"\bcat\b", text)
print(result)

#\B \Word boundary
text = "cat scatter catalog"
result  = re.findall(r"\Bcat\B", text)
print(result)

#META CHARACTERS
'''
Meta-characters have special meaning in regex.

Meta-character  Meaning
.   Any character
^   Start of string
$   End of string
*   0 or more
+   1 or more
?   0 or 1
{n} Exactly n times
{n,}    n or more
{n,m}   Between n and m
[]  Character set
()  Grouping
'''
# ^ start of string
text = "python is easy"
print(re.findall(r"^python", text))

# $ end of string
text = "python is easy"
print(re.findall(r"easy$", text))

# * 0 or more
text =  "ab abb abbb a n"
print(re.findall(r"ab*", text))

# + i or more
text =  "ab abb abbb a n"
print(re.findall(r"ab+", text))

# ?  0 or 1
text = "color colour colr"
print(re.findall(r"colour?", text))

# {n} exactly times

text  = "1 22 333 4444"
print(re.findall(r"\d{3}", text))

#{n,}    n or more
text = "1 22 333 4444"
print(re.findall(r"\d{3,}", text))

#{n,m}   Between n and m
text = "1 22 333 4444"
print(re.findall(r"\d{2,3}", text))

#[] character set
text = "apple banana cat"
print(re.findall(r"[abc]", text))

#() Grouping

text = "2026-02-11"
result = re.findall(r"(\d{4})-(\d{2})-(\d{2})", text)
print(result)

#REGULAR Expression Modifiers
'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''
#re.IGNORECASE   re.I   Case-insensitive matching
text = "Python"
print(re.search("python", text, re.I))

#re.MULTILINE    re.M   ^ and $ match each line
text = "Hello\nPython"
print(re.findall("^Python", text, re.M))

#re.DOTALL   re.S   . matches newline
text = "Hello\nWorld"
print(re.search("Hello.*World", text, re.S))

#re.ASCII    re.A   ASCII-only matching
print(re.findall(r"\w+",text,re.A))

#re.VERBOSE  re.X   Write readable regex with comments
import re

pattern = re.compile(r""" 789sudshskdbksh..%4""", re.DEBUG)
print(pattern)

#ASSERTIONS: VALIDATING THE OUTPUT OR CHECKING CERTAIN CONDITION
"""
^ → Start of string
$ → End of string
b → Word boundary
B → Not word boundary
(?=...) → Positive Lookahead
(?!...) → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
"""


# ^ start of string
text = "python is easy"
print(re.findall(r"^python", text))

# $ end of string
text = "python is easy"
print(re.findall(r"easy$", text))

#\b \Word boundary
text = "cat scatter catlog"
result  = re.findall(r"\bcat\b", text)
print(result)

#\B \Word boundary
text = "cat scatter catalog"
result  = re.findall(r"\Bcat\B", text)
print(result)

# (?=...) positive lookahead = match only if followed by something
text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d)",text))

# (?!...) Negative lookahead
text = "user1 admin2 test"
print(re.findall(r"\w+(?!\d)",text))

#(?<=...) → Positive Lookbehind
text = "price $300"
print(re.findall(r"(?<=$)\d",text))

#(?<!...) → Negative Lookbehind
text = "price $300"
print(re.findall(r"(?<!$)\d",text))