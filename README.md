
## Seinfeld-Talkabot



How to use : 

0. PyTorch & Have a decent GPU
1. Follow installation of dependencies for tortoise and openai on pip (Tip: use conda environment)
2. Attach your openai api key on client side or in env
3. python serenitynow.py => enter any topic you'd like a seinfeld skit/joke on


## Tech Stack

OpenAI===gpt-3.5-turbo
TorToiSe==2.4.2
Conda Environment
Python / Pip
More soon

## To collab
please fork and follow general PR rules. 
 
## Intro:
The Seinfeld-Talkabot is a project that utilizes OpenAI's gpt-3.5-turbo model and the TorToiSe library to generate audio files of Seinfeld characters speaking user-provided text. The goal of the project is to showcase the potential of such apps, which could be used for a variety of purposes, including generating accurate and authentic-sounding audiobooks using prompt engineering and TorToiSe, or translating and dubbing content using the GPT-3 model while maintaining the original voice. By demonstrating the capabilities of these technologies, the Seinfeld-Talkabot aims to inspire further innovation in the field of natural language processing and audio generation.


## Todo:
Create any kind of frontend to interact with backend of selecting a topic (Text input) => turbogpt3.5 generate a script => api call to TorToiSe + pyfastmp3encoder to generate a .wav file with the selected seinfeld character voice. Currently supporting jerry seinfelds voice from his audiobook + wav files from the seinfeld show itself.

## Ethical Promises
This project is just to showcase the potential of such apps. Hopefully in the future we will have a more clear guideline on ethically using applications such as this. I hope I gave enough credit where due. Please let me know of any issues younes@younes.ca

## Thanks to
            https://github.com/neonbjb/ For his pyfastmp3encoder + TorToiSe
            https://github.com/CorentinJ/Real-Time-Voice-Cloning
            Seinfeld, Jerry.
            David, Larry.
            OpenAI

