import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="My first Streamlit website", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

img_spock = Image.open("images/spock.jpg")
img_scotty = Image.open("images/scotty.jpg")

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

    with st.container():
        st.write("---")
        st.header("Second section")
        st.write("##")

        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_spock)
        with text_column:
            st.subheader("A column for text")
            st.write(
                """
                Now all the other gods and men, lords of chariots, slumbered the whole night through, 
                but Zeus was not holden of sweet sleep, 
                for he was pondering in his heart how he might do honour to Achilles 
                and lay many low beside the ships of the Achaeans. 
                And this plan seemed to his mind the best, [5] to send to Agamemnon, 
                son of Atreus, a baneful dream. 
                """
            )
            st.markdown("[Iliad Book 2](http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D2)")

        st.write("##")
        text_column, image_column = st.columns((1,2))
        with image_column:
            st.image(img_scotty)
        with text_column:
            st.subheader("A second column for text")
            st.write(
                """
                Now when they were marshalled, the several companies with their captains, the Trojans came on with clamour 
                and with a cry like birds, even as the clamour of cranes ariseth before the face of heaven, 
                when they flee from wintry storms and measureless rain, [5] and with clamour fly toward the streams of Ocean, bearing slaughter and death to Pigmy men, and in the early dawn they offer evil battle.
                """
            )
            st.markdown("[Iliad Book 3](http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D3)")

        with st.container():
            st.write("---")
            st.write("Contact Form")
            st.write("##")

            contact_form = """
                <form action="https://formsubmit.co/felidaesrule@yahoo.com" method="POST">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" placeholder="Your message" required></textarea>
                    <button type="submit">Send</button>
                </form>
            """

            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()