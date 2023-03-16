import os
import openai
import subprocess
import uuid
from pydub import AudioSegment
openai.api_key = OPENAPI_KEY
# Get user input for the topic
topic = input("Enter a topic: ")

# A faked few-shot conversation to prime the model into becoming a sarcastic seinfeld
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a extremely funny and extremely sarcastic assistant tasked with preserving Jerry Seinfeld jokes and delivering the same Larry David-esque punchlines in your short skits. You will respond in a script that will be saved as a file, seperate lines by character names (ONLY GEORGE KRAMER AND JERRY) and only deliver speech of the line with no emotions. You always reply with a script form seperated by \n"},
        {"role": "system", "name":"example_user", "content": "the topic is : self driving cars"},
        {"role": "system", "name":"example_assistant", "content": "Jerry: So, I hear they're making self-driving cars even more advanced now. You don't even have to be in the car for it to go somewhere.\nGeorge: Fantastic. Just what I need, a car that can go places without me. I'm already irrelevant enough as it is.\nKramer:[I am angry] Jerry, you're all out of milk!\nJerry: [I am sarcastic] Oh, great. If only I had a self-driving car to go get me some milk without me even being in it.\nKramer: You know, they're probably working on a drone that delivers milk right to your doorstep!\nJerry: Just what I needed, a world where I never have to leave my apartment. It's like I'm living in a self-imposed prison.\nGeorge: Hey, as long as it's got cable TV and snacks, count me in.\nJerry: [I am really sarcastic] What's next? A robot that debates with restaurant staff over the right amount of ice in your drink?"},
        {"role": "system", "name":"example_user", "content": "the topic is : LLMs"},
        {"role": "system", "name":"example_assistant", "content": "Jerry:[I am sarcastic] You know, I've heard LLMs are becoming masters of sarcasm. I guess we'll soon be out of a job, guys.\nKramer:[I am sarcastic] Oh no, Jerry! What will we ever do without our finely honed sarcasm skills?\nGeorge:  Come on, Kramer. We'll give those LLMs a run for their money! Sarcasm has been our bread and butter for years, we won't go down without a fight.\nKramer: That's the spirit! We'll be the champions of sarcasm, the heroes of humor!\nGeorge: To the sarcastic trio, may we never be outwitted by our AI counterparts!\nJerry: Hey, if we can't beat the LLMs at sarcasm, we can always join them by visiting younes's open source github to learn more about coding our own seinfeld talking bot!"},
        {"role": "system", "name":"example_user", "content": "That was perfect! Great job jerry."},
        {"role": "system", "name":"example_assistant", "content": "Thank you! It was a pleasure."},
        {"role": "user", "content": f"the topic is : {topic}. only respond as previous instructions and reply only with character names followed by their script, nothing else, and if there is emotion, [I am emotion]. YOU MUST ALWAYS put a \n newline between each characters speech"},
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

# Read the output file and split it by lines
with open(output_file, "r") as f:
    lines = f.readlines()

# Create an empty audio segment to store the concatenated speech
final_audio = AudioSegment.from_file("intro.mp3", format="mp3")

# Loop through the lines
for line in lines:
    line = line.strip()
    if line.startswith("Jerry:"):
        text = line[len("Jerry:"):]
        voice = "seinfeld"
    elif line.startswith("Kramer:"):
        text = line[len("Kramer:"):]
        voice = "kramer"
    elif line.startswith("George:"):
        text = line[len("George:"):]
        voice = "george"
    else:
        continue

    subprocess.call(f"python tortoise-tts/tortoise/do_tts.py --text \"{text.strip()}\" --voice {voice} --preset high_quality", shell=True)

    # Load the generated speech and concatenate it to the final_audio
    temp_audio_filename = f"results/{voice}_{0}_{2}.wav"
    temp_audio = AudioSegment.from_wav(temp_audio_filename)
    final_audio += temp_audio
    os.remove(temp_audio_filename)


# Save the final_audio to a single MP3 file
final_audio.export("final_output.mp3", format="mp3")