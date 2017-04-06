'''
Aim: 

input list [u' ', u'#', u'&', u'+', u'-', u'0', u'2', u'3', u'4', u'5', u'8', u':', u'a', u'b']

Need to pick out only Alphabets from list.

we can see here that there existing only 'a' and 'b' Alphabets and rest are numeric or special characters.
output list ['a','b']
'''
import re
input_list = [u' ', u'#', u'&', u'+', u'-', u'0', u'2', u'3', u'4', u'5', u'8', u':', u'a', u'b']

output_list=list(re.sub(r"[^a-zA-z]+",'',''.join(input_list)))
print output_list