import streamlit as st

def show():

    st.write("#")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")

    with col2:
    
        st.markdown("""
            <p style='text-align: left; font:sans-serif; font-size: 38px; font-weight:bold;'>Tumor Type Infomations</p>""",unsafe_allow_html=True)

        st.markdown("""
            <p style='text-align: left; font:sans-serif; font-size: 25px;'>These are all the current type of tumors in the <span style=color:#3c6ca8;>BTIS</span> database that we can detect</p>""",unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(
            """
            <style>
            .tumor-title {
                font-size: 19.5px;
                font-weight: bold;
            }
            .tumor-image-container {
                display: flex;
                justify-content: space-evenly;
                flex-wrap: wrap;
            }
            .tumor-image {
                height: 200px; /* Set a fixed height */
                object-fit: cover; /* Scale image to fit the height, cropping if necessary */
                width: 100%;
            }
            .tumor-description {
                font-size: 16px;
                text-indent: 40px; 
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        tumor_info = {
            "Astrocytoma": "A type of tumor that originates from astrocytes, which are star-shaped glial cells in the brain and spinal cord. Astrocytomas can range from low-grade (slow-growing) to high-grade (fast-growing and malignant).",
            "Carcinoma": "A type of cancer that originates in the epithelial cells, which line the inside and outside surfaces of the body. Carcinomas can occur in many parts of the body, such as the skin, lungs, breast, and gastrointestinal tract.",
            "Ependymoma": "A tumor that arises from ependymal cells lining the ventricles of the brain and the central canal of the spinal cord. Ependymomas can occur in both children and adults, with varying degrees of aggressiveness.",
            "Ganglioglioma": "A rare type of brain tumor that arises from ganglion cells (a type of neuron) and glial cells. Gangliogliomas are generally slow-growing and considered low-grade.",
            "Germinoma": "A type of germ cell tumor that most commonly occurs in the brain, particularly in the pineal and suprasellar regions. Germinomas are usually highly sensitive to radiation therapy and have a good prognosis with treatment.",
            "Glioblastoma": "The most aggressive type of primary brain tumor, also known as glioblastoma multiforme (GBM). It originates from astrocytes and is characterized by rapid growth and a tendency to spread quickly within the brain.",
            "Granuloma": "A small area of inflammation caused by the accumulation of immune cells. Granulomas can form in response to infections, inflammation, or foreign substances, and are often found in conditions such as tuberculosis or sarcoidosis.",
            "Medulloblastoma": "A type of malignant brain tumor that primarily affects children and arises in the cerebellum or posterior fossa. Medulloblastomas are fast-growing and can spread to other parts of the brain and spinal cord.",
            "Meningioma": "A tumor that arises from the meninges, the membranes that surround the brain and spinal cord. Meningiomas are usually benign and slow-growing, but in some cases, they can be atypical or malignant.",
            "Neurocytoma": "A rare, typically benign tumor that arises from neurons, usually in the ventricular system of the brain. Central neurocytomas are the most common subtype and are generally considered low-grade.",
            "Oligodendroglioma": "A type of glioma that originates from oligodendrocytes, which are cells that produce the myelin sheath around nerve fibers in the brain. Oligodendrogliomas are usually slow-growing but can become more aggressive over time.",
            "Papilloma": "A benign tumor that arises from epithelial cells and forms a wart-like growth. Papillomas can occur in various parts of the body, including the skin, bladder, and respiratory tract.",
            "Schwannoma": "A usually benign tumor that arises from Schwann cells, which form the protective covering around nerve fibers. Schwannomas can occur anywhere in the body but are most commonly found on the peripheral nerves.",
            "Tuberculoma": "A granulomatous lesion caused by the Mycobacterium tuberculosis infection, most commonly found in the brain or lungs. Tuberculomas can cause symptoms depending on their location and are often associated with tuberculosis."
        }

        tumor_images = {
            "Astrocytoma": ["assets/tumorimages/path_to_astrocytoma_image1.jpg",     "assets/tumorimages/path_to_astrocytoma_image2.jpg", "assets/tumorimages/path_to_astrocytoma_image3.jpg"],
            "Carcinoma": ["assets/tumorimages/path_to_carcinoma_image1.jpg", "assets/tumorimages/path_to_carcinoma_image2.jpg", "assets/tumorimages/path_to_carcinoma_image3.png"],
            "Ependymoma": ["assets/tumorimages/path_to_ependymoma_image1.jpg", "assets/tumorimages/path_to_ependymoma_image2.png", "assets/tumorimages/path_to_ependymoma_image3.jpeg"],
            "Ganglioglioma": ["assets/tumorimages/path_to_ganglioglioma_image1.jpeg", "assets/tumorimages/path_to_ganglioglioma_image2.jpg", "assets/tumorimages/path_to_ganglioglioma_image3.jpg"],
            "Germinoma": ["assets/tumorimages/path_to_germinoma_image1.jpeg", "assets/tumorimages/path_to_germinoma_image2.jpeg", "assets/tumorimages/path_to_germinoma_image3.jpeg"],
            "Glioblastoma": ["assets/tumorimages/path_to_glioblastoma_image1.jpeg", "assets/tumorimages/path_to_glioblastoma_image2.jpeg", "assets/tumorimages/path_to_glioblastoma_image3.jpeg"],
            "Granuloma": ["assets/tumorimages/path_to_granuloma_image1.jpeg", "assets/tumorimages/path_to_granuloma_image2.jpg", "assets/tumorimages/path_to_granuloma_image3.jpg"],
            "Medulloblastoma": ["assets/tumorimages/path_to_medulloblastoma_image1.jpg", "assets/tumorimages/path_to_medulloblastoma_image2.jpg", "assets/tumorimages/path_to_medulloblastoma_image3.jpg"],
            "Meningioma": ["assets/tumorimages/path_to_meningioma_image1.jpg", "assets/tumorimages/path_to_meningioma_image2.jpg", "assets/tumorimages/path_to_meningioma_image3.jpg"],
            "Neurocytoma": ["assets/tumorimages/path_to_neurocytoma_image1.jpg", "assets/tumorimages/path_to_neurocytoma_image2.jpg", "assets/tumorimages/path_to_neurocytoma_image3.jpg"],
            "Oligodendroglioma": ["assets/tumorimages/path_to_oligodendroglioma_image1.jpg", "assets/tumorimages/path_to_oligodendroglioma_image2.jpg", "assets/tumorimages/path_to_oligodendroglioma_image3.jpg"],
            "Papilloma": ["assets/tumorimages/path_to_papilloma_image1.jpg", "assets/tumorimages/path_to_papilloma_image2.jpg", "assets/tumorimages/path_to_papilloma_image3.jpg"],
            "Schwannoma": ["assets/tumorimages/path_to_schwannoma_image1.jpg", "assets/tumorimages/path_to_schwannoma_image2.jpg", "assets/tumorimages/path_to_schwannoma_image3.jpg"],
            "Tuberculoma": ["assets/tumorimages/path_to_tuberculoma_image1.jpg", "assets/tumorimages/path_to_tuberculoma_image2.jpg", "assets/tumorimages/path_to_tuberculoma_image3.jpg"]
        }

        image_width = 250   
        
        for tumor, description in tumor_info.items():
            st.markdown(f'<div class="tumor-title">{tumor}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="tumor-description">{description}</div>', unsafe_allow_html=True)
            st.markdown("---")
            
            image_columns = st.columns(3)
            for i, col in enumerate(image_columns):
                if i < len(tumor_images[tumor]):  #original: width=image_width
                    col.image(tumor_images[tumor][i], use_column_width="always",)
            st.markdown("---")
            st.write("")
        

    with col3:
        st.write("")


if __name__ == "__main__":
    show()
 
