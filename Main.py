import tkinter as tk
import random

class VirtualFarmSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Plantação Virtual")
        self.money = 100
        self.crops = []
        self.crop_prices = {"Trigo": 20, "Milho": 15, "Soja": 30}

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Simulador de Plantação Virtual", font=("Arial", 18)).pack(pady=10)

        # Exibir saldo
        self.money_label = tk.Label(self.root, text=f"Saldo: R$ {self.money}", font=("Arial", 14))
        self.money_label.pack(pady=5)

        # Opções de plantação
        tk.Label(self.root, text="Escolha uma plantação:").pack()
        self.crop_menu = tk.StringVar(self.root)
        self.crop_menu.set("Trigo")
        tk.OptionMenu(self.root, self.crop_menu, *self.crop_prices.keys()).pack()

        # Botão para plantar
        tk.Button(self.root, text="Plantar", command=self.plantar).pack(pady=5)

        # Botão para colher
        tk.Button(self.root, text="Colher", command=self.colher).pack(pady=5)

        # Lista de plantações
        self.crop_list_label = tk.Label(self.root, text="Plantações Atuais: Nenhuma")
        self.crop_list_label.pack(pady=10)

    def plantar(self):
        crop_name = self.crop_menu.get()
        price = self.crop_prices[crop_name]
        
        if self.money >= price:
            self.money -= price
            self.crops.append(crop_name)
            self.update_ui()
            tk.messagebox.showinfo("Sucesso", f"Você plantou {crop_name}! Custo: R$ {price}")
        else:
            tk.messagebox.showerror("Erro", "Saldo insuficiente para plantar!")

    def colher(self):
        if not self.crops:
            tk.messagebox.showwarning("Aviso", "Não há plantações para colher.")
            return

        colheita = random.choice(self.crops)
        self.crops.remove(colheita)
        ganho = random.randint(10, 50)
        self.money += ganho
        
        self.update_ui()
        tk.messagebox.showinfo("Sucesso", f"Você colheu {colheita} e ganhou R$ {ganho}!")

    def update_ui(self):
        self.money_label.config(text=f"Saldo: R$ {self.money}")
        planta_listagem = ", ".join(self.crops) if self.crops else "Nenhuma"
        self.crop_list_label.config(text=f"Plantações Atuais: {planta_listagem}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualFarmSimulator(root)
    root.mainloop()
