import random

mylist = random.sample(range(1, 30), 12)


def withlist(mylist):

    newlist = []
    for x in mylist:
        if not x in newlist:
            newlist.append(x)

    return newlist


def withset(mylist):

    newset = set()
    for x in mylist:
        if not x in newset:
            newset.add(x)

    return newset


list_result = withlist(mylist)
print(f"Result with list: {sorted(list_result)}")

set_result = withset(mylist)
print(f"Result with set: {sorted(set_result)}")
