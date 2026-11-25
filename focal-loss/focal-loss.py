import numpy as np

def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    total_loss = 0.0
    for probability, label in zip(p, y):
        positive_loss = -(1-probability)**gamma*label*np.log(probability)
        negative_loss = -(probability)**gamma*(1-label)* np.log(1-probability)
        total_loss+= positive_loss+negative_loss
    return float(total_loss/len(y))
    pass