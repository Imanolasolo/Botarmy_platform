import streamlit as st
import json

# Importar las páginas que vas a utilizar
import admin, basic, premium, developer, guest

# Cargar usuarios desde users.json
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

users = load_users()

# Función para autenticar usuarios
def authenticate(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

# Page name and icon
st.set_page_config(page_title="Botarmy_platform", page_icon=":toolbox:")
# Sidebar navigation
st.sidebar.title("BOTARMY_HUB_PLATFORM")
st.sidebar.subheader("Navigation")

# Variables de estado de Streamlit para mantener la sesión del usuario
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Botón para entrar como invitado
if st.sidebar.button("Enter as Guest"):
    st.session_state.authenticated = True
    st.session_state.current_user = {"name": "Guest", "role": "guest"}
    st.sidebar.success("Logged in as Guest!")

# Formulario de Login en el sidebar, sin permitir login como guest
if not st.session_state.authenticated:
    col1, col2 = st.columns([1,4])
    with col1:
        st.image('Botarmy_logo.png', width=100)
    with col2:
        st.title("Welcome to :red[BOTARMY_HUB] platform")
    st.info("We are _Botarmy_Hub_ your platform to become a profitable AI based tools development agency")
    with st.expander("Botarmy_Platform provided services"):
        st.text('''
1. Reseller tier:
   - Access to basic tools for AI development.
   - Basic formation resources and tutorials to become a successful AI agency.
   - Limited technical support.

2. Premium tier:
   - Access to advanced AI development tools (personalized chatbot).
   - Advanced training resources and tutorials.
   - Premium technical support.
   - Acces to exclusive resources  and premium updates.

3. Developer tier:
   - Access to development environments, APi and libraries.
   - AI projects development collaboration.
   - Specific resources and tutorials for developers.

4. Guest:
   - Limited access to information and introductory resources about platform.
   - Video explanation about differen tiers.
   - General information about how to become a AI based tools development agency.
''')
    
    st.sidebar.write("Please login to access the platform.")
    username = st.sidebar.text_input("Username", key="username")
    password = st.sidebar.text_input("Password", type="password", key="password")
    if st.sidebar.button("LOGIN"):
        user = authenticate(username, password)
        if user and user["role"] != "guest":  # No permitir login como guest
            st.session_state.authenticated = True
            st.session_state.current_user = user
            st.sidebar.success(f"Welcome, {user['name']}!")
        else:
            st.sidebar.error("Invalid username or password, or login as guest is not allowed.")
else:
    st.sidebar.write(f"Logged in as {st.session_state.current_user['name']}")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.current_user = None

# Redirigir a la página correspondiente según el rol del usuario autenticado
if st.session_state.authenticated:
    role = st.session_state.current_user["role"]
    if role == "admin":
        admin.app()
    elif role == "basic":
        basic.app()
    elif role == "premium":
        premium.app()
    elif role == "developer":
        developer.app()
    elif role == "guest":
        guest.app()
else:
    st.warning("Please log in the sidebar area with your credentials to access the platform.")
    st.success("If it´s your first time enter as :red[guest] and enjoy the info that we built for you!")

