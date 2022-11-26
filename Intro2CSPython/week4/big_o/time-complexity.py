"""
Time complexity: O(n + n)
Description: The nested loop loops n times for each iteration
of the main loop
"""
def func(n): 
    for i in range(n):
        for j in range(n): 
            if j < I:
                break


"""
Time complexity: O(n + n)
Description: Both the main function and the helper function are O(n)
"""
def func(L):
    for v in L:
        # helper func time complexity is O(n)
        helper_func(v)


"""
Time complexity: O(log n)
Description: j is divided by 2 in each iteration of the first while loop
"""
def func(n):
    j = n
    while j > 0:
        j = j // 2
    while j<n:
        j = j + 3
        n = n - 5
    return j


"""
Time complexity: O(n log n)
Description: Sum and range have a time complexity of O(n) this
combines with the while loop of O(log n)
"""
def func(n):
    total = 0
    while n > 5:
        n = n // 2
        # Remember the time complexity of the sum and range methods
        total += sum(range(n))
    return total


"""
Time complexity: O(n)
Description: For loop is dependant on range of 2,n
"""
def func(n):
    for i in range(2,n):
        if n % i == 0:
            return True
        if i > n/i:
            return False


"""
Time complexity: O(n * n)
Description: Both for loops have a time complexity of O(n)
"""
def func(n):
    for i in range(n):
        for j in range(i):
            if j * j > I:
                break


"""
Time complexity: O(n^2)
Description:
"""
def func(n):
    k=0
    for i in range(n//2, n): 
        j=1
        while (j <= n):
            k += 1
            j *= 2
    return k


"""
Time complexity:
Description:
"""
def helper_func(x):
    for i in range(x): 
        print(i)
    return x


def func(n):
    if n == 2:
        return 0
    else:
        return helper_func(n - 1) + helper_func(n - 2)


"""
Time complexity:
Description:
"""
def helper_func(n):
    for i in range(n**2):
        print(i)


def func(n):
    for i in range(n**2): 
        print(helper_func(100))
    return 0