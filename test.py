chat_response = "album,I Just Wanna Dance,artist,Tiffany"
chat_response = chat_response.lower()
chat_response = [item.strip() for item in chat_response.split(',')[1:]]

#artist = chat_response.split(',')[1]
#song = chat_response.split(',')[3]
artist = chat_response[2]
song = chat_response[0]
print(artist, song)