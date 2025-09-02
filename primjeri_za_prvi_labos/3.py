import  numpy as np

vector_a = np.array([1,3,5])
print(vector_a)
vector_b = np.array([[2],[4],[6]])
print(vector_b)
print()

mat_mul = np.multiply(vector_a,vector_b)
print(mat_mul)
print()

vect_dot = np.dot(vector_a, vector_b)
print(vect_dot)
print()

mat_exp = np.power(mat_mul,2)
print(mat_exp)
print()

sub_mat = mat_exp[1:, 1:]
print(sub_mat)
print()
