from tkinter import Tk, filedialog
from reportlab.pdfgen import canvas

def choose_text_file():
    root = Tk()
    root.withdraw()  # Tkinter penceresini gösterme

    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    return file_path

def text_to_pdf(input_text_file, output_pdf_file):
    # PDF dosyasını oluştur
    pdf_canvas = canvas.Canvas(output_pdf_file)

    # Metin dosyasını oku ve PDF'ye ekle
    with open(input_text_file, 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()
        y_coordinate = 800  # İlk başta metni eklemeye başlayacağınız dikey konum
        for line in lines:
            pdf_canvas.drawString(100, y_coordinate, line.strip())  # Metni belirli bir konuma ekle
            y_coordinate -= 15  # Dikey konumu azalt

    # PDF dosyasını kaydet
    pdf_canvas.save()

if __name__ == "__main__":
    input_text_file = choose_text_file()
    
    if input_text_file:
        output_pdf_file = "output.pdf"  # PDF dosyasının adını değiştirin
        text_to_pdf(input_text_file, output_pdf_file)
        print(f"PDF file '{output_pdf_file}' created successfully.")
