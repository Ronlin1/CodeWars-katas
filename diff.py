# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b keeping their order.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(list_1, list_2):
    diff = []
    for value in list_1:
        diff.append(value)
        for v in list_2:
            if v in diff:
                diff.remove(v)
    return diff

print(array_diff([1,2,3,4],[1,2,6]))

# Alternative 4 Pros
def array_diff(a, b):
    return [x for x in a if x not in b]
