import tkinter as tk


class PartnerCard(tk.Frame):
    def __init__(self, master: tk.Misc, partner: dict) -> None:
        super().__init__(master, bg="white", bd=1, relief="solid", padx=16, pady=12)

        title_label = tk.Label(
            self,
            text=f'{partner["partner_type"]} | {partner["name"]}',
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#222222",
        )
        title_label.grid(row=0, column=0, sticky="w")

        discount_label = tk.Label(
            self,
            text=f'{partner["discount_percent"]}%',
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#222222",
        )
        discount_label.grid(row=0, column=1, sticky="e")

        director_label = tk.Label(
            self,
            text=partner["director"],
            font=("Arial", 12),
            bg="white",
            fg="#444444",
        )
        director_label.grid(row=1, column=0, sticky="w", pady=(8, 0))

        phone_label = tk.Label(
            self,
            text=partner["phone"],
            font=("Arial", 12),
            bg="white",
            fg="#444444",
        )
        phone_label.grid(row=2, column=0, sticky="w")

        rating_label = tk.Label(
            self,
            text=f'Рейтинг: {partner["rating"]}',
            font=("Arial", 12),
            bg="white",
            fg="#444444",
        )
        rating_label.grid(row=3, column=0, sticky="w")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)


class App(tk.Tk):
    def __init__(self, partners: list[dict]) -> None:
        super().__init__()

        self.title("CRM: Список партнеров и скидок")
        self.geometry("900x650")
        self.configure(bg="#f2f2f2")

        try:
            self.iconbitmap("resources/app_icon.ico")
        except Exception:
            pass

        header = tk.Frame(self, bg="#e9ecef", height=90)
        header.pack(fill="x")

        try:
            logo_image = tk.PhotoImage(file="resources/logo.png")
            logo_label = tk.Label(header, image=logo_image, bg="#e9ecef")
            logo_label.image = logo_image
            logo_label.pack(side="left", padx=20, pady=15)
        except Exception:
            logo_label = tk.Label(
                header,
                text="[ЛОГО]",
                font=("Arial", 14, "bold"),
                bg="#e9ecef",
            )
            logo_label.pack(side="left", padx=20, pady=15)

        title_label = tk.Label(
            header,
            text="CRM: Список партнеров и скидок",
            font=("Arial", 20, "bold"),
            bg="#e9ecef",
            fg="#222222",
        )
        title_label.pack(side="left", padx=10)

        content = tk.Frame(self, bg="#f2f2f2")
        content.pack(fill="both", expand=True, padx=20, pady=20)

        for partner in partners:
            card = PartnerCard(content, partner)
            card.pack(fill="x", pady=10)
