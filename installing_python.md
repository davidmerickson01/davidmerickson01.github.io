# Installing Python

* Go to <https://www.python.org>
* Click the "Downloads" menu item
* If you run Windows, click "Download Python 3.14.0" or whatever the latest version is.
    * If you run Mac, there are instructions after "Not the OS you are looking for?".
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

# Changing the default folder for IDLE

When starting Python IDLE, it's helpful if it points to your own folder of code, not the Python binaries.

Here's how you can change it on Windows:

* From start menu, right click “Open File Location”
* On IDLE binary, right click “Properties”
* Edit “Start In” text box
* An easy technique is to copy yuor location from Windows Explorer, then paste here

*WARNING: Don’t change “Target” text box! And if you mess any of this up, just reinstall Python*

# Using pip to install packages on Windows

pip is the Python Package Installer. You need it to extend your standard python installation with other modules. (pip is a recursive acronym which means "Pip Installs Packages").

* Click Windows button in left corner
* Type "cmd" and select "Command Prompt". You may need to right-click and "Run as Administrator".
* Type "pip". It should find the program and print help.

*If it says "pip not found", then you need to uninstall and reinstall Python and follow my "IMPORTANT: click the "Add Python 3.10 to PATH" checkbox!" advice above.*

* Now, find out what packages you have by running "pip list"
* Some packages we're going to use: pygame, requests, 

* Type "pip install pygame". You will see something like the following:

        Collecting pygame
          Downloading pygame-2.0.2-cp310-cp310-win_amd64.whl (5.3 MB)
             |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| 5.3 MB 656 kB/s
        Installing collected packages: pygame
        Successfully installed pygame-2.0.2

You may see a warning "A new release of pip is available". Just follow the instructions.

# Using pip on Mac

The following are modifications to the previous Windows directions

* Instead of running "cmd", run "Terminal"
* Instead running "pip install pygame", run "pip3 install pygame" or "python3 -m pip install -U pygame --user"
