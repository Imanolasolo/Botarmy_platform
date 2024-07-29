import streamlit as st
import json

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def app():
    users = load_users()
    
    if st.sidebar.button('Botarmy Marketplace'):
        link = 'https://botarmy-marketplace.streamlit.app/'
        st.sidebar.markdown(f"[Marketplace]({link})", unsafe_allow_html=True)

    st.title("Admin Page")

    st.header("Existing Users")
    for user in users:
        st.write(f"Name: {user['name']}, Role: {user['role']}")

    st.header("Add New User")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    new_role = st.selectbox("New Role", ["basic", "premium", "developer", "guest"])

    if st.button("Add User"):
        new_user = {
            "name": new_username,
            "password": new_password,
            "role": new_role
        }
        users.append(new_user)
        save_users(users)
        st.success("User added successfully")

    st.header("Update or Delete User")
    username_to_modify = st.selectbox("Select User to Modify", [user['name'] for user in users if user['name'] != 'admin'])

    if username_to_modify:
        selected_user = next((user for user in users if user['name'] == username_to_modify), None)
        if selected_user:
            new_username = st.text_input("Update Username", selected_user['name'])
            new_password = st.text_input("Update Password", selected_user['password'], type="password")
            new_role = st.selectbox("Update Role", ["basic", "premium", "developer", "guest"], index=["basic", "premium", "developer", "guest"].index(selected_user['role']))

            if st.button("Update User"):
                selected_user['name'] = new_username
                selected_user['password'] = new_password
                selected_user['role'] = new_role
                save_users(users)
                st.success("User updated successfully")

            if st.button("Delete User"):
                users = [user for user in users if user['name'] != selected_user['name']]
                save_users(users)
                st.success("User deleted successfully")
