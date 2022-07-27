__author__ = "Narin Hama, Dominik Rolof"
__copyright__ = "Copyright 2022, Project Innovation Technology II"
__credits__ = "Group 8"
__version__ = "1.2"
__email__ = "dominik.rolof@fau.de"
__status__ = "Production"

from urllib.request import urlopen
import streamlit as st
import json
import time

# INIT ####################################################################################################################################

# page config
st.set_page_config(
    page_title="Ablauf Simulationsfabrik",
    page_icon="📈",
    layout="wide"
)

# use css stylesheet
with open("style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# default page layout
st.title('Fischertechnik Simulationsfabrik & Festo (Historie und Datensammlung): Darstellung sich ändernder Sensorausprägungen und Visualisierung der Wegstrecken')

col1, col2 = st.columns([4,3])
with col1:
    acceleration = st.radio("Bitte gewünschte Beschleunigung wählen:", ("Echtzeit", "10x", "100x"), horizontal=True)
    st.write("\n")
    st.write("\n")
    button = st.button("Status der Maschine abfragen")

with col2:
    col2.write("Störungsanzeige:")
    image_pos = st.empty()
    image_pos.image("ampel_weiss.png", width=225)

# introduce global variables and read json from url
i = 0
k = 0
hVertBuf = 0
hHorBuf = 0
vVertBuf = 0
vDrehBuf = 0
vHorBuf = 0
url = urlopen("https://it2wi1.if-lab.de/rest/ft_ablauf")
data = json.loads(url.read())
keys = data[i]["werte"]

# FUNCTIONS ####################################################################################################################################

# function to print the exact values
def printValues(curr_item, value):
    global i

    datum.write("Datum:\n" + curr_item["datum"])
    schalter.write("Schalter:\n" + value)
    wert.write("Wert:\n" + curr_item["werte"][value])

    # counter for number of changing sensor statuses
    i = i + 1




# function to compare two lines of json output
def showDifference(prev_item, curr_item):
    global image_pos
    global hVertBuf
    global hHorBuf
    global vVertBuf
    global vDrehBuf
    global vHorBuf

# for each different value in json lines show the right image    
    for value in keys:
        if prev_item["werte"][value] != curr_item["werte"][value]:

            # section for changing movement
            if value == "H-vertikal":
                if int(curr_item["werte"][value]) > hVertBuf:
                    image_anlage1.image("arrow_up.png", width=100)
                elif int(curr_item["werte"][value]) < hVertBuf:
                    image_anlage1.image("arrow_down.png", width=100)
                hVertBuf = int(curr_item["werte"][value])
            elif value == "H-horizontal":
                if int(curr_item["werte"][value]) > hHorBuf:
                    image_anlage1.image("arrow_right.png", width=100)
                elif int(curr_item["werte"][value]) < hHorBuf:
                    image_anlage1.image("arrow_left.png", width=100)
                hHorBuf = int(curr_item["werte"][value])
            elif value == "V-vertikal":
                if int(curr_item["werte"][value]) > vVertBuf:
                    image_anlage3.image("arrow_up.png", width=100)
                elif int(curr_item["werte"][value]) < vVertBuf:
                    image_anlage3.image("arrow_down.png", width=100)
                vVertBuf = int(curr_item["werte"][value])
            elif value == "V-drehen":
                if int(curr_item["werte"][value]) > vDrehBuf:
                    image_anlage3.image("arrow_circular_right.png", width=100)
                elif int(curr_item["werte"][value]) < vDrehBuf:
                    image_anlage3.image("arrow_circular_left.png", width=100)
                vDrehBuf = int(curr_item["werte"][value])
            elif value == "V-horizontal":
                if int(curr_item["werte"][value]) > vHorBuf:
                    image_anlage3.image("arrow_right.png", width=100)
                elif int(curr_item["werte"][value]) < vHorBuf:
                    image_anlage3.image("arrow_left.png", width=100)
                vHorBuf = int(curr_item["werte"][value])

            # section for changing sensors
            elif value == "B-Referenzschalter Drehkranz (Pos. Sauger)":
                image_anlage2.image("B-Referenzschalter Drehkranz (Pos. Sauger).png", width=225)
                printValues(curr_item, value)
            elif value == "B-Referenzschalter Drehkranz (Pos. Foerderband)":
                image_anlage2.image("B-Referenzschalter Drehkranz (Pos. Foerderband).png", width=225)
                printValues(curr_item, value)
            elif value == "B-Lichtschranke Ende Foerderband":
                image_anlage2.image("B-Lichtschranke Ende Foerderband.png", width=225)
                printValues(curr_item, value)
            elif value == "B-Referenzschalter Sauger (Pos. Brennofen)":
                image_anlage2.image("-Referenzschalter Sauger (Pos. Brennofen).png", width=225)
                printValues(curr_item, value)
            elif value == "B-Lichtschranke Brennofen":
                image_anlage2.image("B-Lichtschranke Brennofen.png", width=225)
                printValues(curr_item, value)
            elif value == "S-Lichtschranke Eingang":
                image_anlage2.image("S-Lichtschranke Eingang.png", width=225)
                printValues(curr_item, value)
            elif value == "S-Lichtschranke nach Farbsensor":
                image_anlage2.image("S-Lichtschranke nach Farbsensor.png", width=225)
                printValues(curr_item, value)
            elif value == "S-Lichtschranke weiss":
                image_anlage2.image("S-Lichtschranke weiss.png", width=225)
                printValues(curr_item, value)
            elif value == "S-Lichtschranke rot":
                image_anlage2.image("S-Lichtschranke rot.png", width=225)
                printValues(curr_item, value)
            elif value == "S-Lichtschranke blau":
                image_anlage2.image("S-Lichtschranke blau.png", width=225)
                printValues(curr_item, value)
            elif value == "Lichtschranke innen":
                image_anlage2.image("Lichtschranke innen.png", width=225)
                printValues(curr_item, value)
            elif value == "Referenztaster vertikal":
                image_anlage2.image("Referenztaster vertikal.png", width=225)
                printValues(curr_item, value)
            elif value == "Referenztaster Ausleger vorne":
                image_anlage2.image("Referenztaster Ausleger vorne.png", width=225)
                printValues(curr_item, value)
            elif value == "V-Referenzschalter vertikal":
                image_anlage4.image("V-Referenzschalter vertikal.png", width=225)
                printValues(curr_item, value)
            elif value == "V-Referenzschalter horizontal":
                image_anlage4.image("V-Referenzschalter horizontal.png", width=225)
                printValues(curr_item, value)
            elif value == "V-Referenzschalter drehen":
                image_anlage4.image("V-Referenzschalter drehen.png", width=225)
                printValues(curr_item, value)
            elif value == "B-Motor Foerderband vorwaerts":
                image_anlage2.image("B-Motor Foerderband vorwaerts.png", width=225)
                printValues(curr_item, value)
            elif value == "B-Motor Saege":
                image_anlage2.image("B-Motor Saege.png", width=225)
                printValues(curr_item, value)
            elif value == "B-Motor Sauger zum Ofen":
                image_anlage2.image("B-Motor Sauger zum Ofen.png", width=225)
                printValues(curr_item, value)
            elif value == "B-Motor Sauger zum Drehkranz":
                image_anlage2.image("B-Motor Sauger zum Drehkranz.png", width=225)
                printValues(curr_item, value)

            # section for changing machine status
            if value == "Ampel gruen" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_gruen.png", width=225)
            elif value == "Ampel weiss" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_weiss.png", width=225)
            elif value == "Ampel rot" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_rot.png", width=225)
            elif value == "Ampel orange" and curr_item["werte"][value].strip() == "true":
                image_pos.image("ampel_orange.png", width=225)


# MAIN ####################################################################################################################################

# start to work if user pushes the button
if button:
    # index for json lines
    j = 1

    # default layout
    with st.spinner("Maschine arbeitet"):
        col1, col2, col3, col4 = st.columns([2,3,2,3])
        with col1:
            col1.write("Bewegung Hochregal:")
            image_anlage1 = st.empty()
            image_anlage1.write("Keine Bewegung")
        with col2:
            image_anlage2 = st.empty()
            image_anlage2.image("automatisiertes_hochregallager_skaliert_1.png", width=225)
        with col3:
            col3.write("Bewegung Sauggreifer:")
            image_anlage3 = st.empty()
            image_anlage3.write("Keine Bewegung")
        with col4:
            image_anlage4 = st.empty()
            image_anlage4.image("vakuum_skaliert_1.png", width=225)
        
        col5, col6, col7 = st.columns(3)
        with col5:
            datum = st.empty()
        with col6:
            schalter = st.empty()
        with col7:
            wert = st.empty()

        # acceleration setup and walk through json lines
        for item in data:
            try:
                prev_item = data[j-1]
                curr_item = data[j]
                j = j + 1

                if acceleration == "10x":
                    time.sleep(0.1)
                elif acceleration == "100x":
                    time.sleep(0.01)
                else:
                    time.sleep(1)

                image_anlage1.write("Keine Bewegung")
                image_anlage3.write("Keine Bewegung")
                if prev_item["werte"] != curr_item["werte"]:
                    showDifference(prev_item, curr_item)

            except:
                break

        # machine finished and application also ;)
        st.success("Ende des Durchlaufs. Anzahl Statusveränderungen: " + str(i))

# END ####################################################################################################################################        