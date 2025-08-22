string_maps = {  
"1": "abc",  
"2": "def",  
"3": "ghi",  
"4": "jkl",  
"5": "mno",  
"6": "pqrs",  
"7": "tuv",  
"8": "wxy",  
"9": "z"  
}

def two_digit_combinations(digit_str):
    if len(digit_str) != 2:
        return []   # only works for exactly 2 digits
    
    first_letters = string_maps[digit_str[0]]
    second_letters = string_maps[digit_str[1]]
    
    # Cartesian product via list comprehension
    return [a + b for a in first_letters for b in second_letters]


# Example usage
print(two_digit_combinations("12"))
print(two_digit_combinations("56"))