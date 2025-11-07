from flask import Flask, request, jsonify
from random import choice

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if "hola" in user_message:
        response = choice(["Hola! 😊", "¡Hey! ¿Cómo estás?"])
    elif "triste" in user_message:
        response = "Lamento que te sientas así, todo mejora con el tiempo 💛"
    else:
        response = "No estoy seguro de qué decir... pero estoy aquí 🦆"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
