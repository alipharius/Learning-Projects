import qrcode
import argparse

class MyQR:
    def __init__(self, size: int, edge: int):
        self.size = size
        self.edge = edge

    def create_qr_code(self, file_name: str, fg: str, bg: str, data: str|None = None):
        if data == None:
            data = input('Enter your Text: ').strip()
            if not data:
                print("No text was provided!")
                return

        try:
            qr = qrcode.QRCode(box_size= self.size, border= self.edge)
            qr.add_data(data)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color = fg, back_color = bg)
            qr_image.save(file_name)
        except Exception as e:
            print(f"Error: {e}")


def parse_args():
    epilog = """
Examples:

  1. Generate a QR code from text and save as PNG (interactive fallback if text is omitted):
     python myqr.py -f myqr.png

  2. Generate a QR code from a URL:
     python myqr.py -t "https://github.com" -f github.png --fg blue --bg white

  3. Change the QR size and border:
     python myqr.py -t "Hello World" -f hello.png -s 8 -e 2

Notes:
  - Foreground and background colors can be color names ('red', 'blue') or hex codes ('#1E90FF').
  - If --text is omitted, the program will prompt you to enter the text interactively.
"""

    parser = argparse.ArgumentParser(
        description="Simple QR code generator (CLI + interactive fallback)",
        epilog=epilog,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-t", "--text", help="Text or URL to encode into the QR (if omitted, you'll be prompted)")
    parser.add_argument("-f", "--file", default="sample.png", help="Output filename (default: sample.png)")
    parser.add_argument("--fg", default="black", help="Foreground color for QR (default: black)")
    parser.add_argument("--bg", default="white", help="Background color (default: white)")
    parser.add_argument("-s", "--size", type=int, default=10, help="Box size / scale (default: 10)")
    parser.add_argument("-e", "--edge", type=int, default=1, help="Border thickness (default: 1)")

    return parser.parse_args()
    
def main():
    args = parse_args()
    myqr = MyQR(size=args.size, edge=args.edge)
    myqr.create_qr_code(file_name=args.file, fg=args.fg, bg=args.bg, data=args.text)


if __name__ == "__main__":
    main()
