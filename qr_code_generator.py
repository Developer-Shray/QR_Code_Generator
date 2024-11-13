import qrcode
from tkinter import Tk,Label, Entry, Button, filedialog

def generate_qr():
    data = entry.get()
    # Generate QR code
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Saving the QR
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files","*.png")])
    if file_path:
        img.save(file_path)
        label.config(text="QR Code Generated Successfully!")

root = Tk()
root.title("QR Code Generator")

label = Label(root, text="Enter text or URL:")
label.pack()

entry = Entry(root, width=50)
entry.pack()

button = Button(root, text="Generate QR Code", command=generate_qr)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()