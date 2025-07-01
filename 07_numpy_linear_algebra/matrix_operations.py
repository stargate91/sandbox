import numpy as np

a = np.array([
	[1,2,3],
	[4,5,6],
	[7,8,9],

])


A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))

C = np.dot(A, B)

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print(f"A = {A}")
print(f"B = {B}")
print(f"A + B = {A+B}")
print(f"A @ B = {C}")
print(f"det A: {det_A:.2f} det B: {det_B:.2f}")

inv_A = np.linalg.inv(A)
A_T = A.T

print(f"A^(-1) = {inv_A}")
print(f"A^T = {A_T}")

eigenvalues_A, eigenvectors_A = np.linalg.eig(A)

print(f"Eigenvalues = {eigenvalues_A}")
print(f"Eigenvectors = {eigenvectors_A}")