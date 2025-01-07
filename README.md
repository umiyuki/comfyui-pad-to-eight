# ComfyUI PadToEight Node

This is a custom node for ComfyUI that pads images to multiples of eight dimensions.

## Installation

1. Clone the repository into your ComfyUI custom_nodes directory:
```bash
git clone https://github.com/umiyuki/comfyui-pad-to-eight.git
```

2. Install dependencies:
```bash
cd ComfyUI/custom_nodes/ComfyUI-PadToEight
pip install -r requirements.txt
```

For portable ComfyUI versions:
```bash
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-PadToEight\requirements.txt
```

## Usage

1. Load the node in ComfyUI
2. Connect your image to the PadToEight node
3. The node will automatically pad the image dimensions to be multiples of 8

## Features

- Supports both RGB and RGBA images
- Preserves aspect ratio while padding
- Configurable padding color

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
