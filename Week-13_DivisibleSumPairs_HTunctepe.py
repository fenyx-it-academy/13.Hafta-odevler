# n and k are array size and and a positive integer respectively
n_and_k = list(map(int, input('\nEnter the size of the array a and a positive integer: ').split()))
n = n_and_k[0]
k = n_and_k[1]
matching_pairs = []

array_elements = input('\nEnter the elements of the array size of {}: '.format(n))
a = list(map(int, array_elements.split()))
# print(a)
def divisibleSumPairs(n, k, ar):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if i < j:
                    if (ar[i]+ar[j])%k == 0:
                        matching_pairs.append((i, j))
                    else:
                        continue
                else:
                    continue
    print(matching_pairs)
    return len(matching_pairs)


print(divisibleSumPairs(n, k, a))

