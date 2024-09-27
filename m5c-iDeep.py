import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

selected2 = option_menu(None, ["Home", "Predictor", "Dataset", "Citations"],
                        icons=['house', 'search', 'list-task', 'book'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

if selected2 == "Home":
    st.header("m5C-iDeep")
    #st.subheader("The DHU-Pred is a web-server for the prediction of Dihydrouridine in transfer RNA (tRNA) "
     #            "modifications.")
    st.write("2-O-methylation (2OM) refers here to the creation of a new functional group through the attachment of a methyl (-CH3) group to the second position of aromatic ring hydroxyl group (-OH). This change is one of the most frequently known post transcriptional modifications that were once found to appear at almost all types of RNA. It plays an active part of RNA’s physical configuration stability and the way; different RNA molecules interrelate. Further, this modification plays a pivotal role in changing epigenetic regulation of cellular process. Previous approaches like the mass spectrometry could not fully enhance the identification of RNA modified sites. Sequence data was useful in the development of measures that meant that the use of computationally intelligent system to quickly identify 2OM sites."
             )
    #image = Image.open('2OM.PNG')
    #st.image(image, width=400)

elif selected2 == "Predictor":
    #st.subheader("Predictor Page")
    import predictor

    exec(open('predictor.py').read())


elif selected2 == "Dataset":
    #st.subheader("Data Set")
    st.info("iRNA 5mc Dataset")
    with open("iRNA-5mc.rar", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="iRNA-5mc.rar",
            mime=""
        )
    st.info("m5c-Pred-XS")
    with open("m5c-pred-XS.rar", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="m5c-pred-XS.rar",
            mime=""
        )
