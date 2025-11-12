import streamlit as st
import random

# --- Daten ---
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
        {"emoji": "🐷👦", "antwort": "Schweinsgalopp"},
        {"emoji": "👧🌈🦁", "antwort": "Der Zauberer von Oz"},
        {"emoji": "🐳⚓", "antwort": "Moby Dick"},
        {"emoji": "👻🏠", "antwort": "Spukhaus"},
    ],
    "Gegenstände": [
        {"emoji": "📱", "antwort": "Handy"},
        {"emoji": "💡", "antwort": "Lampe"},
        {"emoji": "🪑", "antwort": "Stuhl"},
        {"emoji": "⌚", "antwort": "Uhr"},
        {"emoji": "🎒", "antwort": "Rucksack"},
    ],
}

# --- Initialisierung ---
if "thema" not in st.session_state:
    st.session_state.thema = None
if "punkte" not in st.session_state:
    st.session_state.punkte = 0
if "runde" not in st.session_state:
    st.session_state.runde = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

st.title("🧩 Emoji-Ratespiel")

# --- Themenauswahl ---
if st.session_state.thema is None:
    st.subheader("Wähle ein Thema:")
    thema = st.selectbox("Kategorie:", list(THEMEN.keys()))
    if st.button("Start!"):
        st.session_state.thema = thema
        st.session_state.runde = random.choice(THEMEN[thema])
        st.rerun()

# --- Spiel ---
else:
    st.subheader(f"Thema: {st.session_state.thema}")
    st.write("Errate, was diese Emojis bedeuten:")
    st.markdown(f"### {st.session_state.runde['emoji']}")

    antwort = st.text_input("Deine Antwort:", key="antwort")

    if st.button("Prüfen"):
        if antwort.strip().lower() == st.session_state.runde["antwort"].lower():
            st.session_state.punkte += 1
            st.session_state.feedback = f"✅ Richtig! Es war **{st.session_state.runde['antwort']}** 🎉"
        else:
            st.session_state.feedback = f"❌ Falsch! Richtige Antwort: **{st.session_state.runde['antwort']}**"

        # Neue Runde aus dem gleichen Thema
        st.session_state.runde = random.choice(THEMEN[st.session_state.thema])
        st.session_state.antwort = ""

    st.markdown(st.session_state.feedback)
    st.markdown(f"**Punkte:** {st.session_state.punkte}")

    # --- Neustart ---
    if st.button("🔁 Neues Thema wählen"):
        for key in ["thema", "punkte", "runde", "feedback"]:
            st.session_state[key] = None
        st.rerun()
