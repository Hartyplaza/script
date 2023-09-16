def uniq_add(my_list=[]):
    unique_number = list(set(my_list)) #changeing a list to a unique list
    total = sum(unique_number)
    return total

my_list = [1, 2, 3, 1, 4, 2, 5]
sum_total = uniq_add(my_list)
print("Result: {:d}".format(sum_total))
