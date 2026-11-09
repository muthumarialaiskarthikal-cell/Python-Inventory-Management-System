
import sqlite3

DB_NAME = "inventory.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_product(pid, name, qty):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO products VALUES (?, ?, ?)",
            (pid, name, qty)
        )
        conn.commit()
        print("Product added successfully")

    except sqlite3.IntegrityError:
        print("Product ID already exists")

    finally:
        conn.close()


def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()
    return products


def search_product(pid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE product_id = ?",
        (pid,)
    )
    product = cursor.fetchone()

    conn.close()
    return product


def update_product(pid, qty):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE product_id = ?",
        (qty, pid)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Product updated successfully")
    else:
        print("Product not found")

    conn.close()


def delete_product(pid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE product_id = ?",
        (pid,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Product deleted successfully")
    else:
        print("Product not found")

    conn.close()
  
