import streamlit as st
import random
import time

st.set_page_config(page_title="Emoji-Ratespiel", page_icon="💡")

# --- Spiel-Daten ---
THEMEN = {
    "Filme": [
        {"emoji": "🧙‍♂️⚡🏰", "antwort": "Harry Potter"},
        {"emoji": "🦁👑", "antwort": "König der Löwen"},
        {"emoji": "🧊🚢💔", "antwort": "Titanic"},
        {"emoji": "🦸‍♂️🕷️", "antwort": "Spider-Man"},
        {"emoji": "🐠🔍", "antwort": "Findet Nemo"},
    ],
    "Bücher": [
        {"emoji": "🐍⚡📖", "antwort": "Harry Potter"},
        {"emoji": "👧🌈🦁", "antwort": "Der Zauberer von Oz"},
        {"emoji": "🐳⚓", "antwort": "Moby Dick"},
        {"emoji": "👻🏠", "antwort": "Spukhaus"},
        {"emoji": "🧙‍♂️🪄", "antwort": "Der Herr der Ringe"},
    ],
    "Gegenstände": [
        {"emoji": "📱", "antwort": "Handy"},
        {"emoji": "💡", "antwort": "Lampe"},
        {"emoji": "🪑", "antwort": "Stuhl"},
        {"emoji": "⌚", "antwort": "Uhr"},
        {"emoji": "🎒", "antwort": "Rucksack"},
    ],
    "Songs": [
        {"emoji": "🕺🪩", "antwort": "Stayin' Alive"},
        {"emoji": "👑🕺", "antwort": "King of Pop"},
        {"emoji": "🎅🎶", "antwort": "Jingle Bells"},
        {"emoji": "🔥🎤", "antwort": "Firework"},
        {"emoji": "💔🎵", "antwort": "Someone Like You"},
    ],
    "Tiere": [
        {"emoji": "🦁", "antwort": "Löwe"},
        {"emoji": "🐘", "antwort": "Elefant"},
        {"emoji": "🐍", "antwort": "Schlange"},
        {"emoji": "🐧", "antwort": "Pinguin"},
        {"emoji": "🐢", "antwort": "Schildkröte"},
    ],
    "Länder": [
        {"emoji": "🗼🍣", "antwort": "Japan"},
        {"emoji": "🦘🇦🇺", "antwort": "Australien"},
        {"emoji": "🍕🏛️", "antwort": "Italien"},
        {"emoji": "🗽🍔", "antwort": "USA"},
        {"emoji": "🥨🍺", "antwort": "Deutschland"},
    ],
}

# --- Session Setup ---
if "thema" not in st.session_state:
    st.session_state.thema = None
if "punkte" not in st.session_state:
    st.session_state.punkte = 0
if "runde" not in st.session_state:
    st.session_state.runde = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "reset_key" not in st.session_state:
    st.session_state.reset_key = 0

# --- Titel ---
st.title("🎯 Emoji master – Das Emoji-Ratespiel")
st.caption("Errate, was die Emojis bedeuten, und sammle Punkte! 💡")

# --- Themenauswahl ---
if st.session_state.thema is None:
    st.subheader("Wähle ein Thema:")
    thema = st.selectbox("Kategorie:", list(THEMEN.keys()))
    if st.button("Start! 🚀"):
        st.session_state.thema = thema
        st.session_state.runde = random.choice(THEMEN[thema])
        st.session_state.punkte = 0
        st.rerun()

# --- Spiel ---
else:
    st.subheader(f"Thema: {st.session_state.thema}")
    st.write("Errate, was diese Emojis darstellen:")
    st.markdown(f"### {st.session_state.runde['emoji']}")

    # Das Textfeld bekommt bei jeder Runde einen neuen Key → kein Fehler!
    antwort = st.text_input(
        "Deine Antwort:",
        key=f"user_input_{st.session_state.reset_key}"
    )

    if st.button("Prüfen ✅"):
        richtige_antwort = st.session_state.runde["antwort"].lower().strip()
        user_antwort = antwort.lower().strip()

        if user_antwort == richtige_antwort:
            st.balloons()
            time.sleep(2)
            st.session_state.punkte += 1
            st.session_state.feedback = f"✅ Richtig! Es war **{st.session_state.runde['antwort']}** 🎉"
        else:
            st.session_state.feedback = f"❌ Falsch! Richtige Antwort: **{st.session_state.runde['antwort']}**"

        # Neue Runde + neuer Key fürs Eingabefeld (reset)
        st.session_state.runde = random.choice(THEMEN[st.session_state.thema])
        st.session_state.reset_key = random.randint(0, 1000000)
        st.rerun()

    # --- Feedback & Punkteanzeige ---
    st.markdown(st.session_state.feedback)
    st.markdown(f"**Punkte:** {st.session_state.punkte}")

    # --- Neustart ---
    if st.button("🔁 Neues Thema wählen"):
        for key in ["thema", "punkte", "runde", "feedback", "reset_key"]:
            st.session_state[key] = None
        st.rerun()
