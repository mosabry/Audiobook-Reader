# import important libraries
import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')  # open pdf location
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()

for num in range(7, pages):  # from start page to end page
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
