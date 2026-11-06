import requests
# This function gets pictures from NASA's EPIC API
def get_photos(api_key, date):
# Uses the date entered by the user
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}"
# Sends a request to NASA
    response = requests.get(url)
# Checks if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Could not retrieve pictures.")
        return None
# This function counts how many pictures NASA took
def count_photos(photos):
    return len(photos)
# This function displays information about each picture
def show_photos(photos):

    for photo in photos:
# Gets the image name and date from the dictionary
        image_name = photo["image"]
        photo_date = photo["date"]

# Gets the year, month, and day
        year = photo_date[0:4]
        month = photo_date[5:7]
        day = photo_date[8:10]

# Creates a link to view the picture
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png"

        print("Image Name:", image_name)
        print("Date and Time:", photo_date)
        print("Image Link:", image_url)
        print()
# Main program
def main():

    print("Welcome to NASA's Earth Photo Explorer!")
# Enter your NASA API key
    api_key = "YOUR_API_KEY"
# Asks the user for a date
    date = input("Enter a date (YYYY-MM-DD): ")
# Gets pictures using the user's date
    photos = get_photos(api_key, date)
# Checks if pictures were found
    if photos is not None:

        if len(photos) > 0:
# Displays the total number of pictures
            total = count_photos(photos)
            print("Total pictures found:", total)
            print()
# Displays information about the pictures
            show_photos(photos)

        else:
            print("No pictures were found for that date.")
# Runs the program
if __name__ == "__main__":
    main()
