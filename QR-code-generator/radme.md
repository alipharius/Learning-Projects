# QR Code Generator

A simple and flexible Python QR code generator with both command-line and interactive modes.

##  Features

- **Dual Mode Operation**: Command-line arguments or interactive input
- **Customizable QR Codes**: Adjust size, border, and colors
- **Flexible Input**: Support for text, URLs, and any encodable data
- **Easy to Use**: Simple CLI interface with sensible defaults


## Requirements

- Python 3.7+

- qrcode library

- Pillow library

- Install all dependencies with:

```
pip install qrcode pillow argparse
```
## Usage
Basic Examples
1. Interactive mode (prompts for text):

```
python myqr.py -f my_qr.png
```
2. Command-line mode:

# Generate QR from URL
python myqr.py -t "https://github.com" -f github.png

# Custom colors and size
python myqr.py -t "Hello World" -f hello.png --fg blue --bg white -s 8 -e 2

# Using hex colors
python myqr.py -t "Custom Colors" -f custom.png --fg "#FF5733" --bg "#1E90FF"

## Full Command-line Options
text:
```
-t, --text TEXT    Text or URL to encode (optional - will prompt if omitted)
-f, --file FILE    Output filename (default: sample.png)
--fg COLOR         Foreground color (default: black)
--bg COLOR         Background color (default: white)
-s, --size SIZE    Box size/scale (default: 10)
-e, --edge EDGE    Border thickness (default: 1)
-h, --help         Show help message
```
