
def letter_combinations(digits):
    if len(digits) == 0:
        return []
        
    num_mapper = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    combinations = []
    digits = str(digits)
    letters = [num_mapper[digit] for digit in digits]

    def letter_combinations_rec(prefix, ls):
        if len(prefix) == len(digits):
            combinations.append(prefix)
        
        for l_index in range(0, len(ls)):
            for ch in ls[l_index]:
                letter_combinations_rec(prefix + ch, ls[l_index+1:])

    letter_combinations_rec('', letters)
    return combinations


if __name__ == '__main__':
    d = '234567'
    combinations = letter_combinations(d)
    print(combinations)
