def find_dups(string):
    all = []
    dup = []
    for s in string.lower():
        if s != " ":
            all.append(s)

        if all.count(s) > 1:
            dup.append(s)

    return len(set(dup))
print(find_dups("Indivisibilities"))

# Alternative for Pros
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)
     
