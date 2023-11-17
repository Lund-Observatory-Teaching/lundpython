To generate new title slide images, run the bash script in this folder.
The names of the teachers should be listed in the 'teachers' variable (strings separated by spaces) and their email addresses in the 'contact' variable (space separated).
This requires ImageMagick (on my Linux computer at least) to run.
There could possibly be a problem with the specified font not being available to you. Either install it or change the script to one that you have access to. At time of writing the fonts are of the Liberation family which are open source and should be available on all operating systems.
To list what fonts are available to use, run 'magick -list font'.
