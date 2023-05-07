import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My first Streamlit website", page_icon=":tada:", layout="wide")

def load_lottie_animation(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    return response.json()

with st.container():
    st.subheader("In God We Trust :wave:")
    st.title("An example website using Streamlit")

with st.container():
    st.write("This is example text that is a paragraph")
    st.write("[The source code is in GitHub ](https://github.com/gilgamesh7/sttreamlit_example_website)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Some random stuff")
        st.write("##")
        st.write(
            """
            The wrath sing, goddess, of Peleus' son, Achilles, that destructive wrath which brought countless woes upon the Achaeans, 
            - and sent forth to Hades many valiant souls of heroes, and made them themselves spoil for dogs and every bird; 
            - thus the plan of Zeus came to fulfillment, [5] from the time when1 first they parted in strife Atreus' son, king of men, and brilliant Achilles. 
            - Who then of the gods was it that brought these two together to contend? 
            - The son of Leto and Zeus; for he in anger against the king roused throughout the host an evil pestilence, and the people began to perish, 
            
            [10] because upon the priest Chryses the son of Atreus had wrought dishonour. For he had come to the swift ships of the Achaeans to free his daughter, bearing ransom past counting; and in his hands he held the wreaths of Apollo who strikes from afar,2 on a staff of gold; and he implored all the Achaeans, [15] but most of all the two sons of Atreus, the marshallers of the people: “Sons of Atreus, and other well-greaved Achaeans, to you may the gods who have homes upon Olympus grant that you sack the city of Priam, and return safe to your homes; but my dear child release to me, and accept the ransom [20] out of reverence for the son of Zeus, Apollo who strikes from afar.”

            """
        )
        st.write("[Link to the Iliad Book 1](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D1)")

    with right_column:
        coding_animation_url = load_lottie_animation("https://assets3.lottiefiles.com/packages/lf20_4kx2q32n.json")
        st_lottie(coding_animation_url, height=300, key="coding")
