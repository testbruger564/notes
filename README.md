# notes
Notes.py is app to take quick notes.

You must add notes.py yourself so that it is globally available

Makes notes globally avaliable for current user.

$ vi .bashrc
  
  add the following lines to the .bashrc file.
  Change from command mode to insert mode by pressing i
  
    export PATH=~/notes:$PATH

    alias notes='notes.py'
  
  Save and exit the file by pressing ESC followed by :wq 

Makes notes globally available for all users.

$ sudo cp notes/notes.py /usr/local/bin/
