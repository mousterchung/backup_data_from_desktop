with (open(r'C:\Users\Dinsh\Desktop\name_of_no_mozaic.txt',encoding='UTF-8')as file_in,
      open(r'C:\Users\Dinsh\Desktop\name_of_moziac.csv','w',encoding='UTF-8')as file_out):
    for no_mozaic in file_in:
        if len(no_mozaic.strip())==2:
            file_out.write(no_mozaic[0]+'Ｏ'+'\n')
        elif len(no_mozaic.strip())==3:
            file_out.write(no_mozaic[0]+'Ｏ'+no_mozaic[2]+'\n')
        else:
            file_out.write(no_mozaic.strip()+'\n')
