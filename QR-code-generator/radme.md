# QR Code Generator

A simple and flexible Python QR code generator with both command-line and interactive modes.

##  Features

- **Dual Mode Operation**: Command-line arguments or interactive input
- **Customizable QR Codes**: Adjust size, border, and colors
- **Flexible Input**: Support for text, URLs, and any encodable data
- **Easy to Use**: Simple CLI interface with sensible defaults

##  Installation

### Option 1: Install from PyPI (when published)
```
pip install my-qr-generator
```
### Option 2: Install from source


# Install dependencies
pip install -r qrcode argparse pillow

## Requirements

- Python 3.7+

- qrcode library

- Pillow library

- Install all dependencies with:

```
pip install qrcode[pil]
```
## Usage
Basic Examples
1. Interactive mode (prompts for text):

```
python myqr.py -f my_qr.png
```
2. Command-line mode:

```
# Generate QR from URL
python myqr.py -t "https://github.com" -f github.png

# Custom colors and size
python myqr.py -t "Hello World" -f hello.png --fg blue --bg white -s 8 -e 2

# Using hex colors
python myqr.py -t "Custom Colors" -f custom.png --fg "#FF5733" --bg "#1E90FF"
Full Command-line Options
text
-t, --text TEXT    Text or URL to encode (optional - will prompt if omitted)
-f, --file FILE    Output filename (default: sample.png)
--fg COLOR         Foreground color (default: black)
--bg COLOR         Background color (default: white)
-s, --size SIZE    Box size/scale (default: 10)
-e, --edge EDGE    Border thickness (default: 1)
-h, --help         Show help message
```
## Advanced Usage
As a Python Module
You can also use the QR generator in your own Python code:

python
from myqr import MyQR

# Create generator instance
qr_gen = MyQR(size=10, edge=1)

# Generate QR code
qr_gen.create_qr_code(
    file_name="output.png",
    fg="black", 
    bg="white",
    data="Your text here"
)
Programmatic Usage
python
import myqr

# Direct function call
myqr.main()  # This uses argparse internally

# Or create custom workflow
qr = MyQR(size=15, edge=2)
qr.create_qr_code("custom.png", "red", "yellow", "Custom QR Code")
