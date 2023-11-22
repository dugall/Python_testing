#2: Merge two Python dictionaries into one
import itertools

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

new_dic = dict(itertools.chain(dict1.items(), dict2.items()))

print (new_dic)