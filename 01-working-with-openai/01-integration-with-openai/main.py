client = OpenAI(api_key="")

response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages=[{"role": "user", "content": "Write a polite reply accepting an AI Engineer job offer."}]
)

print(response.choices[0].message.content)