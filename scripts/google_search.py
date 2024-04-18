#!/usr/bin/python3
import sys
import webbrowser
from bs4 import BeautifulSoup

string_arg = sys.argv[1]


def search_youtube_in_brave(query):
    # Replace 'brave' with 'google-chrome' if you're using Chrome
    browser = webbrowser.get()
    # register brave
    # webbrowser.register(
    #     "brave-browser --incognito", None, webbrowser.GenericBrowser("brave-browser --incognito")
    # )

    #if using chrome
    webbrowser.register(
       "google-chrome --incognito", None, webbrowser.GenericBrowser("google-chrome --incognito")
    )
    #google search the arg
    google_url = f"https://www.google.com/search?q={query}"
    
    # Open the YouTube search results in Brave
    browser.open(google_url)


def main():
    # search_query = string_arg
    search_query = string_arg
    search_youtube_in_brave(search_query)


if __name__ == "__main__":
    main()
