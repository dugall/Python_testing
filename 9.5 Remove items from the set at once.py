#5: Remove items from the set at once

set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}

set3 = set1.difference(set2)

print(set3)

set1.difference_update({10, 20, 30})

print(set1)