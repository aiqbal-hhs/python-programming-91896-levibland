# python script that removes duplicate items from a list

def rmdup(list):
    l = []
    if list:
        for item in list:
            if item not in l:
                l.append(item)
    else:
        return list
    return l

print(rmdup([1, 1, 2, 3, 3, 4]))
