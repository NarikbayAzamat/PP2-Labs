def filter_prime(list_of_nums):
    prime_numbers = []
    
    for num in list_of_nums:
        if num < 2:
            continue
        
        divisors = 2
        for i in range(2, num):
            if num % i == 0:
                divisors += 1

        if divisors == 2:
            prime_numbers.append(num)
    
    return prime_numbers

nums = [1,2,3,4,5,6,7,8,9,10,11]
print(filter_prime(nums))