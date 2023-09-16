def common_elements(set_1, set_2):
    element = set_1 & set_2
    return element

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
new_elemnt = common_elements(set_1, set_2)
print(sorted(list(new_elemnt)))