import time
import elevenlabs
from elevenlabs.api.error import APIError

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'c08cf1fb7afa630c326abae524016b5f'

def generate_and_play():
    try:
        # Generate audio with the specified settings
        audio = elevenlabs.generate(
            text="اگر یہ کہہ دو بغیر میرے نہیں گزارہ تو میں تمہارا، یا اس پہ مبنی کوئی تأثر کوئی اشارا تو میں تمہارا، غرور پرور انا کا مالک کچھ اس طرح کے ہیں نام میرے، مگر قسم سے جو تم نے اک نام بھی پکارا تو میں تمہارا، تم اپنی شرطوں پہ کھیل کھیلو میں جیسے چاہے لگاؤں بازی، اگر میں جیتا تو تم ہو میرے اگر میں ہارا تو میں تمہارا، تمہارا عاشق تمہارا مخلص تمہارا ساتھی تمہارا اپنا، رہا نہ ان میں سے کوئی دنیا میں جب تمہارا تو میں تمہارا، تمہارا ہونے کے فیصلے کو میں اپنی قسمت پہ چھوڑتا ہوں، اگر مقدر کا کوئی ٹوٹا کبھی ستارا تو میں تمہارا، یہ کس پہ تعویذ کر رہے ہو یہ کس کو پانے کے ہیں وظیفے، تمام چھوڑو بس ایک کر لو جو استخارہ تو میں تمہارا",
            voice=elevenlabs.Voice(
                voice_id='EXAVITQu4vr4xnSDxMaL',
                settings=elevenlabs.VoiceSettings(stability=0.50, similarity_boost=0.4, style=0.0, use_speaker_boost=True)
            ),
            model="eleven_multilingual_v2",
            api_key=API_KEY
        )

        # Play the audio
        elevenlabs.play(audio)

        # Save the audio to a file (optional)
        with open("output_audio.wav", "wb") as audio_file:
            audio_file.write(audio)

        print("Audio saved and played successfully.")
    except APIError as e:
        print(f"API Error: {e}")
        if "User not found, it is likely still being created" in str(e):
            print("Waiting for user creation to complete. Retrying in 1 minute...")
            time.sleep(60)
            generate_and_play()

if __name__ == "__main__":
    generate_and_play()
