import pikepdf
import pikepdf.settings

import os
import io
import zlib
from datetime import datetime as dt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox

import favicon

PDF_FILE_TYPES = (('PDF Files', '*.pdf'), 
                  ('All Files', '*.*'  ))
PDF_FILE_SIZES = {# ISO A 國際標準 A
                  'A0' :                            (2384, 3370), 
                  'A1' :                            (1684, 2384), 
                  'A2' :                            (1191, 1684), 
                  'A3' :                            ( 842, 1191), 
                  'A4' :                            ( 595,  842), 
                  'A5' :                            ( 420,  595), 
                  'A6' :                            ( 298,  420), 
                  'A7' :                            ( 210,  298), 
                  'A8' :                            ( 147,  210), 
                  'A9' :                            ( 105,  147), 
                  'A10':                            (  74,  105), 
                  
                  # ISO B 國際標準 B
                  'B0' :                            (2835, 4008), 
                  'B1' :                            (2004, 2835), 
                  'B1+':                            (2041, 2891), 
                  'B2' :                            (1417, 2004), 
                  'B2+':                            (1474, 2041), 
                  'B3' :                            (1001, 1417), 
                  'B4' :                            ( 709, 1001), 
                  'B5' :                            ( 499,  709), 
                  'B6' :                            ( 354,  499), 
                  'B7' :                            ( 249,  354), 
                  'B8' :                            ( 176,  249), 
                  'B9' :                            ( 125,  176), 
                  'B10':                            (  88,  125), 
                  
                  # ISO C 國際標準信封
                  'C0' :                            (2599, 3677), 
                  'C1' :                            (1837, 2599), 
                  'C2' :                            (1298, 1837), 
                  'C3' :                            ( 918, 1298), 
                  'C4' :                            ( 649,  918), 
                  'C5' :                            ( 459,  649), 
                  'C6' :                            ( 323,  459), 
                  'C7' :                            ( 230,  323), 
                  'C8' :                            ( 162,  230), 
                  'C9' :                            ( 113,  162), 
                  'C10':                            (  79,  113), 
                  
                  # North American 北美標準
                  'NA_LETTER'      :                ( 612,  791), 
                  'NA_LEGAL'       :                ( 612, 1009), 
                  'NA_JUNIOR_LEGAL':                ( 360,  575), 
                  'NA_TABLOID'     :                ( 791, 1225), 
                  'NA_LEDGER'      :                ( 791, 1225), 
                  'GOV_LETTER'     :                ( 576,  756), 
                  
                  # ANSI 美國國家標準
                  'ANSI_A'              :           ( 612,  791), # ═╦═same
                  'ANSI_LETTER'         :           ( 612,  791), # ═╝
                  'ANSI_B'              :           ( 791, 1225), # ═╗
                  'ANSI_LEDGER'         :           ( 791, 1225), # ═╬═same
                  'ANSI_TABLOID'        :           ( 791, 1225), # ═╝
                  'ANSI_C'              :           (1225, 1585), 
                  'ANSI_D'              :           (1585, 2449), 
                  'ANSI_E'              :           (2449, 3169), 
                  
                  # Architectural 建築繪圖
                  'ARCH_A'              :           ( 649,  865), 
                  'ARCH_B'              :           ( 865, 1295), 
                  'ARCH_C'              :           (1295, 1729), 
                  'ARCH_D'              :           (1729, 2591), 
                  'ARCH_E'              :           (2591, 3455), 
                  'ARCH_E1'             :           (2160, 3025), 
                  'ARCH_E2'             :           (1871, 2735), 
                  'ARCH_E3'             :           (1945, 2809), 
                  
                  # US Announcement Envelope 美規信封
                  'ANNOUNCEMENT_A2'     :           ( 315,  414), # A-2
                  'ANNOUNCEMENT_A6'     :           ( 342,  468), # A-6
                  'ANNOUNCEMENT_A7'     :           ( 378,  522), # A-7
                  'ANNOUNCEMENT_A8'     :           ( 396,  585), # A-8
                  'ANNOUNCEMENT_A10'    :           ( 432,  684), # A-10
                  'ANNOUNCEMENT_ASLIM'  :           ( 279,  639), # A-Slim
                  
                  # US Baronial Envelope 美規信封
                  'BARONIAL_4'          :           ( 261,  369), 
                  'BARONIAL_5_5'        :           ( 315,  414), # 5.5
                  'BARONIAL_6'          :           ( 342,  468), 
                  'BARONIAL_LEE'        :           ( 378,  522), 
                  
                  # US Booklet Envelope 美規信封
                  'BOOKLET_3'           :           ( 342,  468), 
                  'BOOKLET_4_5'         :           ( 396,  540), # 4.5
                  'BOOKLET_6'           :           ( 414,  639), 
                  'BOOKLET_6_5'         :           ( 432,  648), # 6.5
                  'BOOKLET_6_625'       :           ( 432,  684), # 6.625
                  'BOOKLET_6_75'        :           ( 468,  684), # 6.75
                  'BOOKLET_7_25'        :           ( 504,  720), # 7.25
                  'BOOKLET_7_5'         :           ( 540,  756), # 7.5
                  'BOOKLET_9'           :           ( 630,  828), 
                  'BOOKLET_9_5'         :           ( 648,  864), # 9.5
                  'BOOKLET_10'          :           ( 684,  909), 
                  'BOOKLET_13'          :           ( 720,  936), 
                  
                  # US Catalog Envelope 美規信封
                  'CATALOG_1'           :           ( 432,  648), 
                  'CATALOG_1_75'        :           ( 468,  684), # 1.75
                  'CATALOG_3'           :           ( 504,  720), 
                  'CATALOG_6'           :           ( 540,  756), 
                  'CATALOG_9_75'        :           ( 630,  810), # 9.75
                  'CATALOG_10_5'        :           ( 648,  864), # 10.5
                  'CATALOG_12_5'        :           ( 684,  900), # 12.5
                  'CATALOG_13_5'        :           ( 720,  936), # 13.5
                  'CATALOG_14_5'        :           ( 828, 1044), # 14.5
                  'CATALOG_15_5'        :           ( 864, 1116), # 15.5
                  
                  # US Commercial/Official Envelope 美規信封
                  'COMMERCIAL_6_25'     :           ( 252,  432), # 6.25
                  'COMMERCIAL_6_75'     :           ( 261,  468), # 6.75
                  'OFFICIAL_7'          :           ( 270,  486), 
                  'OFFICIAL_7_75'       :           ( 279,  540), # 7.75
                  'OFFICIAL_8_625'      :           ( 261,  621), # 8.625
                  'OFFICIAL_9'          :           ( 279,  639), 
                  'OFFICIAL_10'         :           ( 297,  684), 
                  'OFFICIAL_11'         :           ( 324,  747), 
                  'OFFICIAL_12'         :           ( 342,  792), 
                  'OFFICIAL_14'         :           ( 360,  828), 
                  
                  # US Sqare Envelope 美規方形信封
                  'SQARE_6'             :           ( 432,  432), 
                  'SQARE_6_5'           :           ( 468,  468), # 6.5
                  'SQARE_7'             :           ( 504,  504), 
                  'SQARE_7_5'           :           ( 540,  540), # 7.5
                  'SQARE_8'             :           ( 579,  579), 
                  'SQARE_8_5'           :           ( 612,  612), # 8.5
                  'SQARE_9'             :           ( 648,  648), 
                  'SQARE_9_5'           :           ( 684,  684), # 9.5
                  
                  # ISO RA 印刷原紙
                  'RA0'                 :           (2438, 3458), 
                  'RA1'                 :           (1729, 2438), 
                  'RA2'                 :           (1219, 1729), 
                  'RA3'                 :           ( 865, 1219), 
                  'RA4'                 :           ( 609,  865), 
                  
                  # ISO SRA 印刷原紙
                  'SRA0'                :           (2551, 3628), 
                  'SRA1'                :           (1814, 2551), 
                  'SRA2'                :           (1276, 1814), 
                  'SRA3'                :           ( 907, 1276), 
                  'SRA4'                :           ( 638,  907), 
                  
                  # Business Card 商務名片
                  'BUSINESS_CARD_JP'    :           ( 156,  258), # Japan
                  'BUSINESS_CARD_UK'    :           ( 156,  241), 
                  'BUSINESS_CARD_US'    :           ( 145,  252), 
                  
                  # Miscellaneous 特殊規格
                  '1_3_A4'              :           ( 281,  595), # 1/3
                  'A4_SQUARE'           :           ( 595,  595), 
                  'CD_CASE_INSERT'      :           ( 340,  340), 
                  'GUTENBERG_BIBLE'     :           ( 794, 1128), 
                  'A_FORMAT_PAPERBACK'  :           ( 312,  505), 
                  'B_FORMAT_PAPERBACK'  :           ( 369,  561), 
                  'BILLBOARD_48_SHEET'  :           (8640,17280), 
                  
                  # US Press Sheets 美規印刷大張紙
                  '11x17'               :           ( 792, 1224), 
                  '12x18'               :           ( 864, 1296), 
                  '17x22'               :           (1224, 1584), 
                  '19x25'               :           (1368, 1800), 
                  '20x26'               :           (1440, 1872), 
                  '23x29'               :           (1656, 2088), 
                  '23x35'               :           (1656, 2520), 
                  '24x36'               :           (1728, 2592), 
                  '25x38'               :           (1800, 2736), 
                  '26x40'               :           (1872, 2880), 
                  '28x40'               :           (2016, 2880), 
                  '35x45'               :           (2520, 3240), 
                  '38x50'               :           (2736, 3600), 
                  }
PDF_FILE_SIZES_NAME_TO_KEY = {'## ISO A 國際標準 A': '', 
                              'A0': 'A0', 
                              'A1': 'A1', 
                              'A2': 'A2', 
                              'A3': 'A3', 
                              'A4': 'A4', 
                              'A5': 'A5', 
                              'A6': 'A6', 
                              'A7': 'A7', 
                              'A8': 'A8', 
                              'A9': 'A9', 
                              'A10': 'A10', 
                              
                              '## ISO B 國際標準 B': '', 
                              'B0': 'B0', 
                              'B1': 'B1', 
                              'B1+': 'B1+', 
                              'B2': 'B2', 
                              'B2+': 'B2+', 
                              'B3': 'B3', 
                              'B4': 'B4', 
                              'B5': 'B5', 
                              'B6': 'B6', 
                              'B7': 'B7', 
                              'B8': 'B8', 
                              'B9': 'B9', 
                              'B10': 'B10', 
                              
                              '## ISO C 國際標準信封': '', 
                              'C0': 'C0', 
                              'C1': 'C1', 
                              'C2': 'C2', 
                              'C3': 'C3', 
                              'C4': 'C4', 
                              'C5': 'C5', 
                              'C6': 'C6', 
                              'C7': 'C7', 
                              'C8': 'C8', 
                              'C9': 'C9', 
                              'C10': 'C10', 
                              
                              '## North American 北美標準': '', 
                              'North American Letter': 'NA_LETTER', 
                              'North American Legal': 'NA_LEGAL', 
                              'North American Junior Legal': 'NA_JUNIOR_LEGAL', 
                              'North American Tabloid': 'NA_TABLOID', 
                              'North American Ledger': 'NA_LEDGER', 
                              'Government-Letter': 'GOV_LETTER', 
                              
                              '## ANSI 美國國家標準': '', 
                              'ANSI A (Letter)': 'ANSI_A',           # ═╦═same
                              'ANSI Letter (ANSI A)': 'ANSI_LETTER', # ═╝
                              'ANSI B (Ledger, Tabloid)': 'ANSI_B',   # ═╗
                              'ANSI Ledger (ANSI B)': 'ANSI_LEDGER',  # ═╬═same
                              'ANSI Tabloid (ANSI B': 'ANSI_TABLOID', # ═╝
                              'ANSI C': 'ANSI_C', 
                              'ANSI D': 'ANSI_D', 
                              'ANSI E': 'ANSI_E', 
                              
                              '## Architectural 建築繪圖': '', 
                              'Arch A': 'ARCH_A', 
                              'Arch B': 'ARCH_B', 
                              'Arch C': 'ARCH_C', 
                              'Arch D': 'ARCH_D', 
                              'Arch E': 'ARCH_E', 
                              'Arch E1': 'ARCH_E1', 
                              'Arch E2': 'ARCH_E2', 
                              'Arch E3': 'ARCH_E3', 
                              
                              '## US Announcement Envelope 美規信封': '', 
                              'A-2 Envelope': 'ANNOUNCEMENT_A2', 
                              'A-6 Envelope': 'ANNOUNCEMENT_A6', 
                              'A-7 Envelope': 'ANNOUNCEMENT_A7', 
                              'A-8 Envelope': 'ANNOUNCEMENT_A8', 
                              'A-10 Envelope': 'ANNOUNCEMENT_A10', 
                              'A-Slim Envelope': 'ANNOUNCEMENT_ASLIM', 
                              
                              '## US Baronial Envelope 美規信封': '', 
                              '4 Baronial Envelope': 'BARONIAL_4', 
                              '5.5 Baronial Envelope': 'BARONIAL_5_5', 
                              '6 Baronial Envelope': 'BARONIAL_6', 
                              'Lee Envelope': 'BARONIAL_LEE', 
                              
                              '## US Booklet Envelope 美規信封': '', 
                              '3 Booklet Envelope': 'BOOKLET_3', 
                              '4.5 Booklet Envelope': 'BOOKLET_4_5', 
                              '6 Booklet Envelope': 'BOOKLET_6', 
                              '6.5 Booklet Envelope': 'BOOKLET_6_5', 
                              '6.625 Booklet Envelope': 'BOOKLET_6_625', 
                              '6.75 Booklet Envelope': 'BOOKLET_6_75', 
                              '7.25 Booklet Envelope': 'BOOKLET_7_25', 
                              '7.5 Booklet Envelope': 'BOOKLET_7_5', 
                              '9 Booklet Envelope': 'BOOKLET_9', 
                              '9.5 Booklet Envelope': 'BOOKLET_9_5', 
                              '10 Booklet Envelope': 'BOOKLET_10', 
                              '13 Booklet Envelope': 'BOOKLET_13', 
                              
                              '## US Catalog Envelope 美規信封': '', 
                              '1 Catalog Envelope': 'CATALOG_1', 
                              '1.75 Catalog Envelope': 'CATALOG_1_75', 
                              '3 Catalog Envelope': 'CATALOG_3', 
                              '6 Catalog Envelope': 'CATALOG_6', 
                              '9.75 Catalog Envelope': 'CATALOG_9_75', 
                              '10.5 Catalog Envelope': 'CATALOG_10_5', 
                              '12.5 Catalog Envelope': 'CATALOG_12_5', 
                              '13.5 Catalog Envelope': 'CATALOG_13_5', 
                              '14.5 Catalog Envelope': 'CATALOG_14_5', 
                              '15.5 Catalog Envelope': 'CATALOG_15_5', 
                              
                              '## US Commercial/Official Envelope 美規信封': '', 
                              '6.25 Commercial Envelope': 'COMMERCIAL_6_25', 
                              '6.75 Commercial Envelope': 'COMMERCIAL_6_75', 
                              '7 Official Envelope': 'OFFICIAL_7', 
                              '7.75 Official Envelope': 'OFFICIAL_7_75', 
                              '8.625 Official Envelope': 'OFFICIAL_8_625', 
                              '9 Official Envelope': 'OFFICIAL_9', 
                              '10 Official Envelope': 'OFFICIAL_10', 
                              '11 Official Envelope': 'OFFICIAL_11', 
                              '12 Official Envelope': 'OFFICIAL_12', 
                              '14 Official Envelope': 'OFFICIAL_14', 
                              
                              '## US Sqare Envelope 美規方形信封': '', 
                              '6 Sqare Envelope': 'SQARE_6', 
                              '6.5 Sqare Envelope': 'SQARE_6_5', 
                              '7 Sqare Envelope': 'SQARE_7', 
                              '7.5 Sqare Envelope': 'SQARE_7_5', 
                              '8 Sqare Envelope': 'SQARE_8', 
                              '8.5 Sqare Envelope': 'SQARE_8_5', 
                              '9 Sqare Envelope': 'SQARE_9', 
                              '9.5 Sqare Envelope': 'SQARE_9_5', 
                              
                              '## ISO RA 印刷原紙': '', 
                              'RA0': 'RA0', 
                              'RA1': 'RA1', 
                              'RA2': 'RA2', 
                              'RA3': 'RA3', 
                              'RA4': 'RA4', 
                              
                              '## ISO SRA 印刷原紙': '', 
                              'SRA0': 'SRA0', 
                              'SRA1': 'SRA1', 
                              'SRA2': 'SRA2', 
                              'SRA3': 'SRA3', 
                              'SRA4': 'SRA4', 
                              
                              '## Business Card 商務名片': '', 
                              'Business Card (Japan)': 'BUSINESS_CARD_JP', 
                              'Business Card (UK)': 'BUSINESS_CARD_UK', 
                              'Business Card (US)': 'BUSINESS_CARD_US', 
                              
                              '## Miscellaneous 特殊規格': '', 
                              '1/3 A4': '1_3_A4', 
                              'A4 Sqare': 'A4_SQUARE', 
                              'CD Case Insert': 'CD_CASE_INSERT', 
                              'Gutenberg Bible': 'GUTENBERG_BIBLE', 
                              'A Format Paperback': 'A_FORMAT_PAPERBACK', 
                              'B Format Paperback': 'B_FORMAT_PAPERBACK', 
                              '48 Sheet Billboard': 'BILLBOARD_48_SHEET', 
                              
                              '## US Press Sheets 美規印刷大張紙': '', 
                              '11 x 17': '11x17', 
                              '12 x 18': '12x18', 
                              '17 x 22': '17x22', 
                              '19 x 25': '19x25', 
                              '20 x 26': '20x26', 
                              '23 x 29': '23x29', 
                              '23 x 35': '23x35', 
                              '24 x 36': '24x36', 
                              '25 x 38': '25x38', 
                              '26 x 40': '26x40', 
                              '28 x 40': '28x40', 
                              '35 x 45': '35x45', 
                              '38 x 50': '38x50', 
                              }

# <function class="assert list">
def assert_list(data):
    # print('Running  `assert_list()`')
    if isinstance(data, str):
        data = [data]
    elif isinstance(data, tuple):
        data = list(data)
    return data
    # print('Finished `assert_list()`')

def flat_list(data, base=None):
    # print('Running  `flat_list()`')
    assert_list(data)
    result = [] if base is None else base
    for i in data:
        if isinstance(i, list):
            result = flat_list(i, result)
        else:
            result.append(i)
    return result
    # print('Finished `flat_list()`')

def assert_file_extension(filename, extension=''):
    # print('Running  `assert_file_extension()`')
    if isinstance(filename, str):
        return filename if filename.lower().endswith(extionsion) else filename+extension
    elif isinstance(filename, tk.StringVar) or isinstance(filename, ttk.Combobox):
        filename.set(filename.get() if filename.get().lower().endswith(extension) else filename.get()+extension)
    # print('Finished `assert_file_extension()`')
# </function>

# <function class="cmd browse path">
def browse_dest_path_cmd(dest_path_var):
    # print('Running  `browse_dest_path_cmd()`')
    dest_path_var.set(fd.askdirectory(title='Browse Destination Path'))
    # print('Finished `browse_dest_path_cmd()`')

def browse_one_source_file_cmd(source_file_var, dest_path_var=None):
    # print('Running  `browse_one_source_file_cmd()`')
    source_file_var.set(fd.askopenfilename(title='Browse Source File', filetypes=PDF_FILE_TYPES, initialdir=dest_path_var))
    # print('Finished `browse_one_source_file_cmd()`')

def browse_source_files_cmd(listbox_var, dest_path_var=None):
    # print('Running  `browse_source_files_cmd()`')
    file_paths = fd.askopenfilenames(parent=window, title='Select Source Files', filetypes=PDF_FILE_TYPES, initialdir=dest_path_var)
    listbox_var.insert(tk.END, *file_paths)
    # print('Finished `browse_source_files_cmd()`')

def remove_source_file_item_cmd(listbox_var):
    # print('Running  `remove_source_file_item_cmd()`')
    try:
        listbox_var.delete(listbox_var.curselection()[0])
    except IndexError:
        print('No item selected to delete. ')
    # print('Finished `remove_source_file_item_cmd()`')

def clear_source_file_list_cmd(listbox_var):
    # print('Running  `clear_source_file_list_cmd()`')
    listbox_var.delete(0, tk.END)
    # print('Finished `clear_source_file_list_cmd()`')

def dest_filename_same_as_source_filename_checkbutton_cmd(same_as_var, dest_filename_var, source_path_var):
    # print('Running  `dest_filename_same_as_source_filename_checkbutton_cmd()`')
    same_as = same_as_var.get()
    if same_as:
        dest_filename_var.configure(state=tk.DISABLED)
        dest_filename_var.set(os.path.split(source_path_var.get())[1])
    else:
        dest_filename_var.configure(state=tk.NORMAL)
    # print('Finished `dest_filename_same_as_source_filename_checkbutton_cmd()`')

def range_add_cmd(range_start_var, range_end_var, range_listbox_var, flag=False):
    # print('Running  `range_add_cmd()`')
    if flag:
        split_range_listbox_onchange_cmd(split_into_one_page)
    
    if isinstance(range_start_var, int) or isinstance(range_end_var, int):
        range_listbox_var.insert(tk.END, (range_start_var, '~', range_end_var))
    else:
        range_listbox_var.insert(tk.END, (int(range_start_var.get()), '~', int(range_end_var.get())))
    # print('Finished `range_add_cmd()`')

def range_remove_cmd(listbox_var, flag=False):
    # print('Running  `range_remove_cmd()`')
    if flag:
        split_range_listbox_onchange_cmd(split_into_one_page)
    
    try:
        listbox_var.delete(listbox_var.curselection()[0])
    except IndexError:
        print('No item selected to delete. ')
    # print('Finished `range_remove_cmd()`')

def range_clear_cmd(listbox_var,flag=False):
    # print('Running  `clear_source_file_list_cmd()`')
    if flag:
        split_range_listbox_onchange_cmd(split_into_one_page)
    
    listbox_var.delete(0, tk.END)
    # print('Finished `clear_source_file_list_cmd()`')

def combobox_onselected_cmd(combobox_var): 
    # print('Running  `combobox_onselected_cmd()`')
    if '##' in combobox_var.get():
        combobox_var.set('')
    # print('Finished `combobox_onselected_cmd()`')

def combobox_oninput_cmd(combobox_var, keysym): 
    # print('Running  `combobox_onselected_cmd()`')
    if keysym in ('Return', 'Tab', 'Escape', 'Insert', 'Up', 'Down', 'Left', 'Right', 'Prior', 'Next', 'Home', 'End', 'Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Alt_L', 'Alt_R', 'Win_L', 'Win_R', 'Meta_L', 'Meta_R', 'Super_L', 'Super_R', 'Hyper_L', 'Hyper_R', 'Menu', 'App', 'Caps_Lock', 'Num_Lock', 'Scroll_Lock', 'KP_Enter', 'KP_Tab', 'Print', 'Pause', 'Break', 'Cancel', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 'F32', 'F33', 'F34', 'F35'): 
        return
    
    typed = combobox_var.get()
    
    if typed == '':
        values_data = list(PDF_FILE_SIZES_NAME_TO_KEY.keys())
    else:
        values_data = [i for i in list(PDF_FILE_SIZES_NAME_TO_KEY.keys()) if i.lower().startswith(typed.lower())]
    combobox_var.configure(values=values_data)
# </function>

# <function class="cmd">
def rotate_and_save_cmd(source_path_var, angle_var, dest_path_var, dest_filename_var=None):
    # print('Running  `rotate_and_save_cmd()`')
    if dest_filename_var.get() == '':
        dest_filename_var.set(dt.now().isoformat().replace('-', '').replace(':', '').replace('+', '').replace('T', '').split('.')[0])
    
    assert_file_extension(dest_filename_var, '.pdf')
    os.chdir(dest_path_var.get())
    pdf_rotate(source_path_var.get(), int(angle_var.get())).save(dest_filename_var.get())
    
    msg_content = f'Successfully rotated below file by {angle_var.get()} degrees: '
    msg_content += f'\n\t`{source_path_var.get()}`'
    msgbox.showinfo('Successfully', msg_content)
    # print('Finished `rotate_and_save_cmd()`')

def merge_and_save_cmd(listbox_var, dest_path_var, dest_filename_var):
    # print('Running  `merge_and_save_cmd()`')
    if dest_filename_var.get() == '':
        dest_filename_var.set(dt.now().isoformat().replace('-', '').replace(':', '').replace('+', '').replace('T', '').split('.')[0])
    
    assert_file_extension(dest_filename_var, '.pdf')
    os.chdir(dest_path_var.get())
    pdf_merge(assert_list(listbox_var.get(0, tk.END))).save(dest_filename_var.get())
    
    msg_content = f'Successfully merged below files to `{dest_filename_var.get()}`: '
    for i in listbox_var.get(0, tk.END):
        msg_content += f'\n\t`{i}`'
    msgbox.showinfo('Successfully', msg_content)
    # print('Finished `merge_and_save_cmd()`')

def split_source_path_changed_cmd(source_path_var, range_start_var, range_end_var):
    # print('Running  `split_source_path_changed_cmd()`')
    with pikepdf.Pdf.open(source_path_var.get()) as f:
        range_start_var.configure(to=len(f.pages))
        range_end_var.configure(to=len(f.pages))
    # print('Finished `split_source_path_changed_cmd()`')

def split_into_one_page_cmd(into_one_page_var, source_path_var, range_listbox_var):
    # print('Running  `split_into_one_page_cmd()`')
    if into_one_page_var.get():
        range_clear_cmd(range_listbox_var)
        
        with pikepdf.Pdf.open(source_path_var.get()) as f:
            for i in range(1, len(f.pages)+1):
                range_add_cmd(i, i, range_listbox_var)
    # print('Finished `split_into_one_page_cmd()`')

def split_range_listbox_onchange_cmd(into_one_page_var):
    # print('Running  `split_range_listbox_onchange_cmd()`')
    into_one_page_var.set(False)
    # print('Finished `split_range_listbox_onchange_cmd()`')

def split_and_save_cmd(source_path_var, range_listbox_var, dest_path_var, dest_filename_var, dest_filename_numbering_prefix_var, dest_filename_numbering_postfix_var, dest_filename_numbering_length_var, dest_filename_numbering_start_var):
    # print('Running  `split_and_save_cmd()`')
    if dest_filename_var.get() == '':
        dest_filename_var.set(dt.now().isoformat().replace('-', '').replace(':', '').replace('+', '').replace('T', '').split('.')[0])
    
    assert_file_extension(dest_filename_var, '.pdf')
    os.chdir(dest_path_var.get())
    dest_files = pdf_split(source_path_var.get(), assert_list(range_listbox_var.get(0, tk.END)))
    for i, f in enumerate(dest_files):
        n = i + int(dest_filename_numbering_start_var.get())
        # f.save(f'{dest_filename_var.get().split(".")[0]}{"" if dest_filename_numbering_prefix_var.get()=="" else dest_filename_numbering_prefix_var.get()}{n:0>{int(dest_filename_numbering_length_var.get())}}{"" if dest_filename_numbering_postfix_var.get()=="" else dest_filename_numbering_postfix_var.get()}.pdf')
        f.save(f'{dest_filename_var.get().split(".")[0]}{dest_filename_numbering_prefix_var.get()}{n:0>{int(dest_filename_numbering_length_var.get())}}{dest_filename_numbering_postfix_var.get()}.pdf')
    
    msg_content = f'Successfully splited file `{source_path_var.get()}` into below pieces: '
    for i, (start, *tmp, end) in enumerate(range_listbox_var.get(0, tk.END)):
        n = i + int(dest_filename_numbering_start_var.get())
        msg_content += f'\n\t{n:0>{int(dest_filename_numbering_length_var.get())}}: P.{start}~{end}'
    msgbox.showinfo('Successfully', msg_content)
    # print('Finished `split_and_save_cmd()`')

def resize_and_save_cmd(source_path_var, size_var, orientation_var, dest_path_var, dest_filename_var):
    # print('Running  `resize_and_save_cmd()`')
    if dest_filename_var.get() == '':
        dest_filename_var.set(dt.now().isoformat().replace('-', '').replace(':', '').replace('+', '').replace('T', '').split('.')[0])
    
    assert_file_extension(dest_filename_var, '.pdf')
    os.chdir(dest_path_var.get())
    size = PDF_FILE_SIZES[PDF_FILE_SIZES_NAME_TO_KEY[size_var.get()]]
    if orientation_var.get() == 'Landscape': 
        size = (size[1], size[0])
    pdf_resize(source_path_var.get(), size).save(dest_filename_var.get())
    
    msg_content = f'Successfully resized below file into {size_var.get()} {orientation_var.get()}: '
    msg_content += f'\n\t`{source_path_var.get()}`'
    msgbox.showinfo('Successfully', msg_content)
    # print('Finished `resize_and_save_cmd()`')

def compress_and_save_cmd(source_path_var, dest_path_var, dest_filename_var):
    print('Running  `compress_and_save_cmd()`')
    
    if dest_filename_var.get() == '':
        dest_filename_var.set(dt.now().isoformat().replace('-', '').replace(':', '').replace('+', '').replace('T', '').split('.')[0])
    
    assert_file_extension(dest_filename_var, '.pdf')
    os.chdir(dest_path_var.get())
    pdf_compress(source_path_var.get()).save(dest_filename_var.get())
    
    msg_content = f'Successfully compressed below file: '
    msg_content += f'\n\t`{source_path_var.get()}`'
    msgbox.showinfo('Successfully', msg_content)
    
    print('Finished `compress_and_save_cmd()`')
# </function>

# <function class="pdf-transform">
def pdf_rotate(source_file, angle):
    # print('Running  `pdf_rotate()`')
    result = pikepdf.Pdf.new()
    with pikepdf.Pdf.open(source_file) as f:
        result.pages.extend(f.pages)
        for page in result.pages:
            page.rotate(angle, relative=False)
    return result
    # print('Finished `pdf_rotate()`')

def pdf_merge(source_files):
    # print('Running  `pdf_merge()`')
    result = pikepdf.Pdf.new()
    for i in source_files:
        with pikepdf.Pdf.open(i) as f:
            result.pages.extend(f.pages)
    return result
    # print('Finished `pdf_merge()`')

def pdf_split(source_file, split_ranges):
    # print('Running  `pdf_split()`')
    result = []
    with pikepdf.Pdf.open(source_file) as f:
        for start, *tmp, end in split_ranges:
            result_pdf = pikepdf.Pdf.new()
            result_pdf.pages.extend(f.pages[start-1:end])
            result.append(result_pdf)
    return result
    # print('Finished `pdf_split()`')

def pdf_resize(source_file, size):
    # print('Running  `pdf_resize()`')
    result = pikepdf.Pdf.new()
    with pikepdf.Pdf.open(source_file) as f:
        for page in f.pages:
            new_page = result.add_blank_page(page_size=size)
            
            # shrink=True   auto shrink(smaller) when content is too big
            # expand=True   auto expand(bigger ) when content is too small
            new_page.add_overlay(page, shrink=True, expand=True)
    return result
    # print('Finished `pdf_resize()`')

def pdf_compress(source_file):
    print('Running  `pdf_compress()`')
    
    result = io.BytesIO()
    try:
        pikepdf.settings.set_flate_compression_level(9)
        
        with pikepdf.Pdf.open(source_file) as f:
            try:
                f.save(result, object_stream_mode=pikepdf.ObjectStreamMode.generate, linearize=True)
            except AttributeError:
                try:
                    f.save(result, object_stream_mode=pikepdf.ObjectStreamMode.all, linearize=True)
                finally:
                    pass
            finally:
                result.seek(0)
    finally:
        pikepdf.settings.set_flate_compression_level(zlib.Z_DEFAULT_COMPRESSION)
    return pikepdf.Pdf.open(result)
    
    print('Finished `pdf_compress()`')
# </function>

# <root>
window = tk.Tk()
window.title('PDF Tools')
window.geometry('800x600')
# window.geometry('1200x900')
# window.resizable(False, False)
favicon.make_favicon(window)
window.iconphoto(True, favicon.FAVICON_TK)

tabs = ttk.Notebook(window)

#   <rotate>
rotate_tab = tk.Frame()

rotate_dest_path_label = ttk.Label(rotate_tab, text='Destination Path: ')
rotate_dest_path_label.grid(column=0, row=0, sticky=tk.E)

rotate_dest_path = ttk.Combobox(rotate_tab, width=60)
rotate_dest_path.grid(column=1, row=0)

rotate_browse_dest_path_btn = ttk.Button(rotate_tab, text='Browse', command=lambda: browse_dest_path_cmd(rotate_dest_path))
rotate_browse_dest_path_btn.grid(column=2, row=0)

rotate_dest_filename_label = ttk.Label(rotate_tab, text='Destination File Name: ')
rotate_dest_filename_label.grid(column=0, row=1, sticky=tk.E)

rotate_dest_filename = ttk.Combobox(rotate_tab, width=60)
rotate_dest_filename.grid(column=1, row=1)

rotate_dest_filename_same_as_source_filename = tk.BooleanVar(rotate_tab)
rotate_dest_filename_same_as_source_filename_checkbutton = ttk.Checkbutton(rotate_tab, text='Same as Source', variable=rotate_dest_filename_same_as_source_filename, onvalue=True, offvalue=False, command=lambda: dest_filename_same_as_source_filename_checkbutton_cmd(rotate_dest_filename_same_as_source_filename, rotate_dest_filename, rotate_source_path))
rotate_dest_filename_same_as_source_filename_checkbutton.grid(column=2, row=1)

rotate_source_path_label = ttk.Label(rotate_tab, text='Source File: ')
rotate_source_path_label.grid(column=0, row=2, sticky=tk.E)

rotate_source_path = ttk.Combobox(rotate_tab, width=60)
rotate_source_path.grid(column=1, row=2)

rotate_browse_source_path_btn = ttk.Button(rotate_tab, text='Browse', command=lambda: browse_one_source_file_cmd(rotate_source_path))
rotate_browse_source_path_btn.grid(column=2, row=2)

rotate_angle_label = ttk.Label(rotate_tab, text='Rotate Angle (Clockwise): ')
rotate_angle_label.grid(column=0, row=3, sticky=tk.E)

rotate_angle = ttk.Spinbox(rotate_tab, width=5, values=(-270, -180, -90, 0, 90, 180, 270))
rotate_angle.set(0)
rotate_angle.grid(column=1, row=3, sticky=tk.W)

rotate_and_save_btn = ttk.Button(rotate_tab, text='Rotate and Save', command=lambda: rotate_and_save_cmd(rotate_source_path, rotate_angle, rotate_dest_path, rotate_dest_filename))
rotate_and_save_btn.grid(column=2, row=3)

tabs.add(rotate_tab, text="Rotate")
#   </rotate>

#   <merge>
merge_tab = tk.Frame()

merge_dest_path_label = ttk.Label(merge_tab, text='Destination Path: ')
merge_dest_path_label.grid(column=0, row=0, sticky=tk.E)

merge_dest_path = ttk.Combobox(merge_tab, width=60)
merge_dest_path.grid(column=1, row=0)

merge_browse_dest_path_btn = ttk.Button(merge_tab, text='Browse', command=lambda: browse_dest_path_cmd(merge_dest_path))
merge_browse_dest_path_btn.grid(column=2, row=0)

merge_dest_filename_label = ttk.Label(merge_tab, text='Destination File Name: ')
merge_dest_filename_label.grid(column=0, row=1, sticky=tk.E)


merge_dest_filename = ttk.Combobox(merge_tab, width=60)
merge_dest_filename.grid(column=1, row=1)

merge_dest_path_label = ttk.Label(merge_tab, text='Source Files: ')
merge_dest_path_label.grid(column=0, row=2, rowspan=3, sticky=tk.E+tk.N)

#       <merge-inner>
merge_source_files_listbox_frame = tk.Frame(merge_tab)

merge_source_files_listbox = tk.Listbox(merge_source_files_listbox_frame, width=60)
merge_source_files_listbox.grid(column=0, row=0)

merge_source_files_listbox_yscroll = ttk.Scrollbar(merge_source_files_listbox_frame, command=merge_source_files_listbox.yview, orient=tk.VERTICAL)
merge_source_files_listbox_yscroll.grid(column=1, row=0, sticky=tk.N+tk.S)

merge_source_files_listbox_xscroll = ttk.Scrollbar(merge_source_files_listbox_frame, command=merge_source_files_listbox.xview, orient=tk.HORIZONTAL)
merge_source_files_listbox_xscroll.grid(column=0, row=1, sticky=tk.W+tk.E)

merge_source_files_listbox_frame.grid(column=1, row=2, rowspan=4)
#       </merge-inner>

merge_browse_source_files_btn = ttk.Button(merge_tab, text='Browse (Add)', command=lambda: browse_source_files_cmd(merge_source_files_listbox))
merge_browse_source_files_btn.grid(column=2, row=2)

merge_remove_source_file_item_btn = ttk.Button(merge_tab, text='Remove', command=lambda: remove_source_file_item_cmd(merge_source_files_listbox))
merge_remove_source_file_item_btn.grid(column=2, row=3)

merge_clear_source_file_list_btn = ttk.Button(merge_tab, text='Clear', command=lambda: clear_source_file_list_cmd(merge_source_files_listbox))
merge_clear_source_file_list_btn.grid(column=2, row=4)

merge_and_save_btn = ttk.Button(merge_tab, text='Merge and Save', command=lambda: merge_and_save_cmd(merge_source_files_listbox, merge_dest_path, merge_dest_filename))
merge_and_save_btn.grid(column=2, row=5)

tabs.add(merge_tab, text="Merge")
#   </merge>

#   <split>
split_tab = tk.Frame()

split_dest_path_label = ttk.Label(split_tab, text='Destination Path: ')
split_dest_path_label.grid(column=0, row=0, sticky=tk.E)

split_dest_path = ttk.Combobox(split_tab, width=60)
split_dest_path.grid(column=1, row=0, columnspan=4)

split_browse_dest_path_btn = ttk.Button(split_tab, text='Browse', command=lambda: browse_dest_path_cmd(split_dest_path))
split_browse_dest_path_btn.grid(column=5, row=0)

split_dest_filename_label = ttk.Label(split_tab, text='Destination File Name: ')
split_dest_filename_label.grid(column=0, row=1, sticky=tk.E)

split_dest_filename = ttk.Combobox(split_tab, width=60)
split_dest_filename.grid(column=1, row=1, columnspan=4)

split_dest_filename_same_as_source_filename = tk.BooleanVar(split_tab)
split_dest_filename_same_as_source_filename_checkbutton = ttk.Checkbutton(split_tab, text='Same as Source', variable=split_dest_filename_same_as_source_filename, onvalue=True, offvalue=False, command=lambda: dest_filename_same_as_source_filename_checkbutton_cmd(split_dest_filename_same_as_source_filename, split_dest_filename, split_source_path))
split_dest_filename_same_as_source_filename_checkbutton.grid(column=5, row=1)

split_dest_filename_numbering_prefix_label = ttk.Label(split_tab, text='Numbering Prefix: ')
split_dest_filename_numbering_prefix_label.grid(column=0, row=2, sticky=tk.E)

split_dest_filename_numbering_prefix = ttk.Entry(split_tab, width=15)
split_dest_filename_numbering_prefix.grid(column=1, row=2, sticky=tk.W)

split_dest_filename_numbering_postfix_label = ttk.Label(split_tab, text='Postfix: ')
split_dest_filename_numbering_postfix_label.grid(column=2, row=2, sticky=tk.E)

split_dest_filename_numbering_postfix = ttk.Entry(split_tab, width=15)
split_dest_filename_numbering_postfix.grid(column=3, row=2, sticky=tk.W)

split_dest_filename_numbering_length_label = ttk.Label(split_tab, text='Numbering Length: ')
split_dest_filename_numbering_length_label.grid(column=0, row=3, sticky=tk.E)

split_dest_filename_numbering_length = ttk.Spinbox(split_tab, width=5, from_=1, to=1e100, increment=1)
split_dest_filename_numbering_length.set(1)
split_dest_filename_numbering_length.grid(column=1, row=3, sticky=tk.W)

split_dest_filename_numbering_start_label = ttk.Label(split_tab, text='Start: ')
split_dest_filename_numbering_start_label.grid(column=2, row=3, sticky=tk.E)

split_dest_filename_numbering_start = ttk.Spinbox(split_tab, width=5, from_=0, to=1e100, increment=1)
split_dest_filename_numbering_start.set(1)
split_dest_filename_numbering_start.grid(column=3, row=3, sticky=tk.W)

split_source_path_label = ttk.Label(split_tab, text='Source File: ')
split_source_path_label.grid(column=0, row=5, sticky=tk.E)

split_source_path_var = tk.StringVar(split_tab)
split_source_path_var.trace_add('write', lambda *args: split_source_path_changed_cmd(split_source_path, split_range_start, split_range_end))
split_source_path = ttk.Combobox(split_tab, width=60, textvariable=split_source_path_var)
split_source_path.grid(column=1, row=5, columnspan=4)

split_browse_source_path_btn = ttk.Button(split_tab, text='Browse', command=lambda: browse_one_source_file_cmd(split_source_path))
split_browse_source_path_btn.grid(column=5, row=5)

split_range_label = ttk.Label(split_tab, text='Split Range: ')
split_range_label.grid(column=0, row=6, sticky=tk.E)

split_range_start = ttk.Spinbox(split_tab, from_=1, to=1e100, increment=1, width=5, command=lambda: split_range_end.configure(from_=int(split_range_start.get())))
split_range_start.set(1)
split_range_start.grid(column=1, row=6, sticky=tk.E)

split_range_to_label = ttk.Label(split_tab, text='~')
split_range_to_label.grid(column=2, row=6)

split_range_end = ttk.Spinbox(split_tab, from_=1, to=1e100, increment=1, width=5)
split_range_end.set(1)
split_range_end.grid(column=3, row=6, sticky=tk.W)

split_into_one_page = tk.BooleanVar(split_tab)
split_into_one_page_checkbutton = ttk.Checkbutton(split_tab, text='Split into One Page', variable=split_into_one_page, onvalue=True, offvalue=False, command=lambda: split_into_one_page_cmd(split_into_one_page, split_source_path, split_range_listbox))
split_into_one_page_checkbutton.grid(column=5, row=6)

#       <split-inner>
split_range_listbox_frame = tk.Frame(split_tab)

# split_range_listbox_onchange_flag = tk.StringVar(split_tab)
# split_range_listbox_onchange_flag.trace_add('write', lambda *args: split_range_listbox_onchange_cmd(split_into_one_page))

split_range_listbox = tk.Listbox(split_range_listbox_frame, width=60)
split_range_listbox.grid(column=0, row=0)

split_range_listbox_yscroll = ttk.Scrollbar(split_range_listbox_frame, command=split_range_listbox.yview, orient=tk.VERTICAL)
split_range_listbox_yscroll.grid(column=1, row=0, sticky=tk.N+tk.S)

split_range_listbox_xscroll = ttk.Scrollbar(split_range_listbox_frame, command=split_range_listbox.xview, orient=tk.HORIZONTAL)
split_range_listbox_xscroll.grid(column=0, row=1, sticky=tk.W+tk.E)

split_range_listbox_frame.grid(column=1, row=7, columnspan=4, rowspan=4)
#       </split-inner>

split_range_add_btn = ttk.Button(split_tab, text='Add', command=lambda: range_add_cmd(split_range_start, split_range_end, split_range_listbox, True))
split_range_add_btn.grid(column=5, row=7)

split_range_remove_btn = ttk.Button(split_tab, text='Remove', command=lambda: range_remove_cmd(split_range_listbox, True))
split_range_remove_btn.grid(column=5, row=8)

split_range_clear_btn = ttk.Button(split_tab, text='Clear', command=lambda: range_clear_cmd(split_range_listbox, True))
split_range_clear_btn.grid(column=5, row=9)

split_and_save_btn = ttk.Button(split_tab, text='Split and Save', command=lambda: split_and_save_cmd(split_source_path, split_range_listbox, split_dest_path, split_dest_filename, split_dest_filename_numbering_prefix, split_dest_filename_numbering_postfix, split_dest_filename_numbering_length, split_dest_filename_numbering_start))
split_and_save_btn.grid(column=5, row=10)

tabs.add(split_tab, text="Split")
#   </split>

#   <resize>
resize_tab = tk.Frame()

resize_dest_path_label = ttk.Label(resize_tab, text='Destination Path: ')
resize_dest_path_label.grid(column=0, row=0, sticky=tk.E)

resize_dest_path = ttk.Combobox(resize_tab, width=60)
resize_dest_path.grid(column=1, row=0, columnspan=4)

resize_browse_dest_path_btn = ttk.Button(resize_tab, text='Browse', command=lambda: browse_dest_path_cmd(resize_dest_path))
resize_browse_dest_path_btn.grid(column=5, row=0)

resize_dest_filename_label = ttk.Label(resize_tab, text='Destination File Name: ')
resize_dest_filename_label.grid(column=0, row=1, sticky=tk.E)

resize_dest_filename = ttk.Combobox(resize_tab, width=60)
resize_dest_filename.grid(column=1, row=1, columnspan=4)

resize_dest_filename_same_as_source_filename = tk.BooleanVar(resize_tab)
resize_dest_filename_same_as_source_filename_checkbutton = ttk.Checkbutton(resize_tab, text='Same as Source', variable=resize_dest_filename_same_as_source_filename, onvalue=True, offvalue=False, command=lambda: dest_filename_same_as_source_filename_checkbutton_cmd(resize_dest_filename_same_as_source_filename, resize_dest_filename, resize_source_path))
resize_dest_filename_same_as_source_filename_checkbutton.grid(column=5, row=1)

resize_source_path_label = ttk.Label(resize_tab, text='Source File: ')
resize_source_path_label.grid(column=0, row=2, sticky=tk.E)

resize_source_path = ttk.Combobox(resize_tab, width=60)
resize_source_path.grid(column=1, row=2, columnspan=4)

resize_browse_source_path_btn = ttk.Button(resize_tab, text='Browse', command=lambda: browse_one_source_file_cmd(resize_source_path))
resize_browse_source_path_btn.grid(column=5, row=2)

resize_size_label = ttk.Label(resize_tab, text='Destination File Size: ')
resize_size_label.grid(column=0, row=3, sticky=tk.E)

resize_size = ttk.Combobox(resize_tab, width=30, values=list(PDF_FILE_SIZES_NAME_TO_KEY.keys()))
resize_size.bind('<<ComboboxSelected>>', lambda e: combobox_onselected_cmd(resize_size))
resize_size.bind('<KeyRelease>', lambda e: combobox_oninput_cmd(resize_size, e.keysym))
resize_size.grid(column=1, row=3, columnspan=2)

resize_orientation_label = ttk.Label(resize_tab, text='Orientation: ')
resize_orientation_label.grid(column=3, row=3, sticky=tk.E)

resize_orientation = ttk.Combobox(resize_tab, width=10, values=['Portrait', 'Landscape'], state='readonly')
resize_orientation.set('Portrait')
resize_orientation.grid(column=4, row=3, sticky=tk.W+tk.E)

resize_and_save_btn = ttk.Button(resize_tab, text='Resize and Save', command=lambda: resize_and_save_cmd(resize_source_path, resize_size, resize_orientation, resize_dest_path, resize_dest_filename))
resize_and_save_btn.grid(column=5, row=3)

tabs.add(resize_tab, text="Resize")
#   </resize>

#   <compress>
compress_tab = tk.Frame()

compress_dest_path_label = ttk.Label(compress_tab, text='Destination Path: ')
compress_dest_path_label.grid(column=0, row=0, sticky=tk.E)

compress_dest_path = ttk.Combobox(compress_tab, width=60)
compress_dest_path.grid(column=1, row=0)

compress_browse_dest_path_btn = ttk.Button(compress_tab, text='Browse', command=lambda: browse_dest_path_cmd(compress_dest_path))
compress_browse_dest_path_btn.grid(column=2, row=0)

compress_dest_filename_label = ttk.Label(compress_tab, text='Destination File Name: ')
compress_dest_filename_label.grid(column=0, row=1, sticky=tk.E)

compress_dest_filename = ttk.Combobox(compress_tab, width=60)
compress_dest_filename.grid(column=1, row=1)

compress_dest_filename_same_as_source_filename = tk.BooleanVar(compress_tab)
compress_dest_filename_same_as_source_filename_checkbutton = ttk.Checkbutton(compress_tab, text='Same as Source', variable=compress_dest_filename_same_as_source_filename, onvalue=True, offvalue=False, command=lambda: dest_filename_same_as_source_filename_checkbutton_cmd(compress_dest_filename_same_as_source_filename, compress_dest_filename, compress_source_path))
compress_dest_filename_same_as_source_filename_checkbutton.grid(column=2, row=1)

compress_source_path_label = ttk.Label(compress_tab, text='Source File: ')
compress_source_path_label.grid(column=0, row=2, sticky=tk.E)

compress_source_path = ttk.Combobox(compress_tab, width=60)
compress_source_path.grid(column=1, row=2)

compress_browse_source_path_btn = ttk.Button(compress_tab, text='Browse', command=lambda: browse_one_source_file_cmd(compress_source_path))
compress_browse_source_path_btn.grid(column=2, row=2)

compress_and_save_btn = ttk.Button(compress_tab, text='Compress and Save', command=lambda: compress_and_save_cmd(compress_source_path, compress_dest_path, compress_dest_filename))
compress_and_save_btn.grid(column=2, row=3)

tabs.add(compress_tab, text="Compress")
#   </compress>

tabs.grid(column=0, row=0)

window.mainloop()
# </root>
