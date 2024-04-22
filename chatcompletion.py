import openai
import os

def get_chat_completion(user_prompt):
    """
    Sends a chat completion request to OpenAI's GPT-4 using a specified user prompt and predefined conversation history.
    
    Args:
    user_prompt (str): The user's input prompt for the chat.

    Returns:
    The response from the OpenAI API or an error message if an API call fails.
    """
    # Load API key from environment
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    
    # Initialize the OpenAI client with the API key
    openai.api_key = api_key
    client = openai.OpenAI()

    # Define the full set of messages sent to the GPT-4 model including prior conversation context
    messages = [
        {"role": "system", "content": "You are a helpful assistant to help me give key words for getting input for Spotify API."},
        {"role": "user", "content": "play the latest album by Taylor Swift"},
        {"role": "assistant", "content": "album,The Tortured Poets Department"},
        {"role": "user", "content": "Play the latest album by 21 savage"},
        {"role": "assistant", "content": "album,American Dream"},
        {"role": "user", "content": "播放SHE的五月天"},
        {"role": "assistant", "content": "artist,SHE,song,五月天"},
        {"role": "user", "content": "播放五月天的温柔"},
        {"role": "assistant", "content": "artist,五月天,song,温柔"},
        {"role": "user", "content": "play love story"},
        {"role": "assistant", "content": "song,loves tory"},
        {"role": "user", "content": "play some pop music"},
        {"role": "assistant", "content": "genre,pop"},




        {"role": "user", "content": "stop the music"},
        {"role": "assistant", "content": "pause"},
        {"role": "user", "content": "skip the song"},
        {"role": "assistant", "content": "skip"},
        {"role": "user", "content": "pause the music"},
        {"role": "assistant", "content": "pause"},


        {"role": "user", "content": user_prompt},  # the current user prompt to continue the conversation
        {"role": "assistant", "content": ""}  # placeholder for the assistant's next response
    ]

    # Try to create a chat completion and handle potential exceptions
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        # Access the first choice from the response
        first_choice = response.choices[0]
        # Access the content message from the first choice
        content_message = first_choice.message.content
        return content_message
    except Exception as e:
        print(f"An error occurred while attempting to create a chat completion: {e}")
        return None
    

print(get_chat_completion("播放周杰伦的电影里的歌曲"))

