import re
#RegEx FUNCTIONS

re.findall	#Returns a list containing all matches
re.search	#Returns a Match object if there is a match anywhere in the string
re.split	#Returns a list where the string has been split at each match
re.sub	    #Replaces one or many matches with a string

#FINDALL

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#SEARCH

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#SPLIT

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#SUB

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#MATCH OBJECTS

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

print(x.span()) #returns a tuple containing the start- and end positions of the match.
print(x.string) #returns the string passed into the function
print(x.group()) #returns the part of the string where there was a match

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())