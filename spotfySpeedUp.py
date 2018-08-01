# SpotifySpeedUp
# Deletes current user's local cache to speed up Spotify
# Jason Hammett
# Used the following forum to create this script
# https://community.spotify.com/t5/Desktop-Windows/Why-is-my-spotify-often-so-slow/td-p/703153

import os
import psutil
import sys
import shutil

print("SpotifySpeedUp:")
# Running tally of number of deleted items
numFiles = 0
numDirs = 0

# Check is spotify is currently running, close it
pids = psutil.pids()
for pid in pids:
	p = psutil.Process(pid)
	if "spotify" in p.name():
		print("Spotify is currently running. Close it and re-run.")
		sys.exit(1)

# Grab the current username
userName = os.getlogin()

#Navigate to the Spotify cache directory
spotifyCacheLoc = "\\AppData\\Local\\Spotify"
cDrive = "C:\\Users\\"
location = cDrive + userName + spotifyCacheLoc
os.chdir(location)

# Iterate through directories, deleting all inside but not folder
cacheDirs = ["Storage", "Data", "Browser"]
for cache in cacheDirs:
	os.chdir(cache)
	files  = os.listdir()
	print("Deleting contents from " + cache)
	for f in files:
		try:
			if os.path.isdir(f):
				shutil.rmtree(f)
				numDirs += 1
			else:
				os.remove(f)
				numFiles += 1
		except:
			print("Failed: Is Spotify running? If so, close it and try again.")
			sys.exit(-1)
	# Go back a level
	os.chdir("..")

print("Completed.")
print("Deleted " + str(numDirs) + " directories and " + str(numFiles) + " files.")