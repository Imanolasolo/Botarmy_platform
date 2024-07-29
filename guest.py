import streamlit as st

def app():
    if st.sidebar.button('Botarmy Marketplace'):
        link = 'https://botarmy-marketplace.streamlit.app/'
        st.sidebar.markdown(f"[Marketplace]({link})", unsafe_allow_html=True)

    st.title("Welcome to BOTARMY_HUB_PLATFORM")
    st.warning("Hello, Guest! Welcome to the BOTARMY_HUB_PLATFORM.")
    st.info("We are excited to have you here. Check our videos to know more about Botarmy_hub and how we can collaborate in this amazing opportunity for all of us!")

    st.subheader("Featured Videos")
    
    # List of video URLs (You can replace these with your actual video URLs)
    video_urls = [
        "https://youtu.be/SnY1XlV3gvc",  # Video 1
        "https://youtu.be/p7aAkt-FcXY",  # Video 2
        "https://youtu.be/YPVRiRgCIPI",  # Video 3
       
    ]
    
    # Display each video
    for idx, video_url in enumerate(video_urls):
        st.video(video_url)
        st.write(f"Video {idx + 1}")

    # Personal message to the guest
    st.subheader("Join Us for a Zoom Session")
    st.write("""
        If you enjoyed the videos and would like to learn more about the amazing opportunities we offer, we would love to invite you to a Zoom session.
        During this session, we will explain the benefits of joining BOTARMY_HUB_PLATFORM, the membership costs, and the various options available to you.
        
        Please reach out to us to schedule a convenient time for the Zoom meeting. We look forward to speaking with you!
        
        **Contact Information:**
    """)

    whatsapp_number = "+5930993513082"
    whatsapp_message = "I want more info about BOTARMY_HUB"
    whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={whatsapp_message}"

    if st.button("Contact Us via WhatsApp"):
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank">
                <button>Contact Us via WhatsApp</button>
            </a>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
