import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo
from PIL import Image

# Set page layout to wide
st.set_page_config(layout="wide")

#Remove Streamlit Padding
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:1rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)


# Mini Nav Bar (Hyperlinks)
st.markdown(
    """
    <style>
    .mini-navbar-container {
        display: flex;
        justify-content: flex-end;  /* Aligns the mini navbar items to the right */
        background-color: #f2f2f2;
        padding: 5px 10px;
        font-size: 14px;
    }
    .mini-navbar-container a {
        margin-left: 20px;
        color: #B10060;
        text-decoration: none;
    }
    .mini-navbar-container a:hover {
        text-decoration: underline;
        color: #00838F;
    }
    </style>
    <div class="mini-navbar-container">
        <a href="https://oiawebsite.example.com">Return to OIA Website</a>
        <a href="#accessibility">Accessibility</a>
        <a href="#contact">Contact Us</a>
        <a href="#cymraeg">Cymraeg</a>
    </div>
    """,
    unsafe_allow_html=True
)





# Nav Bar
selected = option_menu(
    menu_title=None,
    options=["Annual Statements Home Page", "View Providers by OIA Banding", "Definitions"],
    icons=["house", "pencil", "file-word"],
    menu_icon="case",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "#B10060",
            "width": "100%",
        },
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "padding": "10px 20px",
            "border-radius": "5px",
            "width": "100%",
            "height": "100%",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "--hover-color": "#00838F",
            "color": "white",
        },
        "nav-link-hover": {
            "background-color": "#00838F",
            "color": "white",
        },
        "nav-link-selected": {
            "background-color": "#00838F",
            "color": "white",
        },
    }
)
st.write("----")



if selected == "Annual Statements Home Page":
    st.write("Welcome to our Annual Statements page. Each year, we publish information about our members' records in handling complaints and appeals for the preceding calendar year. This is so that:")
    st.write("1. more information is available to the public about higher education complaints;")
    st.write("2. students can have greater confidence in complaints handling processes;")
    st.write("3. providers can look at their own record alongside that of similar providers; and")
    st.write("4. we are open about our own processes.")

    st.write("You can view information about individual providers, compare a provider’s record over different years, and compare the record of one provider with other similar providers. The statements provide useful information about complaints and appeals that have reached the end of internal processes at higher education providers and come to us, but the information should be considered in context and interpreted with some caution (see also About Annual Statements).We encourage each provider to share the information in its Annual Statement at appropriate levels within its structure, including at governance level, and with its student representative body or student representatives.On this page you can find Annual Statements for the last five years, where available.We hope that you find the information in our Annual Statements useful.")
    st.write("----")

# Your content below the navbar
