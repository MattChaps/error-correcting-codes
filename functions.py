#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code

def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G

#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n

def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v


#Preliminary setup ########################################


import numpy as np

def int_to_bin(num,w):
    #input number to be converted into binary and width of list

    bin_lst = []

    #turns binary string into list of integers
    for j in np.binary_repr(num, width = w):        
        bin_lst.append(int(j))
    return bin_lst

def bin_to_int(bin_lst):        
    #input binary list to be converted into integer

    #reverse the list
    bin_lst = bin_lst[::-1]     
    total = 0
    for i in range(len(bin_lst)):
        total += bin_lst[i]*2**i
    return total


#Q1 #######################################################


def message(a):
    l = len(a)
    r = 2
    k = 2**r - r - 1
    while l > k - r:
        r += 1
        k = 2**r - r -1
    m = int_to_bin(l,r)
    m.extend(a)
    m.extend([0]*(k-l-r))
    return m


#Q2 #######################################################


def hammingEncoder(m):
    len_m = len(m)
    r = 2
    len_vect = 2**r - r - 1
    while len_m != len_vect:
        r += 1
        len_vect = 2**r - r - 1
        if len_vect > len_m:
            return []
    G = hammingGeneratorMatrix(r)
    c = np.dot(m,G) % 2
    c = list(c)
    return c 

#Q3 #######################################################

def hammingDecoder(v):
    len_v = len(v)
    r = 2
    len_vect = 2**r - 1
    while len_v != len_vect:
        r += 1
        len_vect = 2**r - 1
        if len_vect > len_v:
            return []
        
    #Apply Syndrome decoding with HT as the transpose of the matrix H
    HT = []     
    for i in range(1,len_v+1):
	    lst = int_to_bin(i,r)
	    HT.append(lst)
    HT = np.array(HT)
    vHT = np.dot(v, HT) % 2
    if 1 not in vHT:
        return v
    i = bin_to_int(vHT)
    v[i-1] = (v[i-1] + 1) % 2
    return(v)

#Q4 #######################################################

def messageFromCodeword(c):
    len_c = len(c)
    r = 2
    len_vect = 2**r - 1
    while len_c != len_vect:
        r += 1
        len_vect = 2**r - 1
        if len_vect > len_c:
            return []
    c = list(c)
    for i in range(r):
        #replace data in indices of list to be deleted with a dummy variable, in this case the number "3"
        c[2**i-1] = 3       
    while 3 in c:
        #remove all dummy variables from list to get message
        c.remove(3)          
    m = c
    return m

#Q5 #######################################################

def dataFromMessage(m):
    len_m = len(m)
    r = 2
    len_vect = 2**r - r - 1
    while len_m != len_vect:
        r += 1
        len_vect = 2**r - r - 1
        if len_vect > len_m:
            return []
    bin_str = m[:r]
    l = bin_to_int(bin_str)
    if r+l > len_vect:
        return []
    a = m[r:r+l]
    return a

#Q6 #######################################################
  
def repetitionEncoder(m,n):
    c = m*n
    return c

#Q7 #######################################################

def repetitionDecoder(v):
    num_zeros = v.count(0)
    num_ones = v.count(1)
    if num_zeros == num_ones:
        return []
    elif num_zeros > num_ones:
        m = [0]
    else:
        m = [1]
    return m

#end ######################################################
