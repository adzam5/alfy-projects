# List, Functions and all between

# 1
def input_list_helper(nums):
    """
    the input_list_helper() function
    receives numbers from the input_list
    function, calculates their sum and returns
    it as a list

    :return: list of numbers that were given
    by the user, the last object is the sum of all the others
    """
    res = 0

    for n in nums:
        res += n

    nums.append(res)


def input_list():
    """
    the input_list function collcects user
    input, checks to make sure it is a digit
    and appends it to a list.  Once the user presses
    'space' the list is passed to the input_list_helper
    function
    """
    args = []
    arg = ''

    while arg != ' ':
        arg = input()
        if arg.isdigit():
            args.append(float(arg))

    return input_list_helper(args)


# 2
def check_monotonic_sequence(sequence):
    """
    get a sequence (list) of numbers and dtermine its
    monotonicity type

    :return: list of 4 booleans that represent 4 different
    monotonicity characters
    """
    up = False
    us = False
    dn = False
    ds = False
    sorted_sequence = sorted(sequence)

    if len(sequence) < 2:
        return [True, True, True, True]
    if len(set(sequence)) == 1:
        return [True, False, True, False]
    if sequence == sorted_sequence:
        up = True
        set_sequence = list(set(sorted_sequence))
        if set_sequence == sorted_sequence:
            us = True
    elif sequence == sorted_sequence[::-1]:
        dn = True
        sorted_sequence = sorted_sequence[::-1]
        set_sequence = sorted(list(set(sorted_sequence)))[::-1]
        if sequence == set_sequence:
            ds = True

    res = [up, us, dn, ds]
    return res


def check_monotonic_sequence_inverse(def_bool):
    """
    The function that gets a boolean list, and checks if it
    matches any of the valid monotonicity cases, if it does,
    it will return a matching list,
    else (if such doesn't exist such a sequence),
    it will return None

    :param def_bool: a list of 4 booleans
    :return: matching sequence to the booleans
    monotonicity_inverse value
    """
    match def_bool:
        case [1, 1, 0, 0]: return [1, 2, 3, 4, 5, 6, 7, 8]
        case [0, 0, 1, 1]: return [7.5, 4, 3.141, 0.111]
        case [1, 0, 1, 0]: return [1, 1, 1, 1]
        case [1, 0, 0, 0]: return [1, 2, 2, 3]
        case [0, 0, 1, 0]: return [3, 2, 1, 1]
        case [0, 0, 0, 0]: return [1, 0, -1, 1]
        case [1, 1, 1, 1]: return [0]

# 3
def primes_generator(n):
    """
    the functions find and return a list of prime numbers
    with n primes in it.

    :param n: number of primes the function needs to return
    :return: list that contains the amount of n prime numbers.
    """
    num = 2
    res = []

    while len(res) < n:
        fac = set()
        for i in range(1, num + 1):
            if num % i == 0:
                fac.add(i)
        if len(fac) <= 2:
            res.append(num)
        num += 1

    return res


# 4
def is_empty_vector(vec_lst):
    """
    being called by vectors_list_sum()
    to check if a vector list is empty

    :param vec_lst: a list with lists inside of it,
    each sublist is a vector

    :return: True when empty and False when not.
    """
    if not vec_lst:
        return True
    else:
        return False


def vectors_list_sum(vec_lst):
    """
    get a list of vectors, add them to each other
    and returns a vector of their sum.

    :param vec_lst: a list with lists inside of it,
    each sublist is a vector

    :return: list of the total vectors sum.
    """
    if not all(len(vec_lst[0]) == len(l) for l in vec_lst[1:]) or is_empty_vector(vec_lst):
        return 0
    else:
        return list(map(sum, zip(*vec_lst)))


# 5
def calc_the_inner_product(vec_1, vec_2):
    """
    gets two lists, calculates their inner
    product and returns it.

    :param vec_1: list of numbers
    :param vec_2: list of numbers
    :return: the inner product of the two lists
    """
    tmp = []
    res = 0

    if not vec_1 and not vec_2:
        return 0
    if not vec_1 or not vec_2:
        return None
    for i in range(0, len(vec_1)):
        tmp.append(vec_1[i] * vec_2[i])
    for n in tmp:
        res += n

    return res


def orthogonal_number(vectors):
    """
    get list of vectors, and check how many pairs in
    the list are orthogonal.
    Then it returns the amount of pairs as int.
    You should use the calc_the_inner_product() helper
    function for the calculations.

    :param vectors: list of lists, with numbers in it
    :return: number (float), of the amout of orthogonal pairs
    """
    i = 0
    tmp = []
    pairs = 0

    while i < len(vectors) - 1:
        tmp.append(i)
        for l in range(len(vectors)):
            if (i != l) and (l not in tmp):
                res = calc_the_inner_product(vectors[i], vectors[l])
                if res == 0:
                    pairs += 1
        i +=1

    return pairs