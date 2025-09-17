from flask import Flask, render_template, request
from google import genai
from google.genai import Client, types

# Initialisiere Client mit API-Key
client = Client(api_key="AIzaSyCLZKEwkBAgDc6XJ2t66xYqa1pQsaadYOE")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def callIndex():
    res = ""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        problem = request.form.get("problem", "").strip()
        severity = request.form.get("severity", "").strip()

        # Datei laden
        foto_file = request.files.get("foto")
        foto_bytes = None
        mime_type = None
        if foto_file and foto_file.filename != "":
            foto_bytes = foto_file.read()
            mime_type = foto_file.mimetype or "image/png"

        # Prompt
        content_text = f"""
        IT-Support-Anfrage:
        Titel: {title if title else "Kein Titel angegeben"}
        Problem: {problem}
        Dringlichkeit: {severity}

        Bitte liefere konkrete, priorisierte Lösungsschritte.
        Und bitte liefere nur Antworten, die mit IT-Problemen zu tun haben.
        Sollte der Benutzer andere Anfragen stellen, die nicht mit dem Kontext zu tun haben, dann antworte nicht.
        """

        # Parts manuell zusammenbauen
        parts = [types.Part(text=content_text)]
        if foto_bytes:
            parts.append(types.Part(
                inline_data=types.Blob(mime_type=mime_type, data=foto_bytes)
            ))

        # Content definieren
        contents = [types.Content(role="user", parts=parts)]

        # API-Call
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents
        )

        res = response.text or "Keine Antwort erhalten."

    return render_template("index.html", res=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)