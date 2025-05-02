# Local Spotify Shuffler

This project is a Spotify random shuffler that adds songs to your spotify queue from your liked songs!

## Quickstart

The shuffler works in two ways: as a terminal command or as a localhost website!

### Setup
To get started, you'll need to:
- Signup/Login with [Spotify for Developers] (https://developer.spotify.com/)
- Create a new app using the [Web API] (https://developer.spotify.com/dashboard/create) and any settings of your choosing! 
- Fill in the Client ID, Client Secret, and Redirect URI sections of the .env file with your app's information
- Fill in the User ID section of the .env file with your Spotify account's username

Great! the app is now set up and ready to shuffle!

### Run as Terminal Command
- Run the command `python main.py` to queue songs! The default number queued is 5
- Run the command with a number of songs to queue a specific number of songs (e.g. `python main.py 10`)

### Run as Local Website
- Run the command `python manage.py runserver` to spin up the local website!
- Go to the [website] (http://localhost:8000/) and start queueing songs!





