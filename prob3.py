number = 600851475143

def is_prime(value):
    for i in range(2,value):
        if value % i == 0:
            return False
    
    return True

for num in range(1,number):
    if number % num == 0:
        print(f"checking {num}")
        large_factor = int(number / num)
        if (is_prime(large_factor)):
            print(large_factor)
            break