import os
import shutil
import importlib
import sys
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
 
def readPDF(path):
    pdffile=open(path,"rb")
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)
    process_pdf(rsrcmgr,device,pdffile)
    device.close()
    content=retstr.getvalue()
    retstr.close()

    pdffile.close()
    return content 

def load_file():
      walk = os.walk('./../来自手机')
      for root, dirs,files in walk:
             for name in files:
                 print(name)
                #  print('C:\\Users\\zyf10\\Desktop\\biji\\来自手机\\'+name)
                 print(readPDF('C:\\Users\\zyf10\\Desktop\\biji\\来自手机\\'+name))
                  
       
load_file()
