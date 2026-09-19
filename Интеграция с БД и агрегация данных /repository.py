import sqlite3
from typing import Any


def get_partner_with_total_quantity(partner_id: int) -> dict[str, Any] | None:
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            p.id,
            p.partner_type,
            p.name,
            p.director,
            p.phone,
            p.rating,
            COALESCE(SUM(sh.quantity), 0) AS total_quantity
        FROM partners AS p
        LEFT JOIN sales_history AS sh
            ON p.id = sh.partner_id
        WHERE p.id = ?
        GROUP BY
            p.id,
            p.partner_type,
            p.name,
            p.director,
            p.phone,
            p.rating
        """,
        (partner_id,),
    )

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return dict(row)
