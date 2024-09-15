import img2pdf
from PIL import Image

import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox

def replace_extension(path):
    return path.replace('.jpg', '').replace('.jpeg', '').replace('.jpe', '').replace('.jfif', '').replace('.png', '').replace('.bmp', '').replace('.jdib', '').replace('.gif', '')

img_file_types = (('image files', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif', '*.png', '*.bmp', '*.jdib', '*.gif')), ('JPEG files', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif')), ('PNG files', '*.png'), ('BMP files', ('*.bmp', '*.jdib')), ('GIF files', '*.gif'), ('PDF files', '*.pdf'), ('all files', '*.*'))
pdf_file_types = (('PDF files', '*.pdf'), ('image files', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif', '*.png', '*.bmp', '*.jdib', '*.gif')), ('JPEG files', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif')), ('PNG files', '*.png'), ('BMP files', ('*.bmp', '*.jdib')), ('GIF files', '*.gif'), ('all files', '*.*'))
img_path = ()
pdf_path = tk.StringVar(window)

window = tk.Tk()
window.title('Image to PDF File Converter')
window.geometry('600x200')
window.resizable(False, False)
window.iconbitmap('./img/favicon.ico')

title_label = ttk.Label(text='Image to PDF File Converter')
title_label.grid(column=0, row=1, columnspan=2)

img_path_entry_frame = ttk.Frame(window)
img_path_entry_frame.grid(column=0, row=1, rowspan=3)

img_path_entry = tk.Listbox(img_path_entry_frame, width=60)
img_path_entry.grid(column=0, row=0)

img_path_entry_scrollbar_vertical = ttk.Scrollbar(img_path_entry_frame, command=img_path_entry.yview, orient=tk.VERTICAL)
img_path_entry_scrollbar_vertical.grid(column=1, row=0, sticky=tk.N+tk.S)

img_path_entry_scrollbar_horizontal = ttk.Scrollbar(img_path_entry_frame, command=img_path_entry.xview, orient=tk.HORIZONTAL)
img_path_entry_scrollbar_horizontal.grid(column=0, row=1, sticky=tk.W+tk.E)

def get_img_only_file_name(img_path):
    img_only_file_name = replace_extension(img_path.split(os.path.sep)[-1])
    return img_only_file_name

pdf_path_entry = ttk.Entry(window, width=40, textvariable=pdf_path)
def browse_pdf_path_command():
    global pdf_path
    pdf_path.set(fd.askdirectory(title=f'Save PDF File `{img_path.split("/")[-1]}`'))
browse_pdf_path = ttk.Button(window, text='Browse PDF File Path', command=lambda: browse_pdf_path_command())
browse_pdf_path.grid(column=1, row=1)

def browse_img_path_command():
    global img_path, folder_count
    img_path = fd.askopenfilenames(parent=window, title='Select Image File', filetypes=img_file_types)
    img_path_entry.delete(0, tk.END)
    img_path_entry.insert(tk.END, *img_path)
    print(img_path)
    folder_count = 1
browse_img_path = ttk.Button(window, text='Browse', command=lambda: browse_img_path_command())
browse_img_path.grid(column=1, row=2)

def convert_file_button_command(img_paths):
    for img_path in img_paths:
        img_only_file_name = get_img_only_file_name(img_path)
        image = Image.open(img_path)
        save_pdf_command(img_path, image=image)
convert_file_button = ttk.Button(window, text='Convert to PDF File', command=lambda: convert_file_button_command(img_path))
convert_file_button.grid(column=1, row=3)

def save_pdf_command(img_path, img_only_file_name=None, image=None):
    global pdf_path
    if type(img_path) in (tuple, list):
        for i in img_path:
            save_pdf_command(i)
    if img_only_file_name is None: img_only_file_name = get_img_only_file_name(img_path)
    if pdf_path:
        try:
            with open(replace_extension(img_path)+'.pdf', 'wb') as pdf_file:
                pdf_bytes = img2pdf.convert(image.filename)
                image.close()
                pdf_file.write(pdf_bytes)
            print(f'Successfully Made PDF File. \n`{img_path.split("/")[-1]}`')
            msgbox.showinfo('Successfully Made PDF File.', f'Successfully Made PDF File. \n`{img_path.split("/")[-1]}`')
        except IOError as e:
            result = msgbox.askretrycancel('Error Saving File!', 'Error Saving File! \nPlease Retry.')
            if result: window.after(100, save_pdf_command, img_path, img_only_file_name, image)
save_pdf = ttk.Button(window, text='Save PDF File', command=lambda: save_pdf_command(img_path))
save_pdf.grid(column=1, row=4)

window.mainloop()
