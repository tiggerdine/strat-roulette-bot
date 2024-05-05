from stratroulette.config import TTS, ELEVEN_API_KEY

FILENAME = ".speech"

if TTS == "pyttsx3":
    import pyttsx3

    engine = pyttsx3.init()

    def _generate(text):
        engine.save_to_file(text, FILENAME)
        engine.runAndWait()

elif TTS == "elevenlabs":
    from elevenlabs.client import ElevenLabs
    from elevenlabs import save

    client = ElevenLabs(api_key=ELEVEN_API_KEY)

    def _generate(text):
        audio = client.generate(text=text)
        save(audio, FILENAME)

else:
    raise RuntimeError(f"{TTS} not supported")


def generate(text):
    _generate(text)
    return FILENAME
