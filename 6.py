# l = [1, 2, 2, 3,4,5,6,5,7,8]
# myList = []
# [ myList.append(item) for item in l if item not in myList]
# print(myList)
# elements = [1, 2, 3, 3, 5, 7, 8, 7, 9]
# unique_elements = {element for element in elements}
# print(unique_elements)
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
     pass 
lst = [1, 2, 2, 3, 4, 5, 4]
print[x for x,c in OrderedCounter(lst).items() if c==1]