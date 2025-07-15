import customtkinter as ctk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
import re

def extract_numbers_from_pdf(pdf_path):
    numbers = []
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    numbers.extend(re.findall(r'\b\d+\b', text))
    except Exception as e:
        messagebox.showerror("Erro de Leitura", f"Não foi possível ler o arquivo PDF:\n{e}")
        return None
    return numbers

def process_pdf():
    pdf_path = file_path_entry.get()
    if not pdf_path:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo PDF primeiro.")
        return

    numbers = extract_numbers_from_pdf(pdf_path)
    if numbers is None:
        return
    
    output_textbox.delete('1.0', ctk.END)

    filtered_numbers = [int(number) for number in numbers if 10 <= int(number) <= 999]
    main_numbers = [90, 100, 105, 135, 150, 157, 175, 180, 200, 210]
    numbers_count = {number: filtered_numbers.count(number) for number in set(filtered_numbers)}

    output_text = "CH\t\tQuantidade\n====================\n"
    for number in main_numbers:
        count = numbers_count.get(number, 0)
        output_text += f"{number}\t\t{count}\n"
    output_text += "====================   CONFIRA OS RESULTADOS\n\nOutros Números:\n"

    other_numbers_found = False
    for number, count in sorted(numbers_count.items()):
        if number not in main_numbers:
            output_text += f"{number}\t\t{count}\n"
            other_numbers_found = True
            
    if not other_numbers_found:
        output_text += "(Nenhum outro número encontrado)\n"
    
    output_textbox.insert(ctk.END, output_text)

def select_file():
    filepath = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=(("PDF Files", "*.pdf"), ("All files", "*.*"))
    )
    if filepath:
        file_path_entry.delete(0, ctk.END)
        file_path_entry.insert(0, filepath)

# --- Configuração da Janela Principal ---
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Contador de Números em PDF")
app.geometry("600x450")

# Frame para organizar os widgets
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

file_label = ctk.CTkLabel(frame, text="Arquivo PDF:", font=("", 14))
file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

file_path_entry = ctk.CTkEntry(frame, width=300)
file_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

browse_button = ctk.CTkButton(frame, text="Procurar...", command=select_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

process_button = ctk.CTkButton(frame, text="Contar Números", command=process_pdf, font=("", 12, "bold"))
process_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

output_textbox = ctk.CTkTextbox(frame, width=500, height=250, font=("Courier New", 12))
output_textbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)

app.mainloop()