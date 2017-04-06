'''
Aim: Show Usage of filter || Code Syntax..
To showing its usage, i am taking a very simple problem

input_dictionary={'key1':100,'key2':300,'key3':0,'key4':900,'key5':0}
We need dictionary in which value is atleast greater than zero.
we can see here that key3 and Key5 have 0 value.

output_dictionary = {'key2': 300, 'key1': 100, 'key4': 900}
'''

input_dictionary={'key1':100,'key2':300,'key3':0,'key4':900,'key5':0}
output_dictionary = dict(filter(lambda x: x[1]>0, input_dictionary.items()))
print output_dictionary