import time
import elevenlabs
from elevenlabs.api.error import APIError

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'c08cf1fb7afa630c326abae524016b5f'

def generate_and_play():
    try:
        # Generate audio
        audio = elevenlabs.generate(
            text="Hi, How are you . i hope you like this video . if you got any question comment? dont forget to subscribe to my youtube channel . take care ",
            voice="Dave",
            api_key=API_KEY
        )

        # Play the audio
        elevenlabs.play(audio)

        # Save the audio to a file
        with open("output_audio.wav", "wb") as audio_file:
            audio_file.write(audio)

        print("Audio saved successfully.")
    except APIError as e:
        print(f"API Error: {e}")
        if "User not found, it is likely still being created" in str(e):
            print("Waiting for user creation to complete. Retrying in 1 minute...")
            time.sleep(60)
            generate_and_play()

if __name__ == "__main__":
    generate_and_play()
