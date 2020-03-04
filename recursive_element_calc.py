
def recursive_element_calc( n ):                  # recursive function calculates n_th element of the sequence
    if n == 1:
        return 2
    elif n == 2:
        return 2
    else:
        return recursive_element_calc( n - 1 ) + recursive_element_calc( n - 2 )


if __name__ == '__main__':
    n = 15                                        # number of element in the sequence to calculate
    nth_element = recursive_element_calc(n)