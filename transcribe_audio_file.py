import assemblyai as aai
import os

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# You can use a local filepath:
audio_file = "./interview.mp3"

# Or use a publicly-accessible URL:
# audio_file = (
#     "https://assembly.ai/wildfires.mp3"
# )

config = aai.TranscriptionConfig(
  speaker_labels=True, # Identify different speakers
  speakers_expected=2 # This is ignored for audio files with a duration less than 2 minutes.
)

transcript = aai.Transcriber().transcribe(audio_file, config)

with open ("transcript.txt", "w") as f:
  for utterance in transcript.utterances:
    f.write(f"Speaker {utterance.speaker}: {utterance.text}\n")