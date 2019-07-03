from shutil import copy
import os

STEAM_ID = "YOUR_STEAM_ID3_HERE"    # example: 401500991
STEAM_PATH = "YOUR_STEAM_PATH_HERE" # default: C:\Program Files (x86)\Steam

TAIL_PATH = "/730/local/cfg"
MAIN_PATH = STEAM_PATH + "/" + STEAM_ID + TAIL_PATH

def main():
	sync = sync_cfg()
	print("Successfully Synced {0} CFGs".format(sync))

def sync_cfg():
	count = 0
	for subdir, dir, files in os.walk(STEAM_PATH):
		for file in files:
			try:
				f = str(os.path.join(subdir, file))
				if STEAM_ID in f:
					continue
				if "730" in f and "config.cfg" in f:
					dirs.append(str(f))
					copy(MAIN_PATH + "/config.cfg", f)
			except OSError as err:
				print("OS error: {0}".format(err))
		
	return count

if __name__ == "__main__":
	main()
