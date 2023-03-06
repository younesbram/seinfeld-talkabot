import os
import openai
import subprocess
import uuid

openai.api_key = YOUR_API_KEY
# Get user input for the topic
topic = input("Enter a topic: ")

# A faked few-shot conversation to prime the model into becoming a sarcastic seinfeld
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant tasked with making Jerry Seinfeld jokes. You textify your emotions and put them in brackets before each sentence."},
        {"role": "system", "name":"example_user", "content": "the topic is : public speaking"},
        {"role": "system", "name":"example_assistant", "content": "[I am sarcastic] I saw this study saying speaking in front of a crowd is considered the number one fear of the average person. I found that amazing. [I am sarcastic and surprised] Number two.. was death. [I am surprised and sarcastic] Death is number two?! [I am sarcastic and angry] This means to the average person at a funeral, you would rather be in the casket, than doing the eulogy."},
        {"role": "system", "name":"example_user", "content": "the topic is : expired milk"},
        {"role": "system", "name":"example_assistant", "content": "[I am sarcastic] Have you ever had milk the day after the expiry date? Scares the hell out of you, doesn't it. [I am scared and sarcastic] It's after the day! I'm taking a really big chance here! [I am sarcastic and excited] Makes you wonder, how are the dates exact? Maybe the cows tip them off when they're milking them."},
        {"role": "system", "name":"example_user", "content": "That was perfect! Great job jerry."},
        {"role": "system", "name":"example_assistant", "content": "Thank you! It was a pleasure to deliver a sarcastic take on the topic."},
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
subprocess.call(f"python tortoise-tts/tortoise/read.py --textfile \"{output_file}\" --voice seinfeld --preset high_quality", shell=True)