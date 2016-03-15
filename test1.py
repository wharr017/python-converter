
# 1-3 = I
# 4 = IV
# 5 = V
# 6 = VI
# 7 = VII
# 8 = VIII
# 9 = XI
# 10 = X
# 11 = XI
# 12 = XII
# 13 = XIII
# 14 = XIV
# 15 = XV
# 19 = XIX
# 20 = XX
# 30 = XXX
# 40 = XL
# 50 = L
# 60 = LX
# 90 = XC
# 100 = C
# 400 = CD
# 500 = D
# 600 = DC
# 900 = CM
# 1000 = M

# now i need to order this list in magnitude
# from large to small on how the algorithm will be built

# anything that isnt specif doesnt need to be on this list
# this list will be how I determine my remainder and how to handle that

# i'll simply use the list to determine my remainder and than traverse
# the list until there is no remainder

import collections

def printRomanNumeral(integer):

    romanNumeral = ((1000, 'M'),
                    (900, 'CM'),
                    (500, 'D'),
                    (400, 'CD'),
                    (100, 'C'),
                    (90, 'XC'),
                    (50, 'L'),
                    (40, 'XL'),
                    (10, 'X'),
                    (9, 'IX'),
                    (5, 'V'),
                    (4, 'IV'),
                    (1, 'I'))
    romanNumeral = collections.OrderedDict(romanNumeral)

    def convertRomanNumeral(integer):
        for largest_RomanNumeral in romanNumeral.keys():
            quotient, remainder = divmod(integer, largest_RomanNumeral)
            yield romanNumeral[largest_RomanNumeral] * quotient
            integer -= (largest_RomanNumeral * quotient)
            if integer > 0:
                convertRomanNumeral(integer)
            else:
                break

    return "".join([roman_rep for roman_rep in convertRomanNumeral(integer)])

integer = 3010

print printRomanNumeral(integer)


