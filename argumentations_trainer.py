import streamlit as st

def main():
    # Titel der App
    st.title("Argumentations-Trainer: Klimawandel")

    # Auswahlmenü für den Modus
    mode = st.sidebar.radio("Wähle einen Modus", ["Vertriebsgespräch", "Politische Diskussion", "Fakten vs. Mythen"])

    if mode == "Vertriebsgespräch":
        vertriebsgespräch()
    elif mode == "Politische Diskussion":
        politische_diskussion()
    elif mode == "Fakten vs. Mythen":
        fakten_vs_mythen()

# Funktion für das Vertriebsgespräch-Quiz
def vertriebsgespräch():
    st.subheader("Szenario: Wirtschaftlichkeit von PV-Anlagen")
    st.write("Ein Geschäftskunde äußert Zweifel an der Wirtschaftlichkeit von PV-Anlagen.")
    st.write("Kunde: 'Solar lohnt sich doch gar nicht mehr, die Einspeisevergütung ist viel zu niedrig!'")

    antwort = st.radio("Welche Antwort ist am besten?", [
        "Das stimmt, aber Sie sparen Netzstromkosten.",
        "Nicht ganz. Die Anlagenpreise sind gefallen, die Amortisation ist kürzer.",
        "Das ist ein Missverständnis. Der Eigenverbrauch macht die Anlage rentabel."
    ])

    if st.button("Antwort bewerten"):
        if antwort == "Das ist ein Missverständnis. Der Eigenverbrauch macht die Anlage rentabel.":
            st.success("Richtig! Der Eigenverbrauch ist der wichtigste Faktor für die Rentabilität.")
        else:
            st.error("Nicht optimal. Der Eigenverbrauch ist entscheidend für die Wirtschaftlichkeit.")

# Funktion für politische Diskussionen
def politische_diskussion():
    st.subheader("Szenario: Einfluss Deutschlands auf das Klima")
    st.write("Diskussionsteilnehmer: 'Deutschland allein kann das Klima nicht retten, China verursacht viel mehr CO₂!'")

    antwort = st.radio("Welche Antwort ist am besten?", [
        "Deutschland ist ein Vorbild und treibt Innovationen voran.",
        "China investiert bereits massiv in erneuerbare Energien, wir haben auch Verantwortung.",
        "Deutschland hat nur 2 % der Emissionen, Klimaschutz hier bringt nichts."
    ])

    if st.button("Antwort bewerten"):
        if antwort == "China investiert bereits massiv in erneuerbare Energien, wir haben auch Verantwortung.":
            st.success("Sehr gut! Dies zeigt, dass China bereits Maßnahmen ergreift und Klimaschutz eine globale Verantwortung ist.")
        else:
            st.error("Nicht optimal. Es ist wichtig, Chinas Maßnahmen und Deutschlands Verantwortung zu betonen.")

# Funktion für Fakten vs. Mythen
def fakten_vs_mythen():
    st.subheader("Fakt oder Mythos?")
    frage = "Der Klimawandel ist hauptsächlich durch natürliche Ursachen bedingt."
    antwort = st.radio(f"Frage: {frage}", ["Fakt", "Mythos"])

    if st.button("Antwort überprüfen"):
        if antwort == "Mythos":
            st.success("Richtig! Der Klimawandel wird hauptsächlich durch menschliche Aktivitäten verursacht.")
        else:
            st.error("Falsch! Wissenschaftliche Studien zeigen klar, dass der Mensch die Hauptursache ist.")

if __name__ == "__main__":
    main()
