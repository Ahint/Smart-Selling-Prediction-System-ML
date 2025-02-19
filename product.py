import streamlit as st
import sqlite3
import pandas as pd

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
    df = pd.read_sql_query('SELECT * FROM products', conn)
    conn.close()
    return df

# Main function for product management
def main():
    st.title("Product Management")
    
    create_table()
    
    with st.form("product_form"):
        name = st.text_input("Product Name")
        category = st.text_input("Product Category")
        submitted = st.form_submit_button("Add Product")
        if submitted:
            add_product(name, category)
            st.success("Product added successfully!")
    
    st.subheader("Product List")
    products_df = get_products()
    st.dataframe(products_df)
    
    with st.form("delete_form"):
        product_id = st.number_input("Product ID to delete", min_value=1)
        submitted = st.form_submit_button("Delete Product")
        if submitted:
            delete_product(product_id)
            st.success("Product deleted successfully!")
    
    if st.button("Clear All Products"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products')
        conn.commit()
        conn.close()
        st.success("All products cleared!")