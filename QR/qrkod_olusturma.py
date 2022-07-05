"""QR Kod oluşturma."""
import pyqrcode

url_string = "https://www.akdeniz.edu.tr"

url = pyqrcode.create(url_string)
url.svg("qrkod.svg", scale=8)
