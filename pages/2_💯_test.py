from urllib.request import urlopen
import streamlit as st
import json
import time

st.set_page_config(
    page_title="Wegstrecken-Visualizer",
    page_icon="👋",
)

with open("style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

col1, col2 = st.columns(2)

with col1:
    st.title('FT-Ablauf-Visualizer')   
    st.subheader('Stellt sich ändernde Sensorausprägungen dar')

with col2:
    image_pos = st.empty()
    image_pos.image("ampel_weiss.png", width=50)

i = 0
k = 0
url = urlopen("https://it2wi1.if-lab.de/rest/ft_ablauf")
data = json.loads(url.read())
keys = data[i]["werte"]
acceleration = st.slider("Bitte gewünschte Beschleunigung wählen:", 0, 100)

def showDifference(prev_item, curr_item):
    global image_pos
    
    for value in keys:
        # print("Datum: " + data[i]["datum"] + ", Schalter: " + value + ", Wert1: " + prev_item[value] +  ", Wert2: " + curr_item[value] + "\n")
        if prev_item["werte"][value] != curr_item["werte"][value]:
            # print("Datum: " + data[i]["datum"] + ", Schalter: " + value + ", Wert: " + curr_item[value] + "\n")
            if value == "B-Referenzschalter Drehkranz (Pos. Sauger)":
                image_anlage1.image("automatisiertes_hochregallager_skaliert_1.png", width=400)
                image_anlage2.image("automatisiertes_hochregallager_skaliert_2.png", width=400)
            else:
                image_anlage1.image("multi_bearbeitungsstation_skaliert_1.png", width=400)
                image_anlage2.image("multi_bearbeitungsstation_skaliert_2.png", width=400)
            datum.write("Datum:\n" + curr_item["datum"])
            schalter.write("Schalter:\n" + value)
            wert.write("Wert:\n" + curr_item["werte"][value])
            
            # st.write("Datum: " + curr_item["datum"] + ", Schalter: " + value + ", Wert: " + curr_item["werte"][value])
            if value == "Ampel gruen" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_gruen.png", width=50)
            elif value == "Ampel weiss" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_weiss.png", width=50)
            elif value == "Ampel rot" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_rot.png", width=50)
            elif value == "Ampel orange" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_orange.png", width=50)

# print(data[0]["werte"].keys())
# value = st.text_input("Bitte den auszulesenden Wert eingeben:")
# value = "H-horizontal"
# print(data[0]["werte"])
if st.button("Status der Maschine abfragen"):
    j = 1
    with st.spinner("Maschine arbeitet"):
        col1, col2 = st.columns(2)
        with col1:
            image_anlage1 = st.empty()
            image_anlage1.image("automatisiertes_hochregallager_skaliert_1.png", width=400)
        with col2:
            image_anlage2 = st.empty()
            image_anlage2.image("automatisiertes_hochregallager_skaliert_2.png", width=400)
        
        col3, col4, col5 = st.columns(3)
        with col3:
            datum = st.empty()
        with col4:
            schalter = st.empty()
        with col5:
            wert = st.empty()
        for item in data:
            try:
                prev_item = data[j-1]
                curr_item = data[j]
                j = j + 1
                time.sleep(1 - (acceleration / 100))
                if prev_item["werte"] != curr_item["werte"]:
                    i = i + 1
                    showDifference(prev_item, curr_item)
                # print("Datum: " + item["datum"] + ", Wert: " + item["werte"][value])
                # st.write("Datum: " + col1 + ", Wert: " + item["werte"][value])
                k =  k + i
            except:
                break

# if value != "":

#     with st.spinner("Maschine arbeitet"):
#         buffer = data[0]["werte"][value]
#         for item in data:
#             if buffer != item["werte"][value]:
#                 # print("Datum: " + item["datum"] + ", Wert: " + item["werte"][value])
#                 buffer = item["werte"][value]
#                 col1, col2 = st.columns(2)
#                 col1.write("Datum: " + item["datum"])
#                 col2.write("Wert: " + item["werte"][value])
#                 # st.write("Datum: " + col1 + ", Wert: " + item["werte"][value])
#                 i = i + 1
#                 time.sleep(0.1)
            
        # print("Datum: " + item["datum"] + ", Wert: " + item["werte"][value])
        st.info("Anzahl der Statusveränderungen: " + str(i))
        st.success("Ende des Durchlaufs")
        st.balloons()