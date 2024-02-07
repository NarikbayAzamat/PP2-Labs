def list_of_unique_elements(listt):
    new_list = []
    for item in listt:
        if item not in new_list:
            new_list.append(item)
    
    return new_list

nums = [1, 2, 2, 3, 4, 4, 1]
print(list_of_unique_elements(nums))