import numpy as np

def dice_simmilarity_coef(segmentation, gt, k=1):
    intersection = np.sum(segmentation[gt==k]) * 2.0
    dice = intersection / (np.sum(segmentation) + np.sum(gt))
    return dice