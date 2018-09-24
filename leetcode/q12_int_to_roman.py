def to_roman_numeral(num):
    if num >= 1000:
        return 'M' * (num/1000)
    elif num == 900:
        return 'CM'
    elif 500 <= num <= 800:
        num = num / 100
        return 'D' + 'C' * (num % 5)
    elif num == 400:
        return 'CD'
    elif 100 <= num <= 300:
        return 'C' * (num/100)
    if 50 <= num < 100:
        if num == 90:
            return 'XC'
        elif 90 > num >= 50:
            num = num / 10
            return 'L' + 'X' * (num % 5)
    if 10 <= num < 50:
        if num == 40:
            return 'XL'
        elif 10 <= num < 40:
            return 'X' * (num/10)
    if 0 < num < 10:
        if num == 9:
            return 'IX'
        elif 5 <= num < 9:
            return 'V' + 'I' * (num % 5)
        elif num == 4:
            return 'IV'
        else:
            return 'I' * num


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_values = [1000, 500, 100, 50, 10, 5, 1]
    
    ans = ''
    tens = 1000

    while tens > 0:
        val = num / tens
        num = num % tens

        if val > 0:
            ans += to_roman_numeral(val * tens)

        tens = tens / 10

    return ans


if __name__ == '__main__':
    print(intToRoman(3))
    print(intToRoman(4))
    print(intToRoman(9))
    print(intToRoman(58))
    print(intToRoman(183))
    print(intToRoman(1994))
    print(intToRoman(3999))

