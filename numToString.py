def numToString(num: int) -> str:
    denoms = ['thousand', 'million', 'billion']
    digits = str(num)
    width = len(digits)
    if len(digits) % 3 != 0:
        width += (3 - len(digits) % 3)
    digits = f"{num:>0{width}}"
    denom = len(digits) // 3 - 1
    strnum = ""
    for i in range(denom):
        strnum += makeThird(int(digits[3*i:3*i+3])) + " " + denoms[denom-i] + " "
    strnum += makeThird(int(digits[-3:]))
    return strnum


def makeThird(num: int) -> str:
    first20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    strnum = ""
    hundreds = num // 100
    if hundreds != 0:
        strnum += first20[hundreds] + " hundred and "
        num -= hundreds * 100
    ten = num // 10
    if ten >= 2:
        strnum += tens[ten  - 2]
        if num % 10 != 0:
            strnum += " " + first20[num % 10]
    else:
        strnum += first20[num]
    return strnum


print(numToString(0))
print(numToString(19))
print(makeThird(43))
print(makeThird(385))
print(makeThird(0))
print(makeThird(19))
print(numToString(712340))
