num = int(input("enter the number: "))


def countdigits(num):
    count = 0
    while num != 0:
        count = (count+1)
        num = int(num / 10)
    return count

def reversedigits(num):
    reverse = 0
    while num != 0:
        reverse = (reverse*10) + (num%10)
        num = int(num/10)
    return reverse


print('count', countdigits(num))
print('reverse=', reversedigits(num))