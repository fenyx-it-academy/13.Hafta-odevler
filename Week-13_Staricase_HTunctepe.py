width = int(input('\nEnter the size of the staircase (1-100): '))


def staircase_builder(n):
    if n > 0 and n <= 100:
        for i in range(1, n+1):
            print(('#'*i).rjust(n))
            i += 1
    else:
        print('\nEnter the staircase between 1-100: ')


staircase_builder(width)