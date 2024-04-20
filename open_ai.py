import os
import openai

def transcribe_audio(file_path, model="whisper-1"):
    """
    Transcribes audio using OpenAI's Whisper model.

    Args:
    file_path (str): Path to the audio file to be transcribed.
    model (str): Model name to use for transcription. Default is "whisper-1".

    Returns:
    str: The transcribed text.
    """
    # Load API key from environment
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Initialize the OpenAI client
    openai.api_key = api_key
    client = openai.OpenAI()

    # Open the audio file and create a transcription
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=model,
            file=audio_file
        )
    return transcription.text

# Example usage
if __name__ == "__main__":
    audio_path = "output.wav"  # Path to your audio file
    try:
        result = transcribe_audio(audio_path)
        print("Transcribed Text:", result)
    except Exception as e:
        print("Error:", e)