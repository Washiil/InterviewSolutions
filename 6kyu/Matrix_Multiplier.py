def get_matrix_product(a, b):
    if len(a[0]) != len(b):
        return None
    
    mul = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            x = 0   
            for k in range(len(a[0])):
                x += a[i][k] * b[k][j]    
            row.append(x)
        mul.append(row)
    return mul
