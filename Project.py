import google.generativeai as genai

import tkinter as tk
from tkinter import filedialog, ttk
import threading
import os

genai.configure(api_key="GEMINI_API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILES = {
    "Czysty kod": os.path.join(BASE_DIR, "prompts", "czysty_kod.txt"),
    "OOP": os.path.join(BASE_DIR, "prompts", "oop.txt"),
    "SOLID": os.path.join(BASE_DIR, "prompts", "solid.txt"),
    "DRY": os.path.join(BASE_DIR, "prompts", "dry.txt"),
    "KISS": os.path.join(BASE_DIR, "prompts", "kiss.txt"),
    "Prawo Demeter": os.path.join(BASE_DIR, "prompts", "prawo_demeter.txt"),
    "Code Smell": os.path.join(BASE_DIR, "prompts", "code_smell.txt")
}

class CodeAnalyzer:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")

    def analyze(self, filepath, prompt_path):
        with open(filepath, "r", encoding="utf-8") as file:
            code = file.read()
        with open(prompt_path, "r", encoding="utf-8") as pfile:
            prompt = pfile.read()
        full_prompt = prompt.replace("{code}", code)
        response = self.model.generate_content(full_prompt)
        return response.text

def analyze_in_thread(filepath, prompt_path):
    progress.start()
    def update_gui_start():
        progress.pack(pady=10)
    root.after(0, update_gui_start)
    try:
        result = analyzer.analyze(filepath, prompt_path)
    except Exception as e:
        result = f"Błąd podczas analizy: {e}"
    def update_gui():
        progress.stop()
        progress.pack_forget()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result)
        output_text.pack_forget()
        output_text.pack(padx=10, pady=10)
        buttons_frame.pack(pady=10)
    root.after(0, update_gui)

def open_file_and_analyze(prompt_path):
    filepath = filedialog.askopenfilename(
        filetypes=[("Python files", "*.py"), ("All files", "*.*")]
    )
    if filepath:
        threading.Thread(target=analyze_in_thread, args=(filepath, prompt_path), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Analiza kodu (Gemini)")
    root.geometry("900x600")
    root.resizable(False, False)

    def on_closing():
        root.quit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    analyzer = CodeAnalyzer(GEMINI_API_KEY)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    buttons = []
    button_width = 15
    button_height = 2
    for label, prompt_path in PROMPT_FILES.items():
        btn = tk.Button(
            buttons_frame,
            text=label,
            width=button_width,
            height=button_height,
            command=lambda p=prompt_path: open_file_and_analyze(p)
        )
        btn.pack(side=tk.LEFT, padx=2)
        buttons.append(btn)

    output_text_frame = tk.Frame(root)
    output_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    output_text_scrollbar = tk.Scrollbar(output_text_frame)
    output_text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text = tk.Text(output_text_frame, width=100, height=30, wrap=tk.WORD, yscrollcommand=output_text_scrollbar.set)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    output_text_scrollbar.config(command=output_text.yview)

    progress = ttk.Progressbar(root, mode="indeterminate")

    root.mainloop()