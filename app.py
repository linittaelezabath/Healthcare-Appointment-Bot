from flask import Flask, request, jsonify
from flask_cors import CORS
from bot import HealthcareAppointmentBot

app = Flask(__name__)
CORS(app)   # 👈 THIS LINE FIXES IT

bot = HealthcareAppointmentBot()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = bot.process_input(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
