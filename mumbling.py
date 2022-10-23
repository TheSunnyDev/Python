# The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

Solution:
def accum(s):
    output = ''
    for i,c in enumerate(s):
        for j in range(i+1):
            if j == 0:
                output += c.upper()
            else:
                output += c.lower()
        output += '-'
    return output[:-1] 