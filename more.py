# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(list_):
    list_len = len(list_)
    print(list_len)
    for idx, name in enumerate(list_):
        if list_len == 1:
            return f"{list_[idx]} likes this"
        elif list_len == 2:
            return f"{list_[idx]} and {list_[idx+1]} like this"
        elif list_len == 3:
            return f"{list_[idx]}, {list_[idx+1]} and {list_[idx+2]} like this"
        else:
            others = list_len-2
            return f"{list_[idx]}, {list_[idx+1]} and {others} others like this"
    return "no one likes this"

test = ["Alex", "James","Ronnie","Lin","Gled"]
#  print(likes(test))

# Alternate 4 Pros
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)
