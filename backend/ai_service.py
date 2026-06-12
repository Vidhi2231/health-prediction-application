import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
try:
    from openai import OpenAI
except:
    OpenAI = None


def calculate_risk(glucose, haemoglobin, cholesterol):

    risks = []

    if glucose > 140:
        risks.append(
            "High glucose levels may indicate diabetes risk."
        )

    if cholesterol > 240:
        risks.append(
            "High cholesterol may increase cardiovascular risk."
        )

    if haemoglobin < 12:
        risks.append(
            "Low haemoglobin may indicate anemia."
        )

    if not risks:
        return "All values are within normal range."

    return " ".join(risks)


def generate_ai_remark(
    glucose,
    haemoglobin,
    cholesterol
):

    fallback = calculate_risk(
        glucose,
        haemoglobin,
        cholesterol
    )

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or OpenAI is None:
        return fallback

    try:

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Analyze these blood test results.

                    Glucose: {glucose}
                    Haemoglobin: {haemoglobin}
                    Cholesterol: {cholesterol}

                    Provide a short health assessment.
                    """
                }
            ],
            max_tokens=100
        )

        return response.choices[0].message.content

    except Exception:
        return fallback