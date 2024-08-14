import streamlit as st
#from streamlit_extras.app_logo import add_logo
from streamlit_navigation_bar import st_navbar
from streamlit_extras.switch_page_button import switch_page
import home
import TumorVision
import Tumorinfo

st.set_page_config(page_title="TumorVision", layout="wide", page_icon="🧠"
                  )

def load_nav_bar():
    pages = ["Home", "TumorVision","Tumorinfo"]
    #logo_path = "assets/TumorVision.svg"
    styles = {
        "nav": {
            "background-color": "white",
            "height": "80px",
        },
        "img": {
            "padding-right": "1px",
        },
        "span": {
            "color": "black",
            "font-size": "16px",
            "padding": "17px",
            "font-weight": "bold",
            "border-radius": "0px",
        },
        "hover": {
            "color": "#3c6ca8",
            "font-weight": "bold",
            "text-decoration": "underline",
        },
        "active": {
            "color": "white",
            "padding": "15px",
            "border": "0px solid #101a2c",
            "background-color": "#3c6ca8",
            "border-radius": "15px",
        }
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
        "use_padding": True,
    }

    page = st_navbar(
        pages,
        styles=styles,
        #logo_path=logo_path,
        options=options,
    )
    return page

# Add logo(dosen't work again)
#add_logo("images/TumorVision.jpg", height=80)

# Load navigation bar
selected_page = load_nav_bar()

# Display the selected page
if selected_page == 'Home':
    home.show()
elif selected_page == 'TumorVision':
    TumorVision.show()
elif selected_page == 'Tumorinfo':
    Tumorinfo.show()
else:
    home.show()  # Default to Home page

#selected_page == 'Tumorinfo':