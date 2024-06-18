# YouTube-Music-Download
Local web-page created with Flask and pytube, designed to download audio and/or video from YouTube. Works on Windows and Linux!

The time taken to display results may vary based on your internet speed. Files are downloaded into your default "Downloads" folder.

*Please note, this tool does not support downloading age-restricted YouTube content, live-streams/podcasts, or Youtube Movies/TV.
(This is due to current limitations with pytube's authentication support.)

# Getting Started
   Start by cloning this repo...
    
    `git clone https://github.com/Codex-Major/YouTube-Music-Download`
    
  This tool requires [pytube](https://pypi.org/project/pytube/) and [Flask](https://pypi.org/project/Flask/) ...
  
    `python3 -m pip install pytube flask`

  Launching the web-server:

    `python3 -m pip flask --app main run`

# Index page
  [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
  
  ![pytube-downloader_index_page](https://github.com/Codex-Major/YouTube-Music-Download/assets/39181001/ec81c3b8-78fe-4484-a2ef-b0881af6bcf7)


# Search page
  [http://127.0.0.1:5000/search](http://127.0.0.1:5000/search.html)
  
  ![pytube-downloader_search-page](https://github.com/Codex-Major/YouTube-Music-Download/assets/39181001/bcca8407-9f7a-46c8-8c87-c3f17c0fb57c)
