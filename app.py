from openai import OpenAI

client = OpenAI()


response = client.images.generate(
    prompt="For a children's book: Picture of a realistic jug. The picture shouldn't include any animals or people or anthromorphic features.",
    model="dall-e-3",
    size="1024x1024",
    quality="standard",
    n=1, 
)

print(response)
print(f"URL: {response.data[0].url}")
