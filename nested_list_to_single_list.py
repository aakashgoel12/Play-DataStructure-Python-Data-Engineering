'''Aim: To convert nested list to single list ..
E.g. .. input_list=[[1,2,3,4],[5,6,7,8],[[9,8,10],[11,12]]]
output_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 10, 11, 12]
'''

from compiler.ast import flatten
input_list=[[1,2,3,4],[5,6,7,8],[[9,8,10],[11,12]]]
output_list = flatten(input_list)
print output_list
