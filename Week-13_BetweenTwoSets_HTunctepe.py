# n,m sizes of first and second arrays

# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


sizes = list(map(int, input('\nEnter the size of array a and array b: ').split()))
n = sizes[0]
m = sizes[1]

array_a_elements = input('\nEnter the elements of array a: ')
a = list(map(int, array_a_elements.split()))
array_b_elements = input('\nEnter the elements of array b: ')
b = list(map(int, array_b_elements.split()))


def getTotalX(a, b):
    multiples_of_array_a = []
    factors_of_array_b = []
    numbers_in_between = [num for num in range(max(a), min(b)+1)]

    for num in numbers_in_between:
        for i in range(len(a)):
            if num % a[i] != 0:
                break
        else:
            multiples_of_array_a.append(num)

    for factor in multiples_of_array_a:
        for num in b:
            if num % factor != 0:
                break
        else:
            factors_of_array_b.append(factor)
    print(factors_of_array_b)
    return len(factors_of_array_b)


getTotalX(a, b)
