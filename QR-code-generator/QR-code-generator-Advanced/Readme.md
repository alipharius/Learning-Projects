QR Code Generator
A Python QR code generator with both command-line interface and graphical user interface with live preview. This tool allows you to create customizable QR codes for text, URLs, or any other data.

Features
Dual Interface: Command-line for quick generation and GUI for interactive use

Live Preview: See your QR code update in real-time as you type

Customizable: Adjust colors, size, and border of your QR codes

User-Friendly: Simple interface with color pickers and instant feedback

Installation
Make sure you have Python 3.7+ installed

Install the required dependencies:

bash
pip install qrcode pillow
Usage
Command-Line Mode
Generate QR codes quickly from the terminal:

bash
# Generate QR code with text input
python qr_generator.py --text "Hello World" --file output.png

# Generate QR code from URL
python qr_generator.py -t "https://github.com" -f github_qr.png

# Customize appearance
python qr_generator.py -t "Custom QR" -f custom.png --fg blue --bg yellow --size 12 --edge 2
Command-line options:

-t, --text: Text or URL to encode (optional - GUI launches if omitted)

-f, --file: Output filename (default: qrcode.png)

--fg: Foreground color (default: black)

--bg: Background color (default: white)

-s, --size: Box size/scale (default: 10)

-e, --edge: Border thickness (default: 3)

GUI Mode
Run without arguments to launch the graphical interface:

bash
python qr_generator.py
The GUI provides:

Live preview that updates as you type

Color pickers for foreground and background colors

Adjustable settings for box size and border

Save functionality with file dialog

How It Works
CLI Mode: When you provide --text argument, the script generates the QR code and exits

GUI Mode: When no text argument is provided, the graphical interface opens for interactive QR code creation

Live Preview: The GUI updates the QR code preview in real-time with debouncing to prevent excessive regeneration

Technical Details
Built with Python's qrcode library for QR generation

Uses tkinter for the graphical interface

PIL (Pillow) for image processing and display

Real-time preview updates with 250ms debouncing

Supports both color names and hex codes

Example
bash
# Quick generation
python qr_generator.py -t "Visit our website!" -f website_qr.png

# Interactive creation (launches GUI)
python qr_generator.py
Learning Note
The PyQt6 GUI version of this project was AI-assisted as part of my learning journey in GUI development. This helped me understand modern UI patterns, event handling, and creating professional desktop applications.
