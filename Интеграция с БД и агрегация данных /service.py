from discount import calculate_partner_discount
from repository import get_partner_with_total_quantity


def get_partner_with_discount(partner_id: int) -> dict | None:
    partner = get_partner_with_total_quantity(partner_id)

    if partner is None:
        return None

    total_quantity = int(partner["total_quantity"])
    discount = calculate_partner_discount(total_quantity)
    partner["discount_percent"] = discount

    return partner


if __name__ == "__main__":
    for partner_id in range(1, 5):
        result = get_partner_with_discount(partner_id)
        print(result)
