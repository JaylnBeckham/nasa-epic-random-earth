import requests

# Function 1: Gets photos from NASA's EPIC API
def get_photos(api_key, date):
# Create the URL using the date entered
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}"
# Request information from NASA
    try:
        response = requests.get(url, timeout=15)
# Check if the request was successful
        if response.status_code == 200:
            photos = response.json()
            return photos

        else:
            print("Error: NASA could not retrieve the data.")
            print("Status code:", response.status_code)
            return None

    except requests.exceptions.RequestException:
        print("Error: Could not connect to NASA.")
        return None
# Function 2: Count how many pictures were taken
def count_photos(photos):
# Count the number of pictures in the list
    total = len(photos)

    return total
# Function 3: Display the pictures and their information
def show_photos(photos):
# Go through each picture in the list
    for photo in photos:
# Get the image name and date from the dictionary
        image = photo["image"]
        date = photo["date"]
# Separate the date from the time
        date_only = date.split(" ")[0]
# Change the date format for the image link
        formatted_date = date_only.replace("-", "/")
# Create a link to the actual NASA picture
        link = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{image}.png"
# Display the picture information
        print("Image:", image)
        print("Date and Time:", date)
        print("Photo Link:", link)
        print("------------------------")
# Main program
# NASA's public demo API key
api_key = "DEMO_KEY"
# Ask the user to enter a date
date = input("Enter a date (YYYY-MM-DD): ")
# Retrieve the photos
photos = get_photos(api_key, date)
# Check if the request failed
if photos is None:
    print("Unable to display photos.")
# Check if NASA returned no pictures
elif len(photos) == 0:
    print("No pictures were taken on this date.")

else:
# Count the pictures
    total = count_photos(photos)

    print("Total pictures taken:", total)
# Display the picture information
    show_photos(photos)
