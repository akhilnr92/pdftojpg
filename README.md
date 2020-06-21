# pdftojpg
Tool for converting pdf files to jpg images and set image properties like dpi,bpp etc by iterating through sub folders.

## Requirements:

This tool requires Irfanview(https://www.irfanview.com/main_download_engl.htm) and Poppler(http://blog.alivate.com.au/poppler-windows/).

1. Install Irfanview. (Ensure the exe is in path: C:\Program Files (x86)\IrfanView\i_view32.exe)
2. Add path of Poppler bin/ folder to PATH as environment variable.(Follow the steps here:   	https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)


## How to Run:

1. Run pdftojpg_1.exe.
2. User will be promted to enter the root folder and press enter. (It will go through the subfolders and identify the PDF files)
3. Once convertion has completed, user will be prompted again to exit.

## Limitation:

1. PDF files containing more than 100 pages might throw and error. Such cases will have to be dealt with manually.
	If the tool seems to be stuck after displaying an error press 'ctrl + C' to continue. 

