from pytube import Playlist
import os

print("Welcome to application\ntype 'q' to exit\n")

while True:
    name = input("Filename: ")
    if name == 'q':
        print("Bye!\n")
        break

    url = input("Url: ")
    if url.startswith('https://www.youtube.com/playlist?list=PL'):
        plist = Playlist(url)
        
        try:
            f = open(f"{name}.txt", "x")    
            
            for i in plist:
                f.write(f'{i}\n')

            print(f'\nFILE CREATED IN: "{os.getcwd()}"\n')

        except(FileExistsError):
            print(f'\n"{name}.txt" HAS ALREADY BEEN CREATED!\n')

    else:
        print('\nURL IS INVALID!\n')