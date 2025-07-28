import numpy as np
 
#easy exercise of numpy using to normalize and standarize the data

def feature_scaling(data: np.ndarray):
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        standardized_data = (data - mean)/std

        min_value = np.min(data, axis=0)
        max_value = np.max(data, axis=0)
        normalized_data = (data - min_value)/(max_value - min_value)

        return standardized_data, normalized_data