import streamlit as st
from streamlit_option_menu import option_menu
import general_ehr_generator
import generate_synthetic_records_userip
import medical_image_synthesizer
import personalized_treatment
import home

# Set page configuration
st.set_page_config(page_title="Medical Analysis Tool", page_icon=":hospital:", layout="wide")

# CSS for dark theme
def render_dark_theme():
    st.markdown("""
        <style>
        /* Set the background color for the whole page */
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }

        /* Set the background color and style for the header */
        .header {
            background-color: #444444;
            padding: 10px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        /* Style for the navigation links in the header */
        .header a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            padding: 8px 16px;
            transition: background-color 0.3s, color 0.3s;
            border-radius: 5px;
        }

        .header a:hover {
            background-color: #55C667;
            color: white;
        }

        /* Sidebar and option menu background styling */
        .css-1d391kg {  /* Sidebar */
            background-color: #1e1e1e !important;
        }

        /* Button styling */
        .stButton>button {
            background-color: #00aaff;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 12em;
            margin: 30px auto;
            display: block;
        }

        .stButton>button:hover {
            background-color: #55C667;
            color: white;
        }

        /* Main page link text styling */
        h1, h2, h3, h4, h5, h6, p, div, span {
            color: white !important;  /* Ensures text is white */
        }
        
        /* Custom styling for any other divs or containers */
        .block-container {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# Function to render the header and sidebar
def render_header():
    st.markdown("""
        <div class="header">
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact Us</a>
        </div>
    """, unsafe_allow_html=True)

# Function to render the main application with sidebar
def run_main_app():
    render_header()

    with st.sidebar:
        selected_page = option_menu(
            menu_title='Medical Analysis Tool',  # Title for the sidebar
            options=['Personalized Medical Treatment', 'Medical Image Synthesizer', 'Health Records Synthesizer'],  # Menu options
            icons=['stethoscope', 'image', 'folder'],  # Corresponding icons for each option
            menu_icon='activity',  # Sidebar icon
            default_index=0,  # Default selected menu
            styles={
                "container": {"padding": "5px", "background-color": '#1e1e1e'},
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {
                    "color": "white", 
                    "font-size": "18px", 
                    "text-align": "left", 
                    "margin": "0px", 
                    "--hover-color": "#444444"
                },
                "nav-link-selected": {"background-color": "#00aaff"},
            }
        )

    # Linking pages based on selection
    if selected_page == 'Personalized Medical Treatment':
        personalized_treatment.app()  # Calls the function from personalized_treatment.py
    elif selected_page == 'Medical Image Synthesizer':
        medical_image_synthesizer.app()  # Call the function from generate_synthetic_records_userip.py
    elif selected_page == 'Health Records Synthesizer':
        general_ehr_generator.app()  # Call the function from general_ehr_generator.py

# Main flow control
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Check if the session is still on the home page or if the user clicked on a button
if st.session_state["page"] == "home":
    next_action = home.home_page()
    if next_action == "main":
        st.session_state["page"] = "main"  # Change session state to the main app
elif st.session_state["page"] == "main":
    render_dark_theme()  # Call the dark theme function
    run_main_app()
