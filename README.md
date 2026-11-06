# <nasa-epic-random-earth>

<This program uses NASA's EPIC API to show how many pictures of Earth were taken on a date entered by the user. It uses dictionary keys like "date" and "image" to display photo names, dates, times, and links to view them. If no pictures are available, the program displays a message instead of an error.>

## How it works
- <function_1>: <Gets photos from NASA's EPIC API from a specific day the user inputs>
- <function_2>: <it displays how many photos were taken of the Earth on the day the user inputs>
- <function_3>: <Goes through the pictures NASA took and gives the image name, date, time, and a link to the picture>

## How to run
1. Install requests: pip install requests
2. Run: python <your_file_name>.py
3. Uses "DEMO_KEY" by default. Swap in your own key
   from api.nasa.gov for higher rate limits.

## Built with
Python, requests and the NASA EPIC API
