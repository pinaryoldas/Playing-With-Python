def cmultiply(a,b):
    """
    Returns the product of two complex numbers.
    Multiplication is by standard method.
    """
    return [a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]]

def to_matrix(num):
    """
    Changes complex number from vector to matrix.
    """
    return [[num[0],-num[1]],[num[1],num[0]]]


def mmultiply(a,b):
    """
    Returns the product of two complex numbers.
    Matrix multiplication method.
    """
    m_a = to_matrix(a)
    m_b = to_matrix(b)
    out = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                out[i][k] += m_a[i][j]*m_b[j][k]

    return [out[0][0],out[1][0]]

def main():
    print("Enter two complex numbers: a+ib, c+id")
    a0 = input("a = ")
    b0 = input("b = ")
    c0 = input("c = ")
    d0 = input("d = ")

    a = [float(a0),float(b0)]
    b = [float(c0),float(d0)]

    product = cmultiply(a,b)

    print("Standard: ({}+{}i)*({}+{}i) = {}+{}i".format(
        a0,b0,c0,d0,product[0],product[1]))

    product = mmultiply(a,b)

    print("Matrix: ({}+{}i)*({}+{}i) = {}+{}i".format(
        a0,b0,c0,d0,product[0],product[1]))

if __name__ == "main":
    main()
    
    print("pinar squeezes noah")
