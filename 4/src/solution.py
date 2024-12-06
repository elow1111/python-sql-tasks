import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def get_order_sum(conn, month):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("""
            SELECT c.customer_name, SUM(o.total_amount) AS total_amount
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            WHERE EXTRACT(MONTH FROM o.order_date) = %s
            GROUP BY c.customer_name
            ORDER BY total_amount DESC
        """, (month,))
        
        return "\n".join(
            f"Покупатель {row['customer_name']} совершил покупок на сумму {row['total_amount']}"
            for row in cursor.fetchall()
        )
# END
