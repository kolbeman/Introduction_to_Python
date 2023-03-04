#!/usr/bin/python3
def cleanup(s):
    return s.lower().strip()
spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]
for old_string in spam:
    new_string = cleanup(old_string)
    print("Original: {} \n Revised: {}".format(old_string,new_string))