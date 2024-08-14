import streamlit as st
import streamlit.components.v1 as components
#css = """
#<style>
#@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');
#html, body  {
#    font-family: 'Rubik', sans-serif;
#    font-optical-sizing: auto;
#    font-weight: <weight>;
#    font-style: normal;
#}
#</style>"""
#st.markdown(css, unsafe_allow_html=True)

# Inject custom CSS and JavaScript for fade-in and slide-in animations
components.html("")

def show():

    #doesn't work nav_bar css styling covered it
    #st.logo(
    #    image="images/TumorVision.jpg",
    #)
    st.write("#")

    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.write("")

    with col2:
        st.markdown("<p style='text-align: right; font-size: 55px; font:Rubik;font-weight:bold;'>Welcome to <span style= color:#3c6ca8; font-style:italic;>TumorVision</span></p>", unsafe_allow_html=True)

        col4, col5, col6 = st.columns([2,3,2])

        with col4:
            st.write("")

        with col5:
            st.image("assets/TumorVision.png")

        with col6:
            st.write("")


        #st.markdown(f"""<h2 style='text-align: left; font-size: 18px; font-weight:bold; font: Rubik; >
        st.markdown("""
        <style>
            .custom-text {
                line-height: 2.0; 
                font-size: 20px;  
            }
            .custom-text span {
                color: #3c6ca8;
                font-weight: bold;
            }
        </style>
        <p class="custom-text fade-slide-in-element">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We are <span>TumorVision</span>, an innovative initiative committed to supporting healthcare professionals in the diagnosis of brain tumors through the utilization of advanced machine learning models.
        </p>
        <br>
        
        """, unsafe_allow_html=True)

        # Insert the SVG image here using st.image
        col10, col11,= st.columns([0.55, 0.45])
        with col10:
            st.markdown("""
            <p class="custom-text fade-slide-in-element">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our mission is to enhance patient outcomes by safeguarding individuals against terminal illnesses and adverse conditions. TumorVision goes beyond the conventional framework of an AI tool; it constitutes a crucial initial step in the treatment process, with the potential to meaningfully alleviate disease by enabling prompt and accurate diagnoses.
            </p>
            <br>
            """,unsafe_allow_html=True)

        with col11:
            st.image("assets/model3d.jpg")


        
        #st.button("Try Our App",type="primary",on_click= switch_page('TumorVision')) //this no work

        st.markdown("<p style='text-align: center; font-size: 35px; font-weight:bold; text-decoration: underline;'>Key Features</p>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .flex-container {
            display: flex;
            justify-content: space-around;
            gap: 20px;
        }
        .custom-box {
            border: 2px solid #3c6ca8;
            border-radius: 12px;
            padding: 20px;
            background-color: #f9f9f9;
            height: 310px; /* Adjust the height as needed */
            width: 250px; /* Adjust the width as needed */
            display: flex;
            align-items: center;
            justify-content: space-around;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .custom-box p {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #3c6ca8;
            margin: 0;
        }
        </style>
        """, unsafe_allow_html=True)

        col7, col8, col9= st.columns([1, 1, 1], gap="medium")
        with col7:
            st.markdown("""
                <div class="flex-container">
                    <div class="custom-box">
                        <p>Utilizes advanced machine learning algorithms</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        with col8:
            st.markdown("""
                <div class="flex-container">
                    <div class="custom-box">
                        <p>Rapid and accurate tumor identification</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        with col9:
            st.markdown("""
                <div class="flex-container">
                    <div class="custom-box">
                        <p>User-friendly interface for easy image upload and results</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
        st.markdown("""
        <br>
        <br>
        <p class="custom-text fade-slide-in-element">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Moreover, our model has demonstrated exceptional reliability, achieving an accuracy rate that exceeds 95% on our current classification datasets, which enables healthcare professionals to confidently rely on our system.
        </p>
        """, unsafe_allow_html=True)

        #st.write("""Stay safe and informed with TumorVision!""")

        #st.info("This is the Home page demo. You can customize this content with more information about your project.")

    with col3:
        st.write("")




if __name__ == "__main__":
    show()
