import re

## given keywords list, need to find exact match of all keywords if present in string 
def generate_regex_kwd_list(kwd_list):
	pattern_kwd = ''
	for i in street_list:
		i = i.strip()
		if i!='':
			pattern_kwd+='\\b'+i+'\\b'+'|'
	pattern_kwd = pattern_kwd.strip('|')
	reg_kwd = re.compile(pattern_kwd,re.I)
	return reg_kwd

##########################################################
## Test Program function: generate_regex_kwd_list
##########################################################

s =  "my name is aakash goel, part of goels family i love my country India"
kwd_list = ['india','goel']
reg_kwd = generate_regex_kwd_list(kwd_list=kwd_list)

print("Keywords found in String are: {}".format(\
	reg_kwd.findall(s)))
