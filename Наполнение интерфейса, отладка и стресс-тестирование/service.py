from discount import calculate_partner_discount
from repository import get_all_partners_with_total_quantity


def get_all_partners_with_discount() -> list[dict]:
    partners = get_all_partners_with_total_quantity()

    for partner in partners:
        total_quantity = partner["total_quantity"]

        if total_quantity is None:
            total_quantity = 0

        total_quantity = int(total_quantity)
        partner["total_quantity"] = total_quantity
        partner["discount_percent"] = calculate_partner_discount(total_quantity)

    return partners
