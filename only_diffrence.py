def only_diff_elements(set_1, set_2):
    not_in_both = set_1 ^ set_2
    return not_in_both

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))