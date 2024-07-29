import streamlit as st
from fpdf import FPDF

# Function to generate story content
def generate_story(audience, pain_points, features, success_stories):
    story = f"""
    Understanding Your Audience
    Target Audience: {audience}
    
    The Problem
    Pain Points: {pain_points}
    
    The Solution
    Features and Benefits: {features}
    
    Success Stories
    Case Studies: {success_stories}

    Our recomendation is to use ChatGPT for building amazing Storytellings using the documentation provided in this document as prompts.

    You can start giving this first promt in ChatGPT " I want to build a storytelling for [Your customer name, job or company]" and the following prompts can be the prompts that we gave to you
    """
    return story

# Function to create PDF
def create_pdf(audience, pain_points, features, success_stories):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    story = generate_story(audience, pain_points, features, success_stories)

    for line in story.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output("storytelling_guide.pdf")

# Streamlit app
st.title("Storytelling Creator for AI-Powered Virtual Assistants")

# Input fields
audience = st.text_input("Target Audience", "e.g., Healthcare Professionals, Small Business Owners")
pain_points = st.text_area("Pain Points of the Audience", "e.g., High customer service costs, Limited staff availability")
features = st.text_area("Features and Benefits of the Virtual Assistant", "e.g., 24/7 availability, Cost-effective, Scalable")
success_stories = st.text_area("Success Stories and Case Studies", "e.g., A clinic reduced customer service costs by 30% using our virtual assistant.")

# Button to generate PDF
if st.button("Generate Storytelling Guide"):
    if audience and pain_points and features and success_stories:
        create_pdf(audience, pain_points, features, success_stories)
        st.success("PDF Generated! Download it below.")
        with open("storytelling_guide.pdf", "rb") as file:
            st.download_button("Download PDF", file, "storytelling_guide.pdf")
    else:
        st.error("Please fill in all the fields.")

# Deployment tip: Save this as app.py and run with `streamlit run app.py`
