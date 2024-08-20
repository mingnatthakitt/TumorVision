import streamlit as st

def show():

    st.write("#")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")

    with col2:
    
        st.title("Tumor Type Infomations",anchor=False)

        st.write("This is all the current type of tumors in the database.")
        st.write("The current tumor types we can detect are: ")
        st.write("""
        - Astrocitoma 
        - Carcinoma 
        - Ependimoma 
        - Ganglioglioma 
        - Germinoma
        - Glioblastoma
        - Granuloma
        - Meduloblastoma 
        - Meningioma
        - Neurocitoma
        - Oligodendroglioma
        - Papiloma 
        - Schwannoma
        - Tuberculoma
        - Normal(No tumor)
        """)

    with col3:
        st.write("")


if __name__ == "__main__":
    show()
