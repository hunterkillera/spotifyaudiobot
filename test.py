chat_response = "artist, Taylor Swift, song, Lover"
chat_response = [item.strip() for item in chat_response.split(',')[1:]]

#artist = chat_response.split(',')[1]
#song = chat_response.split(',')[3]
artist = chat_response[0]
song = chat_response[1]
print(chat_response,artist, song)