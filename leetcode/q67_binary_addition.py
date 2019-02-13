def addBinary(a, b):
    if len(a) < len(b):
        temp = b
        b = a
        a = temp

    # ectending the shorter string to match the length of the other string
    b = "0" * (len(a) - len(b)) + b
    print(a)
    print(b)

    remainder = False
    ans = ""
    for i in range(len(a) - 1, -1, -1):
        if remainder == False:
            if a[i] == "0" and b[i] == "0":
                ans = "0" + ans
            elif a[i] == "1" and b[i] == "1":
                ans = "0" + ans
                remainder = True
            else:
                ans = "1" + ans

        else:
            if a[i] == "0" and b[i] == "0":
                ans = "1" + ans
                remainder = False
            elif a[i] == "1" and b[i] == "1":
                ans = "1" + ans
            else:
                ans = "0" + ans

    if remainder:
        ans = "1" + ans

    print(ans)
    return ans


if __name__ == '__main__':
    addBinary("10101011", "10000011001")
