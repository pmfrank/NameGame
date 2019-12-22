# NameGame
A game to teach my daughter the names of her familiy members and their relationship to her. Will use random number generation for family members, text to speech to interact with her, and speech recognition for her to interact with it.

## Main directory
### database.py
This scirpt interacts with the database and table passed in the get_database() function and returns all info in the database
**To Do**
- [ ] Send table fields as argument instead of having them hard coded
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
- [ ] Work with images to get similar sizes
- [ ] See if I can find a graphics person to help me design the interface
### speech.py
This script handles all the speech interaction using Google Text to Speech (even though it has to be on line, we like the pleasant voice)
**To Do**
- [ ] Include an offline voice interface for on the go play
- [ ] Develop speech recognition to allow her to interact with the games by voice
### textboy.py
This script allow a textbox to be created as a surface to take user input from the keyboard from the user
### variables.py
This fill contains the variables of the various scripts. The purpuse of this file is to keep them all in one place so they can be easily update if required