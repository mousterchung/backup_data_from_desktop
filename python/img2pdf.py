import img2pdf
from PIL import Image

import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox



file_types = (('jpeg files', '*.jpg'), ('png files', '*.png'), ('gif files', '*.gif'), ('pdf files', '*.pdf'), ('all files', '*.*'))

window = tk.Tk()
window.title = 'image to PDF file converter'
window.geometry('400x400')
window.resizable(False, False)
window.iconbitmap(os.path.join('.', 'img', 'favicon.ico'))

title_label = ttk.Label(text='image to PDF file converter')
title_label.grid(column=0, row=0, rowspan=2)

img_path = tk.StringVar(window, '')
img_path_entry = ttk.Entry(window, textvariable=img_path)
img_path_entry.grid(column=0, row=1)
def reconfirm_img_only_file_name():
    global img_only_file_name
    img_only_file_name = img_path.get().split(os.path.sep)[-1].replace('.jpg', '').replace('.png', '').replace('.gif', '')
reconfirm_img_only_file_name()

def browse_file_path_command():
    global img_path
    img_path.set(fd.askopenfilename(parent=window, title='select image file', filetypes=file_types))
    print(file_path)
browse_img_path = ttk.Button(window, text='Browse', command=lambda: browse_file_path_command())
browse_img_path.grid(column=1, row=1)

def convert_file_button_command(img_path):
    reconfirm_img_only_file_name()
    image = Image.open(img_path)
    pdf_path = fd.asksaveasfilename(filetypes=file_types, defaultextension=img_only_file_name+'pdf')
    if pdf_path:
        try:
            with open(file_path, 'wb') as pdf_file:
                pdf_bytes = img2pdf.convert(image.filename)
                file.write(pdf_bytes)
                image.close()
            print('Successfully made pdf file')
        except Exception as e:
            result = msgbox.askretrycancel('Error Saving File!', 'Error Saving File! \nPlease Retry.')
            if result: window.after(100, convert_file_button_command, img_path)
convert_file_button = ttk.Button(window, text='convert file', command=lambda: convert_file_button_command(img_path))
convert_file_button.grid(column=0, row=2)

def save_pdf_command():
    reconfirm_img_only_file_name()
    fd.asksaveasfile(filetypes=file_types, defaultextension=img_only_file_name+'.pdf')
save_pdf = ttk.Button(window, text='save PDF file', command=lambda: save_pdf_command())

window.mainloop()
