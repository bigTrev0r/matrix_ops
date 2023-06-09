import fractions

#all done circa 2023
#utility matrix class, assumes matrices are lists of rows
#I advise making sure matrices are lists of fraction types, otherwise inversions get impercise, and they wont cancel out to the identity matrix
#all naive implementations of matrix operations, all done by Trevor Bohl (honestly if what's here is any help to you for whatever reason, cheers.)
class matrix:

    #transposes given matrix, returns the new matrix
    def transpose(a:list) -> list:
        return [list([x[i] for x in a]) for i,x in enumerate(a[0])] 
    
    #multiplies one matrix by another. the number of columns in a must of course be equal to the number of rows in b. returns the resulting matrix.
    def mult(a:list,b:list) -> list:
        return [[sum([x*y for x,y in zip(j,k)]) for k in matrix.transpose(b)] for j in a]

    #adds two matrices together. They must both have an equal number of rows and columns. returns the resulting matrix.
    def add(a:list,b:list) -> list:
        return [[x+y for x,y in zip(j,k)] for j,k in zip(a,b)]

    #finds the determinant of a given matrix by cofactor expansion across the first row. must be square. returns determinant of whatever type was stored in the matrix,
    #ideally a fraction, if it is a matrix of real numbers that is.
    def det(a:list) -> fractions.Fraction:
        if len(a) == 2:
            return (a[0][0]*a[1][1]) - (a[0][1]*a[1][0])
        else:
            return sum([r * ((-1) ** (i)) * matrix.det([[x for k,x in enumerate(j) if k != i] for j in a[1:]]) for i,r in enumerate(a[0])])

    #calculates the cofactor matrix of the given matrix, returns said cofactor matrix. must again be sqaure.
    def cfm(a:list) -> list:
        if len(a) == 2:
            return (a[0][0]*a[1][1]) - (a[0][1]*a[1][0])
        else:
            return [[((-1) ** (i+c)) * matrix.det([[x for k,x in enumerate(j) if k != i] 
            for j in a if j!=z]) for i,r in enumerate(z)] for c,z in enumerate(a)] 
    
    #multiplies a matrix by a scalar constant. returns resulting matrix.
    def cmult(a,c):
        return [[c * x for x in j] for j in a]

    #finds the adjugate matrix of the given matrix, returns said adjugate.
    def adj(a:list) -> list:
        return matrix.transpose(matrix.cfm(a))

    #inverts a given matrix. does not check if said matrix is invertible, please make sure its determinant is non zero. returns inverted matrix.
    def inv(a:list) -> list:
        return matrix.cmult(matrix.adj(a),1/matrix.det(a))

#just an example of the class in use
a = [[2,2,3,4,0],[9,0,-3,1,0],[5,-6,6,8,1],[4,0,0,0,0],[9,3,4,3,0]]
a = [[fractions.Fraction(x) for x in r] for r in a]
print(matrix.det(a))
I = matrix.mult(a,matrix.inv(a))
I = [[int(i) for i in r] for r in I]
print(I)
