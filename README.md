# NameGame
A game to teach my daughter the names of her familiy members and their relationship to her. Will use random number generation for family members, text to speech to interact with her, and speech recognition for her to interact with it.

# Install Requirements
`sudo apt-get install swig python3-dev libpulse-dev libasound2-dev portaudio190dev python-pyaudio python3-pyaudio`

## Main Directory
### classes.py
- File contains all the classes that will be used in the games. Currently only the button class is created
**TO DO**
- [ ] Create class to handle all the photos
### family.db
- The database that contains the information about my daughters family. Basic knowledge with no NPI
**TO DO**
- [ ] Add missing family members
### helper_functions.py
- All of the custom functions that are shared by the various game scripts including:
  * display() - Handles the PyGame surface and support for full screen
  * change_bgcolor() - Used to change the background color of the current surface
  * _dict_factory() - Helper function for get_database that returns the data as a dictionary
  * get_database - Used to pull specific fileds from a given table and database
  * show_img() - Function to show a person's picture to the provided surface
  * speak() - Function handles all the spoken lines for the interface
### mainmenu.py
- Script that uses buttons to allow selection of game to play
### name2person.py
- The game to match one of three pictures to a given name
**TO DO**
- [ ] Refactor to get more OOP style coding
### relationships2person.py
- The game to match one person's picture to one of three relationships
### variable.py
- Variables shared by all the scripts including: a color dictionary and a blank name varialbe dictionary for the name2person.py game.



# Archived
## Main directory
### database.py
This scirpt interacts with the database and table passed in the get_database() function and returns all info in the database
**To Do**
- [X] Send table fields as argument instead of having them hard coded
### diplay.py
This script is used to create the maine PyGame surface based on the caption, dimentions, and backgroup color.
**To Do**
- [ ] Add the ability to create subsurfaces as well
### family.db
The database that contains the info about my daughters family. Pretty basic knowledge with no NPI
### main.py
This will be the script that will eventually interact with all the various game scripts to be a main menu for her to pick the games
### name2person.py
The first game that provides three picture and ask her to identify one of them by name
**To Do**
- [ ] Refactor to a more object OOP format the help with removing redundant code and better organize
- [X] Work with images to get similar sizes
- [ ] See if I can find a graphics person to help me design the interface
### speech.py
This script handles all the speech interaction using Google Text to Speech (even though it has to be on line, we like the pleasant voice)
**To Do**
- [ ] Include an offline voice interface for on the go play
- [ ] Develop speech recognition to allow her to interact with the games by voice
### variables.py
This fill contains the variables of the various scripts. The purpuse of this file is to keep them all in one place so they can be easily update if required