list_match = [1 for x in range(0,5)]
list_random = [x for x in range(0,5)]

print(list_match.count(list_match[0]) == len(list_match))
# what's this doing?
# in list_match, count the number of times the value of list_match[0] (so, the value of the first element in the list)
# and see if that's equal to the length of the list
print(list_random.count(list_random[0]) == len(list_random))