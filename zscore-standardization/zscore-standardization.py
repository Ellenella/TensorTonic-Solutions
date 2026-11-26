import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    mean = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis=axis, ddof=0, keepdims=True)
    safe_std = np.where(std < eps, 1.0, std)
    
    return (X - mean) / safe_std
    pass