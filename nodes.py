#  Package Modules
import os
from typing import Union, BinaryIO, Dict, List, Tuple, Optional
import time
import numpy as np

#  ComfyUI Modules
import folder_paths
from comfy.utils import ProgressBar

#  Your Modules
from .modules.calculator import CalculatorModel


#  Basic practice to get paths from ComfyUI
custom_nodes_script_dir = os.path.dirname(os.path.abspath(__file__))
custom_nodes_model_dir = os.path.join(folder_paths.models_dir, "my-custom-nodes")
custom_nodes_output_dir = os.path.join(folder_paths.get_output_directory(), "my-custom-nodes")




import torch
from PIL import Image

class PadToEight:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT")
    RETURN_NAMES = ("image", "width", "height")
    FUNCTION = "pad_to_eight"
    CATEGORY = "Image/Processing"

    def pad_to_eight(self, image):
        image = image.squeeze(0)
        img = Image.fromarray(torch.clip(image * 255.0, 0, 255).cpu().numpy().astype(np.uint8))
        
        width, height = img.size
        
        # Scale to height 1024
        if height != 1024:
            new_width = int(width * (1024 / height))
            img = img.resize((new_width, 1024), Image.Resampling.LANCZOS)
            width, height = img.size

        # Pad width to multiple of 8
        padding_needed = (8 - width % 8) % 8
        if padding_needed > 0:
            padded_img = Image.new('RGB', (width + padding_needed, height), (255, 255, 255))
            padded_img.paste(img, (0, 0))
            img = padded_img
            width, height = img.size
        
        
        image = torch.from_numpy(np.array(img).astype(np.float32) / 255.0).unsqueeze(0)
        return (image, width, height)
