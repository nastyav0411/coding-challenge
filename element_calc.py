
def element_calc(a0, a1, n):                    # function calculates n_th element of the sequence
    a = [0] * n
    for i in range(n):
        if i == 0:
            a[i] = a0
        elif i == 1:
            a[i] = a1
        else:
            a[i] = a[i-1] + a[i - 2]
    return  a[n-1]          
            
        



if __name__ == '__main__':
    a0 = 2                                       # first element of the sequence
    a1 = 2                                       # second element of the sequence
    n = 15                                       # number of element in the sequence to calculate
    nth_element = element_calc(a0, a1, n)   