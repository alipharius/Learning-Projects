"""
qr_generator_pyqt.py

A modern QR Code Generator with Live Preview built using PyQt6.
Features:
- Real-time QR code preview as you type
- Color pickers for foreground and background
- Adjustable box size and border
- Professional UI with modern styling
- Both GUI and command-line modes

Dependencies:
    pip install PyQt6 qrcode pillow

Usage:
    python qr_generator_pyqt.py                    # Launch GUI
    python qr_generator_pyqt.py --text "Hello"     # CLI mode
"""

import sys
import argparse
from typing import Optional

import qrcode
from PIL import Image, ImageDraw
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QSpinBox, QFrame, QFileDialog, QMessageBox,
                            QColorDialog, QGroupBox, QFormLayout)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QPixmap, QColor, QFont, QPalette
from PyQt6.QtCore import QSize


class QRGenerator:
    """Utility class for generating QR codes."""
    
    @staticmethod
    def generate_qr(data: str, box_size: int = 8, border: int = 4, 
                   fg_color: str = "black", bg_color: str = "white") -> Image.Image:
        """Generate QR code as PIL Image."""
        if not data.strip():
            # Create a placeholder image
            img = Image.new("RGB", (200, 200), bg_color)
            draw = ImageDraw.Draw(img)
            draw.text((50, 90), "Enter text to preview", fill=fg_color)
            return img
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fg_color, back_color=bg_color)
        return img


class ColorPickerButton(QPushButton):
    """Custom button for color selection with color preview."""
    
    colorChanged = pyqtSignal(str)
    
    def __init__(self, initial_color: str = "#000000"):
        super().__init__()
        self.color = initial_color
        self.setFixedSize(80, 30)
        self.setText(self.color.upper())
        self.clicked.connect(self.pick_color)
        self.update_style()
        
    def update_style(self):
        """Update button style to show the current color."""
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.color};
                color: {'white' if self.is_dark_color(self.color) else 'black'};
                border: 2px solid #cccccc;
                border-radius: 5px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                border: 2px solid #0078D7;
            }}
        """)
    
    @staticmethod
    def is_dark_color(color: str) -> bool:
        """Check if color is dark for text contrast."""
        if color.startswith('#'):
            color = color[1:]
            if len(color) == 3:
                color = ''.join([c*2 for c in color])
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            return luminance < 0.5
        return color.lower() in ['black', 'navy', 'darkblue', 'darkred', 'maroon']
    
    def pick_color(self):
        """Open color dialog and update color."""
        color = QColorDialog.getColor(QColor(self.color))
        if color.isValid():
            self.color = color.name()
            self.setText(self.color.upper())
            self.update_style()
            self.colorChanged.emit(self.color)


class QRPreviewWidget(QLabel):
    """Widget for displaying QR code preview."""
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        self.set_empty_preview()
    
    def set_empty_preview(self):
        """Show placeholder when no QR code is generated."""
        self.setText("Enter text to\nsee QR preview")
        self.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #cccccc;
                border-radius: 10px;
                color: #6c757d;
                font-size: 14px;
                padding: 10px;
            }
        """)
    
    def set_qr_preview(self, pixmap: QPixmap):
        """Display QR code preview."""
        self.setPixmap(pixmap)
        self.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
            }
        """)


class QRGeneratorWindow(QMainWindow):
    """Main application window for QR code generator."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator - PyQt")
        self.setFixedSize(700, 600)
        
        # Initialize settings
        self.settings = {
            'text': '',
            'box_size': 8,
            'border': 4,
            'fg_color': '#000000',
            'bg_color': '#FFFFFF'
        }
        
        # Setup UI
        self.setup_ui()
        
        # Setup preview update timer for debouncing
        self.preview_timer = QTimer()
        self.preview_timer.setSingleShot(True)
        self.preview_timer.timeout.connect(self.update_preview)
    
    def setup_ui(self):
        """Initialize the user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QHBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Left side - Preview
        left_layout = QVBoxLayout()
        left_layout.setSpacing(20)
        
        preview_group = QGroupBox("QR Code Preview")
        preview_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 14px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        preview_layout = QVBoxLayout(preview_group)
        self.preview_widget = QRPreviewWidget()
        preview_layout.addWidget(self.preview_widget)
        
        left_layout.addWidget(preview_group)
        left_layout.addStretch()
        
        # Right side - Controls
        right_layout = QVBoxLayout()
        right_layout.setSpacing(15)
        
        # Input section
        input_group = QGroupBox("QR Code Content")
        input_group.setStyleSheet(preview_group.styleSheet())
        input_layout = QFormLayout(input_group)
        
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter text or URL to encode...")
        self.text_input.textChanged.connect(self.on_text_changed)
        self.text_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #e1e5e9;
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #0078D7;
            }
        """)
        input_layout.addRow("Text/URL:", self.text_input)
        
        right_layout.addWidget(input_group)
        
        # Settings section
        settings_group = QGroupBox("QR Code Settings")
        settings_group.setStyleSheet(preview_group.styleSheet())
        settings_layout = QFormLayout(settings_group)
        
        # Box size
        self.box_size_spin = QSpinBox()
        self.box_size_spin.setRange(1, 20)
        self.box_size_spin.setValue(self.settings['box_size'])
        self.box_size_spin.valueChanged.connect(self.on_setting_changed)
        self.box_size_spin.setStyleSheet("""
            QSpinBox {
                padding: 5px;
                border: 1px solid #e1e5e9;
                border-radius: 3px;
            }
        """)
        settings_layout.addRow("Box Size:", self.box_size_spin)
        
        # Border
        self.border_spin = QSpinBox()
        self.border_spin.setRange(0, 10)
        self.border_spin.setValue(self.settings['border'])
        self.border_spin.valueChanged.connect(self.on_setting_changed)
        self.border_spin.setStyleSheet(self.box_size_spin.styleSheet())
        settings_layout.addRow("Border:", self.border_spin)
        
        # Colors
        self.fg_color_picker = ColorPickerButton(self.settings['fg_color'])
        self.fg_color_picker.colorChanged.connect(self.on_color_changed)
        settings_layout.addRow("Foreground:", self.fg_color_picker)
        
        self.bg_color_picker = ColorPickerButton(self.settings['bg_color'])
        self.bg_color_picker.colorChanged.connect(self.on_color_changed)
        settings_layout.addRow("Background:", self.bg_color_picker)
        
        right_layout.addWidget(settings_group)
        
        # Save button
        self.save_button = QPushButton("Save QR Code")
        self.save_button.clicked.connect(self.save_qr_code)
        self.save_button.setEnabled(False)
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #106EBE;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        right_layout.addWidget(self.save_button)
        
        right_layout.addStretch()
        
        # Combine layouts
        layout.addLayout(left_layout, 1)
        layout.addLayout(right_layout, 1)
    
    def on_text_changed(self, text: str):
        """Handle text input changes with debouncing."""
        self.settings['text'] = text.strip()
        self.save_button.setEnabled(bool(self.settings['text']))
        self.preview_timer.start(300)  # 300ms debounce
    
    def on_setting_changed(self):
        """Handle changes to numeric settings."""
        self.settings['box_size'] = self.box_size_spin.value()
        self.settings['border'] = self.border_spin.value()
        self.preview_timer.start(300)
    
    def on_color_changed(self, color: str):
        """Handle color changes."""
        # Determine which color picker sent the signal
        if self.sender() == self.fg_color_picker:
            self.settings['fg_color'] = color
        else:
            self.settings['bg_color'] = color
        self.preview_timer.start(300)
    
    def update_preview(self):
        """Generate and display QR code preview."""
        if not self.settings['text']:
            self.preview_widget.set_empty_preview()
            return
        
        try:
            # Generate QR code
            qr_image = QRGenerator.generate_qr(
                data=self.settings['text'],
                box_size=self.settings['box_size'],
                border=self.settings['border'],
                fg_color=self.settings['fg_color'],
                bg_color=self.settings['bg_color']
            )
            
            # Convert PIL Image to QPixmap
            qr_image = qr_image.convert("RGB")
            qr_image = qr_image.resize((250, 250), Image.Resampling.LANCZOS)
            
            # Convert to QPixmap
            import io
            buffer = io.BytesIO()
            qr_image.save(buffer, format="PNG")
            
            pixmap = QPixmap()
            pixmap.loadFromData(buffer.getvalue())
            
            self.preview_widget.set_qr_preview(pixmap)
            
        except Exception as e:
            self.show_error(f"Error generating preview: {str(e)}")
    
    def save_qr_code(self):
        """Save the generated QR code to a file."""
        if not self.settings['text']:
            self.show_error("Please enter some text to encode.")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save QR Code",
            f"qr_code_{self.settings['text'][:20]}.png",
            "PNG Images (*.png);;All Files (*)"
        )
        
        if file_path:
            try:
                qr_image = QRGenerator.generate_qr(
                    data=self.settings['text'],
                    box_size=self.settings['box_size'],
                    border=self.settings['border'],
                    fg_color=self.settings['fg_color'],
                    bg_color=self.settings['bg_color']
                )
                
                qr_image.save(file_path)
                self.show_success(f"QR code saved successfully!\n{file_path}")
                
            except Exception as e:
                self.show_error(f"Error saving QR code: {str(e)}")
    
    def show_error(self, message: str):
        """Show error message dialog."""
        QMessageBox.critical(self, "Error", message)
    
    def show_success(self, message: str):
        """Show success message dialog."""
        QMessageBox.information(self, "Success", message)


def run_cli(args: argparse.Namespace) -> None:
    """Generate QR code from command line arguments."""
    try:
        qr_image = QRGenerator.generate_qr(
            data=args.text,
            box_size=args.size,
            border=args.edge,
            fg_color=args.fg,
            bg_color=args.bg
        )
        qr_image.save(args.file)
        print(f"✅ QR code saved to: {args.file}")
    except Exception as e:
        print(f"❌ Error: {e}")


def run_gui() -> None:
    """Launch the PyQt GUI application."""
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show main window
    window = QRGeneratorWindow()
    window.show()
    
    sys.exit(app.exec())


def main() -> None:
    """Main entry point with CLI argument parsing."""
    parser = argparse.ArgumentParser(
        description="QR Code Generator with PyQt GUI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python qr_generator_pyqt.py                    # Launch GUI
  python qr_generator_pyqt.py -t "Hello World"   # CLI mode
  python qr_generator_pyqt.py -t "https://example.com" -s 12 -e 2
        """
    )
    
    parser.add_argument("--text", "-t", help="Text or URL to encode (CLI mode)")
    parser.add_argument("--file", "-f", default="qrcode.png", help="Output filename (CLI mode)")
    parser.add_argument("--fg", default="#000000", help="Foreground color (CLI mode)")
    parser.add_argument("--bg", default="#FFFFFF", help="Background color (CLI mode)")
    parser.add_argument("--size", "-s", type=int, default=10, help="Box size (CLI mode)")
    parser.add_argument("--edge", "-e", type=int, default=4, help="Border thickness (CLI mode)")
    
    args = parser.parse_args()
    
    if args.text:
        run_cli(args)
    else:
        run_gui()


if __name__ == "__main__":
    main()
