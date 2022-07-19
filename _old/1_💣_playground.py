from urllib.request import urlopen
import streamlit as st
import json
import time

st.set_page_config(
    page_title="FT-Ablauf-Visualizer",
    page_icon="👋",
    layout="wide",
    menu_items={"About": "von Gruppe 8"}
)

with open("style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title('FT-Ablauf-Visualizer')

st.subheader('Stellt sich ändernde Sensorausprägungen dar')

i = 0
url = urlopen("https://it2wi1.if-lab.de/rest/ft_ablauf")
data = json.loads(url.read())
# print(data[0]["werte"].keys())
# value = st.text_input("Bitte den auszulesenden Wert eingeben:")
# value = "H-horizontal"
keys = {"":""}
keys.update(data[0]["werte"])
value = st.selectbox("Bitte den auszulesenden Wert wählen:", keys)

if value != "":

    with st.spinner("Maschine arbeitet"):
        buffer = data[0]["werte"][value]
        for item in data:
            if buffer != item["werte"][value]:
                # print("Datum: " + item["datum"] + ", Wert: " + item["werte"][value])
                buffer = item["werte"][value]
                col1, col2 = st.columns(2)
                col1.write("Datum: " + item["datum"])
                col2.write("Wert: " + item["werte"][value])
                # st.write("Datum: " + col1 + ", Wert: " + item["werte"][value])
                i = i + 1
                time.sleep(0.1)
            
        # print("Datum: " + item["datum"] + ", Wert: " + item["werte"][value])
        st.info("Anzahl der Statusveränderungen: " + str(i))
        st.success("Ende des Durchlaufs")
        st.balloons()