
import os
from openai import OpenAI
def generate_remark(glucose,hb,chol):
    key=os.getenv("OPENAI_API_KEY")
    if not key:
        return "OpenAI key not configured"
    client=OpenAI(api_key=key)
    resp=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":f"Assess patient: glucose={glucose}, haemoglobin={hb}, cholesterol={chol}. Give short health remark."}]
    )
    return resp.choices[0].message.content
