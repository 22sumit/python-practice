def sum_digits(n):
    if (n==0):
        return 0
    return (n%10 + sum_digits(int(n/10)))

n=123456789
result=sum_digits(n)
print("Sum of digits: ",result)