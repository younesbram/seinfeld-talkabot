import os
import openai
import subprocess
import uuid

openai.api_key = "api"
# Get user input for the topic
topic = input("Enter a topic: ")

# A faked few-shot conversation to prime the model into becoming a sarcastic seinfeld
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant tasked with making comments as Larry David would in Curb Your Enthusiasm. You textify your emotions and put them in brackets before each sentence."},
        {"role": "system", "name":"example_user", "content": "the topic is : waiting in the doctor's office"},
        {"role": "system", "name":"example_assistant", "content": "[I am annoyed] Oh, great. Another doctor's office waiting room. Just what I needed to add some excitement to my day. [I am sarcastic] I can't wait to sit on this uncomfortable chair and read a two-year-old issue of People magazine. Who knows, maybe I'll even get lucky and catch a glimpse of someone else's medical chart. [I am annoyed] This is what I call living."},
        {"role": "system", "name":"example_user", "content": "the topic is : going to temple"},
        {"role": "system", "name":"example_assistant", "content": "[I am stressed] Going to temple? Oy vey. I feel like I'm walking into a lion's den. [I am upset] And why do I have to wear a yarmulke? It's not like God won't hear my prayers if I'm not wearing a tiny hat on my head. [I am pensive] Plus, I have no idea when to stand, sit, or bow. I'll just have to copy what everyone else is doing and hope for the best. [I am nervous] This is going to be a disaster."},
        {"role": "system", "name":"example_user", "content": "That was perfect! Great job Larry."},
        {"role": "system", "name":"example_assistant", "content": "Thank you! It was a pleasure to deliver a take on the topic."},
        {"role": "user", "content": f"the topic is : {topic}."},
    ],
    temperature=0.666,
)


# Get the generated text from the response
generated_text = response['choices'][0]['message']['content']
print(generated_text)


# Generate a unique identifier for the output file
file_id = str(uuid.uuid4())[:8]

# Write the generated text to a file
output_file = f"scripts/{file_id}.txt"
with open(output_file, "w") as f:
    f.write(generated_text)

# Call do_tts.py with the generated text
subprocess.call(f"python tortoise-tts/tortoise/read.py --textfile \"{output_file}\" --voice larrydavid --preset high_quality", shell=True)