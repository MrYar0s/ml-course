import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    r = np.random.rand(data.shape[1])
    val = float(0)
    for i in range(num_steps):
        curr = data.dot(r)
        r = curr/np.linalg.norm(curr)
        val = float(r.dot(curr)/(r.dot(r)))
    
    return val, r