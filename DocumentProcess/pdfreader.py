from six import StringIO
import six
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import os
cur_path = os.path.dirname(__file__)
txtDir = cur_path+"/converted_pdf"


# converts pdf, returns its text content as a string

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)


    for page in PDFPage.get_pages(fname, pagenums):
        interpreter.process_page(page)

    # infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


def convertMultiple(pdf):
    # if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in

    # for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
    # pdfDir = "": pdfDir = os.getcwd() + "\\"
    #     fileExtension = pdf.split(".")[-1]
    #     filename = pdf.split(".")[0]
    #     if fileExtension == "pdf":

    # pdfFilename = pdfDir + pdf

    text = convert(pdf)  # get string of text content of pdf
    textFilename = txtDir + "/" + pdf.filename + ".txt"
    textFile = open(textFilename, "wb")  # make text file
    textFile.write(text.encode("utf-8"))  # write text to text file
    return "success"
# textFile.close



# convertMultiple("advs.pdf")

