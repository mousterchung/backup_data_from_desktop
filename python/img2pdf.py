import img2pdf
from PIL import Image

import os
import tkinter as tk
from tkinter import ttk
from tkinter import fd

root = tk.Tk()
file_types = (('jpeg files', '*.jpg'), ('png files', '*.png'), ('gif files', '*.gif'), ('all files', '*.*'))
'''
file_path = fd.askopenfilename(parent=root, title='select file', filetypes=file_types)
print(file_path)
fd.asksaveasfile(filetypes = file_types, defaultextension = 'default file name')
'''

'''
img_path = 'C:/Users/Admin/Desktop/GfG_images/do_nawab.png' # storing image path
pdf_path = 'C:/Users/Admin/Desktop/GfG_images/file.pdf' # storing pdf path
image = Image.open(img_path) # opening image
pdf_bytes = img2pdf.convert(image.filename) # converting into chunks using img2pdf
'''
'''only_file_name = image.filename.split(os.path.sep)[-1]'''
'''
file = open(pdf_path, 'wb') # opening or creating pdf file
file.write(pdf_bytes) # writing pdf files with chunks
image.close() # closing image file
file.close() # closing pdf file
print('Successfully made pdf file') # output
'''