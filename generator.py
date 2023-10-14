import numpy as np

def normalize(obj, type):
    return obj % type

# a > 0 and b > 0 is asssumed
def ggT(a, b):
    u1 = 1
    v1 = 0
    u2 = 0
    v2 = 1
    while a > 1:
        while b > a:
            b -= a
            u2 -= u1
            v2 -= v1
        while a > b:
            a -= b
            u1 -= u2
            v1 -= v2
    return a, u1, v1

def add(a, b, p):
    return (a + b) % p

def mul(a, b, p):
    return (a * b) % p

def inv(a, p):
    if a == 0:
        raise Exception("0 is not invertible")
    else:
        for i in range(p):
            if mul(a, i, p) == 1:
                return i

def random(p):
    return np.random.randint(0, p)

def random_inv(p):
    return np.random.randint(1, p)

def random_inv_matrix(type, size):
    a = np.identity(size)
    v = random_inv(type)
    pos = np.random.randint(0, size, 2)
    if pos[0] == pos[1]:
        a_inv = a.copy()
        a_inv[pos[0], pos[1]] = inv(v, type)
    a_inv = a.copy()
    a_inv[pos[0], pos[1]] = - v
    a[pos[0], pos[1]] = v
    return a, a_inv

def generate(type, size):
    times = 2 * size
    A = np.identity(size)
    A_inv = np.identity(size)
    for i in range(times):
        T, T_inv = random_inv_matrix(type, size)
        A = A @ T
        A_inv = T_inv @ A_inv
    A = normalize(A, type)
    A_inv = normalize(A_inv, type)
    
    B = np.zeros((size, size))

    indices = np.random.randint(0, size, size)
    indices.sort()
    indices = list(indices)
    indices.insert(0, 0)
    indices.append(size)
    length = len(indices)

    for i in range(length - 1):
        i1 = indices[i]
        i2 = indices[i+1]
        ev = random(type)
        for j in range(i1, i2-1):
            B[j][j] = ev
            B[j][j+1] = 1
        if i2 > i1:
            B[i2-1][i2-1] = ev

    M = normalize(A @ B @ A_inv, type)
    return A, A_inv, B, M

if __name__ == "__main__":
    #g, u, v = ggT(8, 19)
    #print(g, u, v)
    for i in range(20):
        generate(2, 4)