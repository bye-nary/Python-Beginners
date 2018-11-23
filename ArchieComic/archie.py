import urllib.request
import os
from fpdf import FPDF

try:
    pdf=FPDF()
    pdf.add_page() #adds the first page for the pdf
    
    #this is static. can be programmed into the script to pick up the number of pages automatically
    for i in range(1,35):    
        #url image, the url differs by the page number which is determined by the iterative value of i
        URL="page_url"+i+".jpg"
        #prints url for catching errors, if they occur
        print(URL)
      
        NAME=str(i)
        
        #gives the path
        FNAME=os.path.join("C://insert_your_target_folder_here"+NAME+".jpg")
        #retrieves the image and saves it to the path specified in FNAME
        urllib.request.urlretrieve(URL, FNAME)
        
        #copies image from path to the PDF object pdf
        #w, h gives the width and height
        pdf.image(FNAME, w=210, h=297)
        
except Exception as e:
    print(str(e))
    
#saves the pdf
pdf.output("OUtput2.pdf", "F")
print("Done")         #prints DONE when over.
