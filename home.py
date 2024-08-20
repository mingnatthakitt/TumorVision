import streamlit as st
import streamlit.components.v1 as components


def show():

    st.write("#")

    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.write("")

    with col2:
        st.markdown("<p style='text-align: right; font-size: 48px; font-weight:bold;'>Welcome to <span style= color:#3c6ca8; font-style:italic;>TumorVision</span></p>", unsafe_allow_html=True)

        col4, col5, col6 = st.columns([2,3,2])

        with col4:
            st.write("")

        with col5:
            st.image("assets/TumorVision.png")

        with col6:
            st.write("")


        st.markdown("""
        <style>
            .custom-text {
                line-height: 1.5; 
                font-size: 19.5px;  
            }
            .custom-text span {
                color: #3c6ca8;
                font-weight: bold;
            }
            .custom-text blue {
                color: #3c6ca8;
            }
            .custom-text strong {
                font-weight: bold;
            }
            .custom-text line {
                text-decoration: underline; 
            }
            .custom-text strongnline {
                font-weight: bold;
                text-decoration: underline;   
            }
            .custom-text mission {
                font-size: 30px;
            }d
            .custom-text redirect {
                font-size: 22px;
            }
            .small-text {
                line-height: 1.6;
                font-size: 17.2px;   
            }
        </style>
        <p class="custom-text">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; At <span>TumorVision</span>, we are pioneering the future of medical diagnostics. Our innovative initiative harnesses the power of cutting-edge machine learning models to support healthcare professionals in the critical task of brain tumor diagnosis. By bridging the gap between artificial intelligence and medical expertise, we're setting new standards in early detection and patient care.
        </p>
        <br>

        """, unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: left; font-size: 25px; font-weight:bold;'>
        To try out our service please go the the dedicated <span style= color:#3c6ca8; >TumorVision </span> page
        </p><br><br>
        """, unsafe_allow_html=True)


        col10, col11,= st.columns([0.55, 0.45])
        with col10:
            st.markdown("""
            <p class="custom-text"> 
                <mission><blue>Our Mission</blue></mission>
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TumorVision is more than just an AI tool - it's a lifeline in the fight against terminal illnesses. Our mission have twofolds:
                <br>         
            </p>
            <p class="custom-text">
                <strong>1) Enhance Patient Outcomes</strong>: 
                <br>       
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; By providing rapid and accurate diagnoses, we aim to significantly improve the prognosis for individuals facing potential brain tumors.
                <br>
                <br>
                <strong>2) Empower Healthcare Professionals</strong>: 
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We equip medical experts with state-of-the-art technology, allowing them to make informed decisions with unprecedented speed and precision. 
                <br>
                Our system serves as a crucial first step in the treatment process, potentially alleviating the impact of disease through early intervention and tailored care plans.    
            </p>
            <br>
            """,unsafe_allow_html=True)

        with col11:
            st.image("assets/model3d.jpg")




        st.markdown("<p style='text-align: center; font-size: 30px; font-weight:bold; text-decoration: underline;'>Key Features</p>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .flex-container {
            display: flex;
            justify-content: space-evenly;
            gap: 0px;
        }

        .custom-box {
            border: 2px solid #3c6ca8;
            border-radius: 12px;
            padding: 20px;
            background-color: #f9f9f9;
            height: 300px; /* Adjust the height as needed */
            width: 250px; /* Adjust the width as needed */
            display: flex;
            align-items: center;
            justify-content: space-evenly;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .custom-box p {
            text-align: center;
            font-size: 22px;
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
        <p class="custom-text">
        <mission>Why Choose <span>TumorVision?</span></mission>
        <br>
        </p>
        <p class="small-text">
        &nbsp;&nbsp;&nbsp;&nbsp;&#x2022; <strong>Cutting-Edge Technology :</strong> Our AI models are built on the latest advancements in machine learning and medical imaging.
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&#x2022; <strong>Time Efficiency :</strong> Rapid diagnosis allows for quicker treatment initiation, potentially saving crucial time in critical cases.
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&#x2022; <strong>Support for Medical Professionals :</strong> We augment the expertise of healthcare providers, offering an additional layer of diagnostic confidence.         
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&#x2022; <strong>Ongoing Research and Development :</strong> Our commitment to innovation means we're constantly improving our model and expanding our capabilities.         
        </p> """, unsafe_allow_html=True)


    with col3:
        st.write("")




if __name__ == "__main__":
    show()
