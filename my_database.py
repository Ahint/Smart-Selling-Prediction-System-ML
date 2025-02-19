import sqlite3

# Database connection
def get_db_connection():
    conn = sqlite3.connect('products.db')
    return conn

# Create products table if not exists
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add product
def add_product(name, category):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, category) VALUES (?, ?)', (name, category))
    conn.commit()
    conn.close()

# Delete product
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

# Get all products
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products