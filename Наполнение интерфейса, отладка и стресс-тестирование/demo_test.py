from service import get_all_partners_with_discount


def run_demo_test() -> None:
    partners = get_all_partners_with_discount()

    assert len(partners) > 0

    for partner in partners:
        assert "name" in partner
        assert "phone" in partner
        assert "discount_percent" in partner
        assert partner["discount_percent"] in [0, 5, 10, 15]
        assert partner["total_quantity"] >= 0

    partner_without_sales = None

    for partner in partners:
        if partner["name"] == "Партнер Д":
            partner_without_sales = partner
            break

    assert partner_without_sales is not None
    assert partner_without_sales["total_quantity"] == 0
    assert partner_without_sales["discount_percent"] == 0

    print("Demo test passed successfully.")


if __name__ == "__main__":
    run_demo_test()
