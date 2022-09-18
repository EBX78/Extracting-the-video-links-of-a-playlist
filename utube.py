from pytube import Playlist
import os

print("Welcome to application\ntype 'q' to exit\n")

while True:

    name = input("Name: ")
    if name == 'q':
        print("\nBye.\n")
        break

    url = input("Url: ")
    if url == 'q':
        print("\nBye.\n")
        break

    elif url.startswith('https://www.youtube.com/playlist?list=PL'):
        plist = Playlist(url)

        try:
            with open(f"{name}.txt", "x") as f:
                [f.write(f'{i}\n') for i in plist]

            print(f'\nFILE CREATED IN: "{os.getcwd()}"\n')

        except(FileExistsError):
            print(f'\n"{name}.txt" HAS ALREADY BEEN CREATED!\n')

    else:
        print('\nURL IS INVALID!\n')
