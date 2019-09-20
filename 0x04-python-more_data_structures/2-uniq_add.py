def uniq_add(my_list=[]):
    new_list = []
    [new_list.append(i) for i in my_list if i not in new_list]
    return (sum(new_list))
