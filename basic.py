import streamlit as st
import webbrowser

def app():
    if st.sidebar.button('Botarmy Marketplace'):
        link = 'https://botarmy-marketplace.streamlit.app/'
        st.sidebar.markdown(f"[Marketplace]({link})", unsafe_allow_html=True)

    st.warning("Hello, partner! Welcome to the BOTARMY_HUB_PLATFORM.")
    st.info("With these resources you will be able to promote and market AI based tools and perform a profitable career as AI Agency!")
    with st.expander("Reseller work process"):
        st.markdown("The objective of the reseller platform partner is to resell AI-based virtual assistants to their contacts, whether professional or personal.")
        st.markdown("For each paying customer brought by the basic partner, the partner will receive 50% of the price agreed with the final customer once he or she pays for the product.")
        st.markdown("This basic tier is suitable for anyone who wants to be a reseller partner and generate profit from the sale of virtual assistants based on AI, you only have to provide interested contacts, Botarmy does the rest of the work.")

    st.header("Tools for reseller tier")

    # Define the URL
    urlchat = 'https://botarmy-chat.streamlit.app/'
    # Define the URL for the customer management app
    urlcustomerapp = "https://basic-tier-contacts.streamlit.app/"

    col1, col2, col3 = st.columns(3)
    with col1:        
        # Create a button that renders a Markdown link
        if st.button('Basic user Sample to show'):
            st.markdown(f"[Click here to show the chat]({urlchat})")
    with col2:
        # New button for customer management app    
        # Create a button that renders a Markdown link
        if st.button('Customer managing app'):
            st.markdown(f"[Click here to show the app]({urlcustomerapp})")
    with col3:
        whatsapp_number = "+5930993513082"
        whatsapp_message = "I have a possible customer"
        whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message}"

        if st.button("Customer handling message"):
            st.markdown(f"""
                <a href="{whatsapp_url}" target="_blank">
                    <button>Customer handling message</button>
                </a>
            """, unsafe_allow_html=True)
    

    
