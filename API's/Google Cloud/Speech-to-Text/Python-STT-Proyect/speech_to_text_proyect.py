# Imports the Google Cloud client library
import speech as speech
from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient.from_service_account_file("key.json")

file_name = "myfile.mp3"

with open(file_name, "rb") as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)

config = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=False,
    language_code='es-PE',
    speech_contexts=speech.SpeechContexts(phrases=("do", "re", "mi", "fa", "sol", "la", "si"), boost=10)
)

response = client.recognize(
    config=config,
    audio=audio_file
)

print(response)
