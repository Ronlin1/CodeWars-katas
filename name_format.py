# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
#
# Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
#
# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

names = []
def namelist(nameS):

    new_names = []
    for name in nameS:
        name = name.get("name")
        new_names.append(name)

    name_len = len(new_names)
    if name_len == 0:
        return 'waa'
    elif name_len == 1:
        return ''.join(new_names)
    elif name_len == 2:
        return ' & '.join(new_names)
    elif name_len > 2:
        names_with_no_last = new_names[:-1]
        last_name = new_names[-1]
        return ", ".join(names_with_no_last) + ' & ' + ''.join(last_name)


# Alternative solutions
def namelist(names):
    name_str = ''
    if (len(names) > 0):
        for i in xrange(0,len(names)):
            if (i == len(names) - 1 and i > 0):
                name_str += " & "
            elif (i > 0):
                name_str += ", "
            name_str += names[i]['name']

    return name_str

# from codewars
def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

# 4 pros
def namelist(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))
