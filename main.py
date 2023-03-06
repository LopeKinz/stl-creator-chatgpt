import openai
from pystl import Solid, Vertex

# 1. Verbinde dich mit der OpenAI API
openai.api_key = "Dein API-Schlüssel hier"
model_engine = "davinci"  # oder ein anderes Modell, je nach Bedarf

# 2. Definiere eine Funktion, die ChatGPT nutzt, um den Benutzer zu fragen, was er/sie drucken möchte.
def ask_user():
    prompt = "Was möchtest du drucken? "
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# 3. Definiere eine Funktion, die aus der Benutzereingabe eine STP-Datei erstellt.
def create_stp_file(user_input):
    solid = Solid()  # Erstelle ein neues STP-Objekt

    # Füge einige Beispielgeometrien hinzu
    # Hier kannst du deiner Kreativität freien Lauf lassen und die Geometrien basierend auf der Benutzereingabe erstellen.
    solid.add_face([Vertex(0,0,0), Vertex(1,0,0), Vertex(1,1,0)])
    solid.add_face([Vertex(0,0,0), Vertex(1,1,0), Vertex(0,1,0)])
    solid.add_face([Vertex(0,0,0), Vertex(0,1,0), Vertex(0,1,1)])
    solid.add_face([Vertex(0,0,0), Vertex(0,1,1), Vertex(0,0,1)])

    # Speichere das STP-Objekt in einer Datei
    solid.write_stp("output.stp")

# 4. Hauptprogramm
def main():
    user_input = ask_user()
    create_stp_file(user_input)

# 5. Führe das Hauptprogramm aus
if __name__ == "__main__":
    main()
