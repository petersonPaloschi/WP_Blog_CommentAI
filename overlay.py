import tkinter as tk
import multiprocessing
import threading

def get_screen_resolution(root):
    """Retorna a resolução da tela como uma string no formato 'largura x altura'."""
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    return f"{width}x{height}"

class OverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.keep_running = True  # variável de controle para manter o loop em execução
        self.setup_window()
        self.create_widgets()
        self.message_queue = multiprocessing.Queue()
        self.consume_text()

    def setup_window(self):
        """Configura a janela principal."""
        resolution = get_screen_resolution(self.root)
        self.root.geometry(resolution)
        self.root.overrideredirect(True)
        self.root.config(bg='#000000')
        self.root.attributes("-alpha", 1)
        self.root.wm_attributes("-topmost", 1)
        self.root.attributes('-transparentcolor', '#000000', '-topmost', 1)
        self.root.resizable(False, False)

    def create_widgets(self):
        """Cria os widgets para a janela principal."""
        self.console = tk.Text(self.root, state='disabled', width=50, height=10, bg="black", fg="red", bd=0)
        self.console.place(x=20, y=20)

    def show_log(self, message):
        """Exibe a mensagem no console."""
        self.message_queue.put(("CONSOLE", message))
        self.consume_text()

    def consume_text(self):
        """Lê a fila de mensagens e exibe as mensagens no console."""
        if not self.message_queue.empty():
            message = self.message_queue.get()
            if 'CONSOLE' in message[0]:
                self.console.configure(state='normal')
                self.console.insert(tk.END, f'{message[1]}\n')
                self.console.configure(state='disabled')
                self.console.yview(tk.END)

        if self.keep_running:
            self.root.after(ms=1, func=self.consume_text)

    def stop(self):
        """Interrompe a execução do loop principal."""
        self.keep_running = False

    def run(self):
        """Inicia o loop principal da aplicação."""
        def run_tk():
            while self.keep_running:
                self.root.update()  # atualiza a janela do Tkinter
                self.consume_text()

        # inicia a thread do loop do Tkinter
        t = threading.Thread(target=run_tk)
        t.start()

