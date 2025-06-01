def check_numbers(numbers):
    if __debug__:
        for num in numbers:
            assert num > 0, f"Number {num} is not positive!"
    print("All numbers are positive!")
check_numbers([1, 2, 3, 4]) 
# raise an assertion error 
check_numbers([5, -2, 7])     
