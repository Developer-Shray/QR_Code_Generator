import qrcode

import pandas as pd

from tkinter import Tk, filedialog, messagebox

'''This is Version 2 file.'''

def generate_qr(data, index, save_path):

    qr = qrcode.QRCode(

        version=1,

        error_correction=qrcode.constants.ERROR_CORRECT_L,

        box_size=10,

        border=4,

    )

    qr.add_data(data)

    qr.make(fit=True)

 

    img = qr.make_image(fill='black', back_color='white')

    img.save(f"{save_path}/QR_{index}.png")

 

def load_excel_and_generate_qrs():

    root = Tk()

    root.withdraw()  

 

   

    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

    if file_path:

        try:

            df = pd.read_excel(file_path)

 

           

            save_path = filedialog.askdirectory()

            if save_path:

                for index, row in df.iterrows():

                    data = row[0]

                    generate_qr(data, index + 1, save_path)

                messagebox.showinfo("Success", "QR codes generated and saved successfully!")

            else:

                messagebox.showwarning("Input Error", "No save location selected.")

        except Exception as e:

            messagebox.showerror("Error", f"An error occurred: {e}")

    else:

        messagebox.showwarning("Input Error", "No file selected.")

 

if __name__ == "__main__":

    load_excel_and_generate_qrs()
