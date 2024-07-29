import streamlit as st

def app():
    if st.sidebar.button('Botarmy Marketplace'):
        link = 'https://botarmy-marketplace.streamlit.app/'
        st.sidebar.markdown(f"[Marketplace]({link})", unsafe_allow_html=True)
    
    st.warning("Hello, Premium partner! Welcome to the BOTARMY_HUB_PLATFORM.")
    st.info("We are excited to have you here. Check our newest resources, tutorials and courses and become an expert into AI based tools!")
    
    st.container()  # Remove height and border as they are not valid parameters for st.container
    st.markdown("Here you will find your personalized chat to show to potential customers and courses and sub apps to help you in your career as _AI based tools development agency_!")
    
    # Define the URL
    urlchat = 'https://aiprofilevcard.streamlit.app/'
    # Create a button that renders a Markdown link
    if st.button('Personalized chat to show'):
        st.markdown(f"[Click here to show the chat]({urlchat})")
    with st.expander('Premium tier information, :red[read carefully]'):
        st.warning("You will be able to sell and perform project managing apps, knowledge base creation apps, Notion documents, data administration tools management and a lot of amazing apps that will grow your portfolio")
        st.info("Every relation between you and Botarmy-hub will be remote via WhatsApp or Zoom, mostly because we are an international company")
        st.warning("The payments or economic obligations will be as electronic transfer between partners accounts and our international accounts")
    
    st.header("Tools for premium members")
    col1,col2,col3 = st.columns(3)
    with col1:
        # Display the PDF file
        pdf_file_path = 'Notion_course.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Download Notion Course PDF", data=PDFbyte, file_name=pdf_file_path, mime='application/octet-stream')
    
    with col2:
        url_knowledge_base = "https://knowledge-base-builder.streamlit.app/"
        if st.button('Knowledge base creator'):
            st.markdown(f"[Click here to show the app]({url_knowledge_base})")

    with col3:
        url_task_manager = "https://taskforge.streamlit.app/"
        if st.button('Task managing app'):
            st.markdown(f"[Click here to show the app]({url_task_manager})")


# Run the app
if __name__ == "__main__":
    app()
