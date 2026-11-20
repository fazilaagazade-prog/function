def common_friends(list1, list2):
    result = []
    for name in list1:
        if name in list2:
            result.append(name)
    return sorted(result)


def only_first(list1, list2):
    result = []
    for name in list1:
        if name not in list2:
            result.append(name)
    return sorted(result)


ali = ["Aysel", "Murad", "Leyla", "Elvin"]
vali = ["Leyla", "Nigar", "Aysel", "Kamal"]
print(common_friends(ali, vali))
print(only_first(ali, vali))