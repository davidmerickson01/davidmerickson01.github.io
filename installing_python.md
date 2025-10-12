# Installing Python

* Go to <https://www.python.org>
* Click the "Downloads" menu item
* If you run Windows, click "Download Python 3.14.0" or whatever the latest version is.
    * If you run Mac, there are instructions after "Looking for Python with a different OS?".
    * If you use Chromebook, Python should already be included. Press Ctrl+Alt+T for a terminal, then type "python3".
* After it downloads, run the ".exe" file, usually by clicking on the download button at the bottom of the browser
* Before cliking "Install Now", first click the "Add python.exe to PATH" checkbox at the bottom of the dialog!
    * You need this to run python from a command prompt (which I will teach you about.)*

* Now click "Install Now"
* Windows "User Account Control" will ask you, "Do you want to allow this app to make changes to your device?" Click Yes.
* When you see "Setup was successful", then click "Close"
* Click the Windows button in the lower left and type "IDLE (Python 3.14 64 bit)".
* It will launch a program called "IDLE Shell" which prints text like this:

        Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
        Enter "help" below or click "Help" above for more information.
        >>>

* Now you are ready to program in Python!

Other notes:

* We are not using Python 2, and the syntax does not match Python 3. If you have Python 2 installed, or an earlier version of Python 3, you probably want to uninstall that first.

# Your First Program

Type this after the "\>\>\>" prompt and press Enter:

    
    print("Hello World!")
    

You have begun!

# Learning on your own

* Go to <https://www.python.org>
* Click the "Documentation" menu item. 
* Find something that looks interesting. If you don't know, click on "Beginner's Guide" and read a bit.

# Installing pygame on Windows

* We're going to use <https://www.pygame.org> to create 2D games. Click on "Getting Started" for installation instructions. Or do the following...
* Click Windows button in left corner
* Type "cmd" and select "Command Prompt". You may need to right-click and "Run as Administrator".
* Type "pip install pygame". This will run the "python installer program" and install the pygame package. You will see something like the following:

        Collecting pygame
          Downloading pygame-2.0.2-cp310-cp310-win_amd64.whl (5.3 MB)
             |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| 5.3 MB 656 kB/s
        Installing collected packages: pygame
        Successfully installed pygame-2.0.2

* If it says "pip not found", then you need to uninstall and reinstall Python and follow my "IMPORTANT: click the "Add Python 3.10 to PATH" checkbox!" advice above.
* You may see this warning:

        WARNING: You are using pip version 21.2.3; however, version 21.2.4 is available.
        You should consider upgrading via the 'C:\Users\david\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip' command.

* If you want, you can also upgrade pip as instructed. Just type this "python -m pip install --upgrade pip" and press Enter.

# Installing pygame on Mac

The following are modifications to the previous Windows directions

* Instead of running "cmd", run "Terminal"
* Instead running "pip install pygame", run "pip3 install pygame" or "python3 -m pip install -U pygame --user"
