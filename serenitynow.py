import os
import openai
import subprocess
import uuid

openai.api_key = YOUR_OPENAI_KEY_API
# Get user input for the topic
topic = input("Enter a topic: ")

# Generate text using OpenAI's GPT-3 API
prompt = f"Generate a topic about {topic} described by a sarcastic Jerry Seinfeld and give the text."
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.6,
)

# Get the generated text from the response
generated_text = response.choices[0].text.strip()
print(generated_text)


# Generate a unique identifier for the output file
file_id = str(uuid.uuid4())[:8]

# Write the generated text to a file
output_file = f"scripts/{file_id}.txt"
with open(output_file, "w") as f:
    f.write(generated_text)

# Call do_tts.py with the generated text
subprocess.call(f"python tortoise-tts/tortoise/read.py --textfile \"{output_file}\" --voice seinfeld --preset high_quality", shell=True)