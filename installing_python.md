# Installing Python

* Go to <https://www.python.org>
* Click the "Downloads" menu item
* If you run Windows, click "Download Python 3.10.0" or whatever the latest version is.
    * If you run Mac, there are instructions after "Looking for Python with a different OS?".
    * If you use Chromebook, Python should already be included. Press Ctrl+Alt+T for a terminal, then type "python3".
* After it downloads, run the ".exe" file, usually by clicking on the download button at the bottom of the browser

*IMPORTANT: click the "Add Python 3.10 to PATH" checkbox! You need this to run python from a command prompt (which I will teach you about.)*

* Then click "Install Now" (If you forget to do this, just install again.)
* Windows "User Account Control" will ask you, "Do yuo want to allow this app to make changes to your device?" Click Yes.
* When you see "Setup was successful", then click "Close"
* Click the Windows button in the lower left and type "IDLE (Python 3.10...)".
* It will launch a program called "IDLE Shell" which prints text like this:

        Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license()" for more information.
        >>>

* Now you are ready to program in Python!

# Your First Program

Type this after the "\>\>\>" prompt and press Enter:

    
    print("Hello World!")
    

You have begun!

# Learning on your own

* Go to <https://www.python.org>
* Click the "Documentation" menu item. 
* Find something that looks interesting. If you don't know, click on "Beginner's Guide" and read a bit.

# Installing pygame

* We're going to use <https://www.pygame.org> to create 2D games. Click on "Getting Started" for installation instructions. Or do the following...
* Click Windows button in left corner
* Type "cmd" and press Enter. It will launch a program called "Command Prompt"
* Type "pip install pygame". This will run the "python installer program" and install the pygame package. You will see something like the following:

        Collecting pygame
          Downloading pygame-2.0.2-cp310-cp310-win_amd64.whl (5.3 MB)
             |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| 5.3 MB 656 kB/s
        Installing collected packages: pygame
        Successfully installed pygame-2.0.2

* You may see this warning:

        WARNING: You are using pip version 21.2.3; however, version 21.2.4 is available.
        You should consider upgrading via the 'C:\Users\david\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip' command.

* If you want, you can also upgrade pip as instructed. Just type this "python -m pip install --upgrade pip" and press Enter.
