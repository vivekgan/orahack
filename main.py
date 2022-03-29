from conversions import *
import os
import fitz
import io
from PIL import Image


def get_images_descriptions(tool):
    file = "assets/dashboard.pdf"
    pdf_file = fitz.open(file)
    image_count = 0
    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.get_images()
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img = Image.open(io.BytesIO(pdf_file.extract_image(xref)['image']))
            img.save('assets/'+str(image_count)+".jpg")
            image_count += 1

    images = ['assets/'+str(i)+".jpg" for i in range(image_count)]

    if(tool=="Power BI"):
        return(powerbi_imgdes(images))
    elif(tool=="Tableau"):
        return(tableau_imgdes(images))
    else:
        return []
