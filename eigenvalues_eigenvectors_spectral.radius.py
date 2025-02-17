import numpy as np

# Matrix (a)
A1 = np.array([
    [1, 2],
    [-1, 2]
], dtype=float)

# Matrix (b)
A2 = np.array([
    [-1, 2, 0],
    [0, 3, 4],
    [0, 0, 7]
], dtype=float)

print("\n--- Eigenvalues, Eigenvectors, and Spectral Radius ---")

# Eigenvalues and Eigenvectors for A1
eigvals1, eigvecs1 = np.linalg.eig(A1)
spectral_radius1 = max(abs(eigvals1))
print("Matrix A1:")
for row in A1:
    print(f"  {row}")
print("Eigenvalues:")
for val in eigvals1:
    print(f"  {val:.4f}")
print("Eigenvectors:")
for row in eigvecs1:
    print(f"  {row}")
print(f"Spectral Radius: {spectral_radius1:.4f}")

# Eigenvalues and Eigenvectors for A2
eigvals2, eigvecs2 = np.linalg.eig(A2)
spectral_radius2 = max(abs(eigvals2))
print("\nMatrix A2:")
for row in A2:
    print(f"  {row}")
print("Eigenvalues:")
for val in eigvals2:
    print(f"  {val:.4f}")
print("Eigenvectors:")
for row in eigvecs2:
    print(f"  {row}")
print(f"Spectral Radius: {spectral_radius2:.4f}")
