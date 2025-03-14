import streamlit as st
import random

# Definition der Fragen für jedes Modul
fragen = {
    "Vertriebsgespräch": [
        ("Ein Kunde sagt: 'Solar lohnt sich nicht mehr, die Einspeisevergütung ist zu niedrig!'", [
            "Das stimmt, aber Sie sparen Netzstromkosten.",
            "Nicht ganz. Die Anlagenpreise sind gefallen, die Amortisation ist kürzer.",
            "Das ist ein Missverständnis. Der Eigenverbrauch macht die Anlage rentabel."
        ], 2),
        ("Ein Kunde fragt: 'Warum sollte ich jetzt eine PV-Anlage kaufen?'", [
            "Weil die Technologie immer besser wird.",
            "Weil die Strompreise steigen und Eigenverbrauch günstiger wird.",
            "Weil die Förderung bald ausläuft."
        ], 1)
    ],
    "Politische Diskussion": [
        ("Diskussionsteilnehmer: 'Deutschland allein kann das Klima nicht retten, China verursacht viel mehr CO₂!'", [
            "Deutschland ist ein Vorbild und treibt Innovationen voran.",
            "China investiert bereits massiv in erneuerbare Energien, wir haben auch Verantwortung.",
            "Deutschland hat nur 2 % der Emissionen, Klimaschutz hier bringt nichts."
        ], 1),
        ("Jemand sagt: 'Klimawandel gab es doch schon immer!'", [
            "Das stimmt, aber die Geschwindigkeit heute ist unnatürlich hoch.",
            "Das ist falsch, früher gab es keine Klimaveränderungen.",
            "Das ist egal, denn wir können nichts tun."
        ], 0)
    ],
    "Fakten vs. Mythen": [
        ("Der Klimawandel ist hauptsächlich durch natürliche Ursachen bedingt.", [
            "Fakt", "Mythos"
        ], 1),
        ("Windräder töten massenhaft Vögel.", [
            "Fakt", "Mythos"
        ], 1)
    ]
}

def quiz(modus):
    st.subheader(f"Quiz: {modus}")
    alle_fragen = fragen[modus]
    zufallsfragen = random.sample(alle_fragen, min(10, len(alle_fragen)))
    score = 0
    total_questions = len(zufallsfragen)

    for i, (frage, antworten, richtige_index) in enumerate(zufallsfragen):
        st.write(f"**Frage {i + 1}/{total_questions}:** {frage}")
        antwort = st.multiselect("Wähle die richtige(n) Antwort(en):", antworten)
        if st.button(f"Antwort {i + 1} überprüfen", key=f"button_{i}"):
            if richtige_index in [antworten.index(a) for a in antwort]:
                st.success("Richtig!")
                score += 1
            else:
                st.error("Leider falsch.")
    
    if st.button("Quiz auswerten"):
        st.write(f"Dein Score: {score}/{total_questions}")
        st.success("Gut gemacht!" if score >= total_questions / 2 else "Du kannst noch etwas lernen!")

def main():
    st.title("Argumentations-Trainer: Klimawandel")
    mode = st.sidebar.radio("Wähle einen Modus", ["Vertriebsgespräch", "Politische Diskussion", "Fakten vs. Mythen"])
    quiz(mode)

if __name__ == "__main__":
    main()
