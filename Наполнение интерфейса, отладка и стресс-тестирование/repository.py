import sqlite3
from typing import Any


def get_all_partners_with_total_quantity() -> list[dict[str, Any]]:
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
        GROUP BY
            p.id,
            p.partner_type,
            p.name,
            p.director,
            p.phone,
            p.rating
        ORDER BY p.id
        """
    )

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]
