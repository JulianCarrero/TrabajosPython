##1er punto
A=[4,6,8]
B=[2,2,2]
C=[1,2,3]

n=len(A)
((A[i]*(B[i])+C[i]) for i in range(n))
sumatoria = sum(((A[i]*(B[i])+C[i]) for i in range(n)))+n**2
print(sumatoria)