"""PDF sayalarını seslendirme."""
# PDF üzerinde işlem yapmak için PyPDF
import PyPDF2  # pip install PyPDF2
# pyttsx3 dökümanları
# https://pyttsx3.readthedocs.io/en/latest/engine.html
import pyttsx3  # pip install pyttsx3

konusmaci = pyttsx3.init()


okuma_hizi = konusmaci.getProperty('rate')
ses_seviyesi = konusmaci.getProperty('volume')

# TEXT = 'Akdeniz Üniversitesi'
# seslendirmeci eklemek.
# https://www.microsoft.com/en-us/download/details.aspx?id=27224
# seslendirenler = konusmaci.getProperty('voices')
# SES_ZIRA = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
# konusmaci.setProperty('voice', SES_ZIRA)
# konusmaci.setProperty('rate', okuma_hizi - 85)
# konusmaci.say(TEXT)
# konusmaci.runAndWait()

# for seslendiren in seslendirenler:
#     print(seslendiren)
#     # print(seslendiren.languages,seslendiren.gender)
#     konusmaci.setProperty('voice', seslendiren.id)
#     konusmaci.setProperty('rate', okuma_hizi - 85)
#     konusmaci.setProperty('volume', okuma_hizi + 1.0)
#     pyttsx3.speak(text=TEXT)
#     # konusmaci.say(TEXT)
#     # konusmaci.runAndWait()

# konusmaci.save_to_file(TEXT, 'deneme.mp3')
# konusmaci.runAndWait()

pdf_oku = PyPDF2.PdfFileReader(
    open('Akdeniz_Universitesi_Tanitim_Katalogu.pdf', 'rb'))

# for sayfaNo in range(pdf_oku.numPages):
#     text = pdf_oku.getPage(sayfaNo).extractText()
#     konusmaci.say(text=text)
#     konusmaci.runAndWait()
text = pdf_oku.getPage(8).extractText()
print(text)
konusmaci.say(text=text)
konusmaci.runAndWait()
konusmaci.stop()
