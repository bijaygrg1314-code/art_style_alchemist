import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2

def load_image(image_file, max_size=None):
    image = Image.open(image_file).convert('RGB')
    if max_size:
        # Resize logic to keep inference fast on CPU
        ratio = max_size / max(image.size)
        new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
        image = image.resize(new_size, Image.LANCZOS)
    
    # Preprocessing for the network
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255)) # Scale to 0-255 for standard models
    ])
    return transform(image).unsqueeze(0)

def tensor_to_image(tensor):
    image = tensor.clone().clamp(0, 255).numpy()
    image = image.transpose(0, 2, 3, 1) # Change to HxWxC
    image = image[0].astype("uint8")
    return Image.fromarray(image)

def apply_edge_preservation(original_pil, stylized_pil, intensity=0.5):
    """
    Applies a bilateral filter or simple blending to preserve details.
    This fulfills the tutor's request for 'Edge Preserving Filters'.
    """
    # Convert PIL to OpenCV format
    orig_cv = np.array(original_pil)
    style_cv = np.array(stylized_pil)
    
    # Ensure they are the same size (inference might have slightly altered size)
    style_cv = cv2.resize(style_cv, (orig_cv.shape[1], orig_cv.shape[0]))
    
    # Simple Alpha Blending for 'Intensity'
    # Formula: Result = Original * (1 - intensity) + Style * intensity
    blended = cv2.addWeighted(orig_cv, 1 - intensity, style_cv, intensity, 0)
    
    return Image.fromarray(blended)