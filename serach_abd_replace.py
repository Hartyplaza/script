def search_replace(my_list, search, replace):
        # Create a new list to store the modified elements
    new_list = []

        # Iterate through the elements in the original list
    for item in my_list:
            # If the current element matches the search element, add the replacement element
        if item == search:
            new_list.append(replace)
        else:
                # Otherwise, keep the original element
            new_list.append(item)

    return new_list

    # Example usage:
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
search = 2
replace = 89
new_list = search_replace(my_list, search, replace)

print(new_list)
print(my_list)

