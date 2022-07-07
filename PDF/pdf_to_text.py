"""PDF dönüştürme."""
import os
import pathlib
from glob import glob
from PIL import Image  # pip install Pillow
import pdf2image  # pip install pdf2image
import pytesseract  # pip install pytesseract

# sıkıştırılmış dosya açılıp bin klasör bilgisi
# path bilgisi olarak eklenmelidir.
# path kontrolü için : pdftoppm -h
# komutu kullanılabilir.
# https://blog.alivate.com.au/poppler-windows/


def get_files(path):
    """belirtilen pathdeki dosyaları döndürür."""
    files = [file for file in os.listdir(
        path) if os.path.isfile(os.path.join(path, file))]
    return files


def get_filesv2(path):
    """belirtilen pathdeki dosyaları döndürür."""
    files = []
    # for (dir_path, dir_name, file_name) in os.walk(path):
    for (_, _, file_name) in os.walk(path):
        files.extend(file_name)
    return files


def get_filesv3(path):
    """belirtilen pathdeki dosyaları döndürür."""
    res = glob(path+'\\*')
    return res


def get_filev4(path):
    """belirtilen pathdeki dosyaları döndürür."""
    res = []
    p = pathlib.Path(path)
    for entry in p.iterdir():
        if entry.is_file():
            res.append(entry)
            # uzantısı
            # print(entry.suffix)
    return res


# çalışılan klasörün path bilgisinin bulunması.
# current_directory = os.getcwd()

pdf_files = list(
    filter(lambda x: os.path.isfile(os.path.join(os.getcwd(), x)) and
           pathlib.Path(x).suffix == '.pdf',
           os.listdir(os.getcwd())))


def pdf_extract(path, file, i):
    print('FILE:', os.path.join(path, file))
    pages_image = pdf2image.convert_from_path(
        os.path.join(path, file),
        dpi=500,
        output_folder=os.path.join(path, 'temp'))
    print(pages_image)
    files = [f for f in os.listdir(os.path.join(path, 'temp')) if '.ppm' in f]
    files.sort()
    # txt_file = open(os.path.join(path, 'result{}.txt'.format(i)),
    #                 'w', encoding='utf-8')

    print(os.path.join(path, 'temp', file))
    # https://tesseract-ocr.github.io/tessdoc/Installation.html
    i = 0
    for f in sorted(files):
        txt_file = open(os.path.join(path, 'temp', os.path.basename(f)+'result{}.txt'.format(i)),
                        'w', encoding='utf-8')
        # Türkçe dil desteği için
        # https://github.com/tesseract-ocr/tessdoc/blob/main/tess3/Data-Files.md
        temp = pytesseract.image_to_string(
            Image.open(os.path.join(path, 'temp', f)), lang='tur')
        txt_file.write(temp)
        txt_file.close()
        i += 1


def dosya_sil(uzanti, ekpath=''):
    del_files = list(
        filter(lambda x: os.path.isfile(os.path.join(os.getcwd(), ekpath, x)) and
               pathlib.Path(x).suffix == uzanti,
               os.listdir(os.path.join(os.getcwd(), ekpath))))
    print(del_files)

    for f in del_files:
        os.remove(os.path.join(os.getcwd(), ekpath, f))


dosya_sil('.ppm', ekpath='temp')
dosya_sil('.txt', ekpath='temp')

pdf_files = list(
    filter(lambda x: os.path.isfile(os.path.join(os.getcwd(), x)) and
           pathlib.Path(x).suffix == '.pdf',
           os.listdir(os.getcwd())))
print(pdf_files)

for i, dosya in enumerate(pdf_files):
    pdf_extract(os.getcwd(), dosya, i)
