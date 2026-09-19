import tkinter as tk
from tkinter import ttk


class PartnerCard(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        partner_type: str,
        name: str,
        director: str,
        phone: str,
        rating: int,
        discount: int,
    ) -> None:
        super().__init__(master, bg="white", bd=1, relief="solid", padx=16, pady=12)

        title_label = tk.Label(
            self,
            text=f"{partner_type} | {name}",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#222222",
        )
        title_label.grid(row=0, column=0, sticky="w")

        discount_label = tk.Label(
            self,
            text=f"{discount}%",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#222222",
        )
        discount_label.grid(row=0, column=1, sticky="e")

        director_label = tk.Label(
            self,
            text=director,
            font=("Arial", 12),
            bg="white",
            fg="#444444",
        )
        director_label.grid(row=1, column=0, sticky="w", pady=(8, 0))

        phone_label = tk.Label(
            self,
            text=phone,
            font=("Arial", 12),
            bg="white",
            fg="#444444",
        )
        phone_label.grid(row=2, column=0, sticky="w")

        rating_label = tk.Label(
            self,
            text=f"Рейтинг: {rating}",
            font=("Arial", 12),
            bg="white",
            fg="#444444",
        )
        rating_label.grid(row=3, column=0, sticky="w")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)


def create_mockup() -> None:
    root = tk.Tk()
    root.title("CRM: Список партнеров и скидок")
    root.geometry("900x650")
    root.configure(bg="#f2f2f2")

    try:
        root.iconbitmap("resources/app_icon.ico")
    except Exception:
        pass

    header = tk.Frame(root, bg="#e9ecef", height=90)
    header.pack(fill="x")

    try:
        logo_image = tk.PhotoImage(file="resources/logo.png.avif")
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

    content = tk.Frame(root, bg="#f2f2f2")
    content.pack(fill="both", expand=True, padx=20, pady=20)

    partners = [
        ("Тип", "Наименование партнера", "Директор", "+7 223 322 22 32", 10, 10),
        ("Тип", "Наименование партнера", "Директор", "+7 223 322 22 32", 10, 10),
        ("Тип", "Наименование партнера", "Директор", "+7 223 322 22 32", 10, 10),
    ]

    for partner in partners:
        card = PartnerCard(content, *partner)
        card.pack(fill="x", pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_mockup()
