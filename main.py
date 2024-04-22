import tkinter as tk
from gui import RecorderApp

def main():
    root = tk.Tk()
    app = RecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


'''
functions should add
1. stop the music when click the recording button

Issues:
1. API return wrong output when ask complicated song. ex: latest album by specific artist
2. simplified chinese vs traditional chinese, some songs are in tradioonal chinese and they are cannot be searched by using simplified chinese
Also some of the chinese artist used english name in spotify

'''