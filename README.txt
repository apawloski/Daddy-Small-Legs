This was a quick project designed to find broken links and bad images on a given (as of now hardcoded) domain.

Any bad images or links are saved in their respective log files (bad_*.log). The first line of these files is the number of bad links or images found. This is convenient for interacting with a nagios plugin or similar monitoring utility -- they just have to check the first line of the bad_*.log file. Two bare-bone nagios plugins are included as examples.

Requires BeautifulSoup and requests.
