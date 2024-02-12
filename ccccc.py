def is_palindrome(num_str):
    return num_str == num_str[::-1]

def next_palindrome(from_num, radix, next_palindrome):
    if radix < 2 or radix > 36:
        return 0  

    num = from_num + 1
    max_num = 2**64 - 1 

    while num <= max_num:
        num_str = format(num, f'0{radix}d')
        if is_palindrome(num_str):
            next_palindrome[0] = num
            return 1
        num += 1

    return 0  


from_num = 181
radix = 10
next_palindrome_num = [0]
success = next_palindrome(from_num, radix, next_palindrome_num)

if success:
    print(f"Nejbližší větší palindrom čísla {from_num} v soustavě {radix} je: {next_palindrome_num[0]}")
else:
    print("Nelze najít palindrom větší než zadané číslo.")
