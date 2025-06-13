import random

def predict_severity(image_array):
    return random.choice(['Normal', 'Benign', 'Malignant'])

def predict_subtype(image_array):
    return random.choice(['Luminal A', 'Luminal B', 'HER2-positive', 'Triple-negative'])
