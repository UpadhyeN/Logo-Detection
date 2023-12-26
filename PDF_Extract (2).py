import fitz # Extension of PyMuPDF
import io # library to deal with Input and output
from PIL import Image # Library to work with images
import os # Library to get information about Operating system
from tqdm import tqdm # pip install tqdm

def extracting_images(pdf_file,images_folder):
    """
    2 inputs,
    Input 1 : pdf_file
    Input 2 : images_folder
    """
    doc = fitz.Document(pdf_file) # Opening the file

    for i in tqdm(range(len(doc)), desc="pages"): # looping through pages
            for img in tqdm(doc.get_page_images(i), desc="page_images"): # looping through all the images in the page
                xref = img[0] 
                image = doc.extract_image(xref) # Extraqcting the first image 
                #Pixmaps (“pixel maps”) are objects at the heart of MuPDF’s rendering capabilities.
                pix = fitz.Pixmap(doc, xref) 
                image_directory = images_folder
                
               
                if os.path.exists(images_folder): # if the folder exist then save images to the folder directly
                    pix.save(os.path.join(images_folder, "p%s-%s.png" % (i, xref)))
                else:
                    os.mkdir(images_folder)# if the folder does not exist then create a folder and save it to that
                    pix.save(os.path.join(images_folder, "p%s-%s.png" % (i, xref)))
    return 0 # as saving is done in the file we dont have to return anything


def extracting_text(pdf_file,text_path,text_file_name): # creating a function 
    """
    @fuction to extract text file.
    input1 = pdf_file
    input2 = text_path
    input3 = text_file_name
    """
    doc = fitz.open(pdf_file) # reading the main pdf
    total_pages = doc.page_count # storing the number of pages of PDF in total_pages variable
    for i in range(0,total_pages):
        page = doc[i] # Reading a single Page
        text = page.get_text("text") # Extracting the text
        print(text) 
        page_no = "page No "+str(i) # creating a variable so that in the extraction file we can get the page number and then content
        with open(text_path+text_file_name+".txt","a+",encoding="utf-8") as my_file: # creating a text file to store the text
            """
            We are writing page number then on new line we are writing text
            """
            my_file.write(page_no)
            my_file.write("\n")
            my_file.write(text)
            
    return 0 # as file is getting stored function doesnt have to return anything


