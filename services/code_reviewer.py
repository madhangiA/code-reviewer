from dotenv import load_dotenv
import google.generativeai as genai
from prompts.review_prompt import get_review_prompt
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def review_code(code, language):

    prompt = get_review_prompt(
        code,
        language
    )

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as exc:

        raise RuntimeError(
            f"Gemini request failed: {exc}"
        ) from exc