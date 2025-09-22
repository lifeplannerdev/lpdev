import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import google.generativeai as genai

GOOGLE_API_KEY = config("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load knowledge base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "context.txt"), "r", encoding="utf-8") as f:
    BASE_CONTEXT = f.read()

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            if not user_message:
                return JsonResponse({"reply": "Please enter a message."})

            # Gemini model
            model = genai.GenerativeModel("models/gemini-2.5-pro")

            # Correct format: role + parts -> list of dicts with 'text'
            response = model.generate_content([
                {
                    "role": "user",
                    "parts": [
                        {"text": f"{BASE_CONTEXT}\n\n{user_message}"}
                    ]
                }
            ])

            bot_reply = response.text if response.text else "Sorry, I couldn’t understand that."
            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"reply": f"⚠️ Error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
