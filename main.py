from flask import Flask, render_template, request
from google.genai import Client

client = Client(api_key="AIzaSyCLZKEwkBAgDc6XJ2t66xYqa1pQsaadYOE")
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])

def callIndex():
    res = ""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        problem = request.form.get("problem", "").strip()
        severity = request.form.get("severity", "").strip()

        # Prompt zusammensetzen (wie bei dir)
        content = f"""
        IT-Support-Anfrage:
        Titel: {title if title else "Kein Titel angegeben"}
        Problem: {problem}
        Dringlichkeit: {severity}

        Bitte liefere konkrete, priorisierte Lösungsschritte.
        Und Bitte liefere nur antworten die mit Problemen zu tun haben,
        sollte der User andere Anfragen stellen die nicht mit dem Kontext zu tun haben, 
        dann antworte ihn nicht
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[content]
        )

        res = response.text
        print(res)

        #hier kommt das Bilderverständnis API

    return render_template("index.html", res=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)