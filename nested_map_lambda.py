'''
Aim: Show Usage of Nested Map/Lambda Function -- Replacement of nested for loops..
To showing its usage, i am taking a very simple problem

ip_list= [['a',' b',' c ','d'],['e',' f','g ','h']]
we can see here that there existing space (left or right end of element or both), we wish to remove that space And list is nested one. so, we have to maintain it..
op_list= [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']] 
'''
ip_list= [['a',' b',' c ','d'],['e',' f','g ','h']]
# here we can see nested map function. We can solve this problem by using nested for loops but map/lambda is considered to be fast.
op_list = map(lambda single_list: map(lambda element:element.strip() ,single_list),ip_list)

print op_list