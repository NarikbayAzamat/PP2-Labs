def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
    return False

ex1 = has_33([1, 3, 3])
ex2 = has_33([1, 3, 1, 1])
ex3 = has_33([3, 1, 3])

print(ex1)
print(ex2)
print(ex3)