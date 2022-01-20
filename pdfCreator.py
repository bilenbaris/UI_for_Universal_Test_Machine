from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date
from reportlab.lib.units import cm

class pdfCreator():
    def __init__(self):
        pdfmetrics.registerFont(TTFont('Times New Roman', 'times.ttf'))
        pdfmetrics.registerFont(TTFont('Times New Roman Bold', 'Times New Roman Bold.ttf'))
        self.today = date.today().strftime("%d.%m.%Y")
        

    def __write(self,filename,stringArray, intArray):
        uni_name = stringArray[0].lower()
        name = stringArray[1].lower()
        date_entered = stringArray[2].lower()
        material = stringArray[3].lower()

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)

        #HEADER
        can.drawImage(filename,20,720,width=100,height=100,mask='auto') 
        can.setFont('Times New Roman Bold', 18)
        can.drawString(130, 780, uni_name.upper())
        can.setFont('Times New Roman', 12)
        can.drawString(130, 750, "ÇEKME DENEY TEST CİHAZI, EDUNEERING")
        ###

        
        can.setFont('Times New Roman', 11)
        can.drawString(500, 700, self.today)
        can.setFont('Times New Roman Bold', 11)
        can.drawString(240, 690, "ÇEKME TEST RAPORU")

        can.setFont('Times New Roman', 11)
        can.drawString(50, 660, "Company name:")
        can.drawString(50, 640, "Company contact person:")
        can.drawString(50, 620, "Date of testing:")
        can.drawString(50, 600, "Material:")

        can.setFont('Times New Roman Bold', 11)
        can.drawString(125, 660, uni_name.title())
        can.drawString(165, 640, name.title())
        can.drawString(120, 620, date_entered.title())
        can.drawString(93, 600, material.upper())

        can.setFont('Times New Roman Bold', 12)
        can.drawString(50, 550,"TEST RAPOR ÖZETI")

        can.setFont('Times New Roman', 11)
        string1 = material.upper() + ' malzemeli test numunesinin çekme testi ASTM E8 standardınca ' + date_entered.title() + ' tarihinde gerçekleştirilmiştir.'
        string2 = '\nTest EDUNEERING TEST MACHINE makinesinde gerçekleştirilmiş olup, cihaza bağlı kişisel bilgisayar ile analiz\nve ölçüm hesaplamaları yapılmıştır.'
        string3 = 'Test numunelerinin bertarafı görsel ve ölçüsel olarak muayene ile kontrol edilmiştir.'
        string4 = '\nSonuçların detayı aşağıda yer almaktadır.'

        stringAll = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
        textobject = can.beginText(1.8*cm, 29.7 * cm - 11 * cm)
        for line in stringAll.splitlines(False):
            textobject.textLine(line.rstrip())
        can.drawText(textobject)
        
        can.drawString(210, 390, str(intArray[0]))
        can.drawString(290, 390, str(intArray[1]))
        can.drawString(380, 390, str(intArray[2]))
        can.drawString(470, 390, str(intArray[3]))

        can.setFont('Times New Roman', 11)
        can.drawString(50, 325,"S1 numunesinin akma dayanımı X, kopma dayanımı Y olarak ölçülmüştür.")

        can.setFont('Times New Roman Bold', 12)
        can.drawString(50, 260,"HAZIRLAYAN VE ONAYLAYAN")

        can.setFont('Times New Roman', 11)
        can.drawString(50, 230, name.title())
        can.drawString(50, 210, uni_name.title())
        can.drawString(50, 190, "Öğrenci, Proje Sorumlusu")

        can.setFont('Times New Roman Bold', 11)
        can.drawString(50, 170, "Imza:")

        can.save()
        #move to the beginning of the StringIO buffer
        packet.seek(0)
        return packet


    def create(self,filename, stringArray, intArray):
        
        packet = self.__write(filename,stringArray, intArray)

        # create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("RAPOR_CIKTI_Empty.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open("C:/Users/baris/Desktop/Test Raporu.pdf", "wb")
        output.write(outputStream)
        outputStream.close()
