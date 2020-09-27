# import important libraries
import pyttsx3
import PyPDF2

book = open('<name.pdf>', 'rb')  # open pdf location
pdfReader = PyPDF2.PdfFileReader(book)  # access the book
pages = pdfReader.numPages  # access the number of pages
# print(pages)

speaker = pyttsx3.init()

for num in range(7, pages):  # from page number 7 to end page
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
