#!/usr/bin/python3
import os
import sys
import webbrowser

# string_arg = sys.argv[1]


def search_youtube_in_brave(query):
    # Replace 'brave' with 'google-chrome' if you're using Chrome
    #browser = webbrowser.get()
    # register brave
    webbrowser.register(
        "brave-browser", None, webbrowser.GenericBrowser("brave-browser")
    )

    #replace spaces with +
    query = query.replace(" ", "+")
    # URL to the YouTube search results page with the query
    youtube_url = f"https://www.youtube.com/results?search_query={query}"

    os.system(f'curl {youtube_url} > temp.txt')

    with open("temp.txt", "r") as f:
        data = f.read()

    start = 0

    instances = []

    while True:
        start = data.find('href="/watch?v=', start)
        #find the next occurance of "
        temp = data[start+len('href="/watch?v='):]
        end = temp.find('"')
        
        if start == -1:
            break
        video_id = temp[:end]


    # Open the YouTube search results in Brave
    #browser.open(youtube_url)

   


def main():
    # search_query = string_arg
    search_query = "bad bunny monaco"
    search_youtube_in_brave(search_query)


if __name__ == "__main__":
    main()
