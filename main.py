import streamlit as st
import langchain_code

st.title("Restaurant Name Generator")

# Sidebar selection for cuisine
cuisine = st.sidebar.selectbox("Pick a cuisine", ("South Indian", "North Indian", "Odisha", "Western"))

if cuisine:
    response = langchain_code.generate_name(cuisine)
    
    # Display restaurant name
    st.header(response['restaurant_name'].strip())

    # Display menu items
    menu_items = [item.strip() for item in response['menu_items'].split(",")]
    st.markdown("### Menu Items")
    for item in menu_items:
        st.write(f"- {item}")