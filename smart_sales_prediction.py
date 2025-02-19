import streamlit as st
import product
import sales

# Main App
def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ("Product Management", "Sales Prediction"))

    if choice == "Product Management":
        product.main()
    elif choice == "Sales Prediction":
        sales.main()

if __name__ == "__main__":
    main()