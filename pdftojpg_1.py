import os
from pdf2image import convert_from_path
import logging


#Define function for logging

def log():
    logging.basicConfig(filename = 'log.log',level=logging.DEBUG, format='\n%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.error("Exception occurred", exc_info=True)

#Declare Irfanview path and source and target file type 
    
IVIEW32_PATH = 'C:\Program Files (x86)\IrfanView\i_view32.exe'
SOURCE_FILETYPE = 'jpg'
TARGET_FILETYPE = 'jpg'

#Get root folder from user and change directory to that path

pdf_dir = input("Enter path of root folder: ")
os.chdir(pdf_dir)


#Define function to extract images from pdf, save as jpg and update image properties using irfanview

def convert(s):
    os.chdir(s)

    
    for pdf_file in os.listdir(s):

        if pdf_file.endswith(".pdf"):
             try:
                pages = convert_from_path(pdf_file)
                pdf_file = pdf_file[:-4]
                

             
                for page in pages:

                    page.save("%s-page%d.jpg" % (pdf_file,pages.index(page)),"JPEG")
                    command = '"%s" '%IVIEW32_PATH + os.getcwd() + r"\*.%s /dpi=(200,200)/resize=(1699,2199)/bpp=24 /convert="%(SOURCE_FILETYPE) + os.getcwd() + r"\Images\*.%s"%TARGET_FILETYPE
                    os.system(command)
                    

                    for img in os.listdir(s):

                        if img.endswith(".jpg"):

                            os.remove(img)
                            
             except:
                 print('Error: Please check PDF files and convert manually.')
                 log()


#Iterate through the subfolders 

for root, dirs, files in os.walk(pdf_dir, topdown=True):
##   for name in files:
##      r = os.path.join(root, name) 
##      convert(r)
##      print(r + 'done')
   for name in dirs:
      s = os.path.join(root, name)
      
      print (s)
      convert(s)
      print( 'done')
