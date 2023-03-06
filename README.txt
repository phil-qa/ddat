This repo contains all the exercises and proposed solutions for supporting DDAT MSE delivery.

Setup:
using the image supplied for the course, all machines should have network visibility of the instructor machine
clone the full repo set as the instructor (you should have done so to get this)
setup a new folder that will be student facing called exercises.git
Make the folder a network share, note the network share path.
navigate to the folder and open git bash in it
initialise a bare repository
git init --bare --shared
set the branch name mto main:
git symbolic-ref HEAD refs/heads/main
create a local folder that will interact with the new repository, DO NOT make the folder in this repository folder,
find somewhere else, call it exercises.
navigate to your new folder and open git bash.
clone the new repo using the path to the bare repo you just made
git clone [path]\\exercises.git

inform the delegates that they need to map a network location to the network shared path
inform the delegates to make a new folder called exercises on their machines
inform the delegates to navigate to that folder and open git bash at that location
inform the delegates to do a git clone on the repository eg:
git clone \\\\INSTRUCTOR\\repositories\\exercises.git

You may now copy an exercise from the full repo location into the folder exercises that you are using as the local
repository

git add the file
git commit the file
git push the file

ask the delegates to pull and confirm that they all have a copy of the file in their folders.

The recommendation is that the delegates then branch locally to keep their work separate. This also allows for instructor
to switch branches to assist with code and review progress.

pull in exercises and solutions as appropriate.
