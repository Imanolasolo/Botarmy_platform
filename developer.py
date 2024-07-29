import streamlit as st

def app():
    if st.sidebar.button('Botarmy Marketplace'):
        link = 'https://botarmy-marketplace.streamlit.app/'
        st.sidebar.markdown(f"[Marketplace]({link})", unsafe_allow_html=True)


    st.warning("Hello, Developer! Welcome to the BOTARMY_HUB_PLATFORM.")
    st.info("Here you will find the resources and knowledge to develop AI based tools like a pro!")
    
    with st.expander("Botarmy4devs info"):
        st.write("The next app is a sample for Botarmy capabilities to present different bots in one app")
        st.write("You can use this app to create different backend projects with the assistance of different language bots")

    col1,col2 = st.columns(2)
    with col1:
        botarmy4devs = "https://botarmy-backend-dev.streamlit.app/"
        if st.button('Botarmy4devs app'):
            st.markdown(f"[Click here to show the app]({botarmy4devs})")

    with col2:
        whatsapp_number = "+5930993513082"
        whatsapp_message = "I have a possible customer in developer"
        whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message}"

        if st.button("Developer whatssap Channel"):
            st.markdown(f"""
                <a href="{whatsapp_url}" target="_blank">
                    <button>Developer whatssap channel</button>
                </a>
            """, unsafe_allow_html=True)   

    