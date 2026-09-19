from service import get_all_partners_with_discount
from ui import App


def main() -> None:
    partners = get_all_partners_with_discount()
    app = App(partners)
    app.mainloop()


if __name__ == "__main__":
    main()
