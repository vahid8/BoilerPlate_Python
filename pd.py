# extract_doc_info.py
import cv2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import os
# import module
from pdf2image import convert_from_path


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def downsize_pdf(path):
    # first read each page and convert it to pdf
    pdf_reader = PdfFileReader(path)
    for num, page in enumerate(range(pdf_reader.getNumPages())):
            # create a new pdf writer
            pdf_writer = PdfFileWriter()
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
            # Write out the PDF to temp
            with open("temp.pdf", 'wb') as out:
                pdf_writer.write(out)
            img = convert_from_path("temp.pdf")[0]

            img = img.resize((1240 , 1754))
            # img.save('page' + str(num) + '.jpg', 'JPEG')
            img.save("page" + str(num+1) + '.pdf')


def convert_single_image_to_pdf(path):
    image1 = Image.open(path)
    im1 = image1.convert('RGB')
    im1.save("output.pdf")

def convert_to_pdf(files, path):
    images = list()
    for file in files:
        image1 = Image.open(file)
        im1 = image1.convert('RGB')
        im1.save(path+"/"+file.split("/")[-1][0:-4]+".pdf")
        images.append(im1)

#
#
if __name__ == '__main__':
    # path = '/home/vahid/Documents/Steuer_Docs/2019/to_print/04105_BetriebsKosten.pdf'
    # extract_information(path)
    pdf_path = 'pdf'
    # img_files = [path + "/" + x for x in os.listdir(path) if x.endswith(".jpg")]
    # pdf_images = convert_to_pdf(img_files, path)

    # GET THE LIST OF AVAILABLE PDFS
    # pdf_files = [os.path.join(pdf_path, item) for item in os.listdir(pdf_path) if item.endswith(".pdf")]
    # pdf_files.sort()
    # merge_pdfs(pdf_files, output='merged.pdf')
    #

    downsize_pdf("Salary Vahid Aghajani 07-2022.pdf")
    # convert_single_image_to_pdf("temp.jpg")

# Store Pdf with convert_from_path function
# images = convert_from_path('pcr.pdf',dpi=600,userpw='21.09.1987')
#
# for i in range(len(images)):
#     # Save pages as images in the pdf
#     images[i].save('page' + str(i) + '.jpg', 'JPEG')
