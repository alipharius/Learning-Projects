"""
qr_generator_with_live_preview.py

A small Python utility that supports both:
 - Command-line QR generation (argparse)
 - A Tkinter GUI with live QR preview and color pickers

Dependencies:
    pip install qrcode pillow

How it works:
 - If you run the script with --text it will generate the QR and exit (CLI mode)
 - If you run it without --text it opens a GUI where you can type text and see a live preview

"""

import qrcode
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk


class MyQR:
    """Utility wrapper around the qrcode library. Returns Pillow images."""

    @staticmethod
    def generate(data: str, box_size: int = 10, border: int = 3, fg: str = "black", bg: str = "white") -> Image.Image:
        """Generate and return a PIL.Image for the given data and styling options.

        Returns a PIL Image in RGBA mode.
        """
        qr = qrcode.QRCode(box_size=box_size, border=border)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg, back_color=bg).convert("RGBA")
        return img


def run_cli(args: argparse.Namespace) -> None:
    """Generate and save a QR image based on CLI args."""
    img = MyQR.generate(data=args.text, box_size=args.size, border=args.edge, fg=args.fg, bg=args.bg)
    img.save(args.file)
    print(f"✅ Saved QR code to: {args.file}")


class QRApp(tk.Tk):
    """Tkinter application with live QR preview and controls."""

    PREVIEW_WH = 220  # preview width/height in pixels

    def __init__(self, default_box: int = 6, default_border: int = 2):
        super().__init__()
        self.title("QR Code Generator — Live Preview")
        self.resizable(False, False)

        # Model variables
        self.text_var = tk.StringVar()
        self.fg_var = tk.StringVar(value="black")
        self.bg_var = tk.StringVar(value="white")
        self.box_var = tk.IntVar(value=default_box)
        self.border_var = tk.IntVar(value=default_border)

        # Keep a reference to the current PhotoImage to avoid GC
        self._preview_photo = None
        # Debounce handle for typing
        self._after_id = None

        self._build_ui()

        # Watch for changes to update preview (debounced)
        # trace_add is available in modern Python/Tk; trace fallback would be similar
        self.text_var.trace_add("write", self._on_change)
        self.fg_var.trace_add("write", self._on_change)
        self.bg_var.trace_add("write", self._on_change)
        self.box_var.trace_add("write", self._on_change)
        self.border_var.trace_add("write", self._on_change)

        # initial preview
        self.update_preview()

    def _build_ui(self) -> None:
        pad = 8
        frm = tk.Frame(self, padx=pad, pady=pad)
        frm.pack()

        # Row 0: label + entry
        tk.Label(frm, text="Text / URL:").grid(row=0, column=0, sticky="w")
        tk.Entry(frm, textvariable=self.text_var, width=42).grid(row=0, column=1, columnspan=3, pady=4)

        # Row 1: colors
        tk.Label(frm, text="Foreground:").grid(row=1, column=0, sticky="w")
        tk.Entry(frm, textvariable=self.fg_var, width=14).grid(row=1, column=1, sticky="w")
        tk.Button(frm, text="Pick", command=self._choose_fg).grid(row=1, column=2, sticky="w")

        tk.Label(frm, text="Background:").grid(row=2, column=0, sticky="w")
        tk.Entry(frm, textvariable=self.bg_var, width=14).grid(row=2, column=1, sticky="w")
        tk.Button(frm, text="Pick", command=self._choose_bg).grid(row=2, column=2, sticky="w")

        # Row 3: box size and border
        tk.Label(frm, text="Box size:").grid(row=3, column=0, sticky="w")
        tk.Spinbox(frm, from_=1, to=40, width=6, textvariable=self.box_var).grid(row=3, column=1, sticky="w")
        tk.Label(frm, text="Border:").grid(row=3, column=2, sticky="w")
        tk.Spinbox(frm, from_=0, to=10, width=6, textvariable=self.border_var).grid(row=3, column=3, sticky="w")

        # Row 4: Save button
        tk.Button(frm, text="Save QR...", command=self._save_qr, bg="#0078D7", fg="white").grid(row=4, column=0, columnspan=4, sticky="we", pady=8)

        # Row 5: preview area
        preview_frame = tk.Frame(frm, relief="sunken", bd=1)
        preview_frame.grid(row=5, column=0, columnspan=4, pady=(6,0))
        self.preview_label = tk.Label(preview_frame)
        self.preview_label.pack(padx=6, pady=6)

    def _choose_fg(self) -> None:
        color = colorchooser.askcolor(title="Choose foreground color", initialcolor=self.fg_var.get())[1]
        if color:
            self.fg_var.set(color)

    def _choose_bg(self) -> None:
        color = colorchooser.askcolor(title="Choose background color", initialcolor=self.bg_var.get())[1]
        if color:
            self.bg_var.set(color)

    def _on_change(self, *args) -> None:
        # Debounce rapid changes (typing) to avoid generating too many images
        if self._after_id:
            self.after_cancel(self._after_id)
        self._after_id = self.after(250, self.update_preview)

    def update_preview(self) -> None:
        """Generate a small preview image and display it in the GUI."""
        data = self.text_var.get().strip()
        if not data:
            # show a neutral placeholder
            placeholder = Image.new("RGBA", (self.PREVIEW_WH, self.PREVIEW_WH), (245, 245, 245, 255))
            self._preview_photo = ImageTk.PhotoImage(placeholder)
            self.preview_label.configure(image=self._preview_photo)
            return

        try:
            img = MyQR.generate(
                data=data,
                box_size=self.box_var.get(),
                border=self.border_var.get(),
                fg=self.fg_var.get(),
                bg=self.bg_var.get(),
            )
            # scale to preview size for display (use NEAREST to keep crisp edges)
            preview = img.resize((self.PREVIEW_WH, self.PREVIEW_WH), Image.NEAREST)
            self._preview_photo = ImageTk.PhotoImage(preview)
            self.preview_label.configure(image=self._preview_photo)
        except Exception as exc:
            # show error as text in the preview area
            self.preview_label.configure(text=f"Error: {exc}")

    def _save_qr(self) -> None:
        data = self.text_var.get().strip()
        if not data:
            messagebox.showerror("Error", "Please enter text or URL to encode.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG image", "*.png")])
        if not file_path:
            return

        try:
            img = MyQR.generate(
                data=data,
                box_size=self.box_var.get(),
                border=self.border_var.get(),
                fg=self.fg_var.get(),
                bg=self.bg_var.get(),
            )
            img.save(file_path)
            messagebox.showinfo("Saved", f"QR code saved to:\n{file_path}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))


def run_gui() -> None:
    app = QRApp()
    app.mainloop()


def main() -> None:
    parser = argparse.ArgumentParser(description="QR Code generator (CLI + GUI)")
    parser.add_argument("--text", "-t", help="Text or URL to encode")
    parser.add_argument("--file", "-f", default="qrcode.png", help="Output filename (CLI mode)")
    parser.add_argument("--fg", default="black", help="Foreground color (CLI mode)")
    parser.add_argument("--bg", default="white", help="Background color (CLI mode)")
    parser.add_argument("--size", "-s", type=int, default=10, help="Box size / scale (CLI mode)")
    parser.add_argument("--edge", "-e", type=int, default=3, help="Border thickness (CLI mode)")

    args = parser.parse_args()

    if args.text:
        run_cli(args)
    else:
        run_gui()


if __name__ == "__main__":
    main()
