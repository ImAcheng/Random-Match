# Random Match
This is a simple program which is designed to be a teaching tool.

## IMPORTANT
Something you need to know before using.
* Because of the pygame module, you might not able to open the python file in file explore.
* To open the py file, please open this stuff in IDE.
* Now, the program includes both of the console and window version.

## Usage
Launch
* The program now automatically starts in windowed mode.
* You can change to launch mode by modifying [Settings.json -> Language] in "UserData" folder.

Window Mode
* Just click on the UI elements!

Console Mode - Enter the commands below to use it.
- help ({command}) - Show all commands (or specific command's details).
- match - Main function. Use it to match random name to random object.
- add {target} {name} - Add a new name / object to the database.
- remove {target} {name} - Remove a name / object from the database.
- load {target} {path}. Load content to the list(name / object) from a file.
- clear {data} - Clear data(name / object / all) from the database.
- print {target} - Show all content in the list(name / object).
- stop - Stop program.

## Version
- Release 2.1.0 (All additions / changes / removes / improvements)
  - Added Multi-Language system [ Supports English (us) / Spanish / Chinese (Traditional) ].
  - Added Resource Packs system [ You can change the textures of the program ].
  - Added Advanced Settings system [ You can change some details of the program ].
  - Added a new title image.
  - Added Cursor Statement system [ The cursor would be changed if it were in the buttons ].
  - Added a debug icon (CouldNotFindFileAnywhere.png) [ Please DO NOT remove it ].
  - Added a new splash animation.
  - Improved the textures loading performance.
  - Changed some texts.
  - Some technical details (which means I've already forgotten.)

- Explanations
  - What is Resource Packs system?
    - Well, if you didn't like the original textures, you could draw new ones and apply them to the program easily!
  - What is Advanced Settings system?
    - It means some settings that I use while developing. I think they're useful, so I put them into the program.
  - Why can't we delete the debug icon?
    - It's the last texture the program can load, which means if you ACCIDENTALLY DELETED the textures from Program Data,
    the program could load this texture. 
    If you ACCIDENTALLY DELETED this texture, too, you might not able to open the program anymore.
  
- Release date: Sep. 9th, 2024
    
#
©2024 Lonely Work (Lonely Acheng a.k.a. ChengDev) All Rights Reserved.
