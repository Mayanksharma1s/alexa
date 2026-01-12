from google import genai

def response_chatbot(prompt):
    client = genai.Client(api_key = "AIzaSyCwsZbKSxoI9pqWjSD_OpB2w1jFzottLyU")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents = prompt
    )
    return response.text
