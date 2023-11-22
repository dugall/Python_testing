#8: Sort a tuple of tuples by 2nd item
from operator import itemgetter

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple2 = sorted(tuple1, key=itemgetter(1))

print (tuple2)

#https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value