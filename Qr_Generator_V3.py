import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog
import pyodbc
from datetime import datetime

# Function to connect to the database
def connect_to_db():
    try:
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=SHRAY\SQLEXPRESS;DATABASE=My_Database;Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print("Error connecting to database: ", e)
        return None

# Function to insert QR code data into the database
def insert_into_db(name, data):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO QRCodeRecords (Name, Content, GeneratedAt) VALUES (?, ?, ?)"
        cursor.execute(query, name, data, timestamp)
        conn.commit()
        cursor.close()
        conn.close()

def generate_qr():
    data = data_entry.get()
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
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)
        label.config(text="QR Code Generated Successfully!")
        
        # Extract the name from file_path
        name = file_path.split('/')[-1].split('.')[0]
        
        # Insert QR code data into database
        insert_into_db(name, data)

root = Tk()
root.title("QR Code Generator")

label_data = Label(root, text="Enter text or URL:")
label_data.pack()

data_entry = Entry(root, width=50)
data_entry.pack()

button = Button(root, text="Generate QR Code", command=generate_qr)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
