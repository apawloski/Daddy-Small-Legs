This was a quick project designed to find broken links and bad images on a given domain.

USAGE: $ python daddy.py $BASE_DOMAIN_URL

OUTPUT: bad_links.log	 <- list of all bad links found during crawl
	bad_images.log	 <- list of all bad images found during crawl

The first line of these output files is the number of bad links or images found. This is convenient for interacting with a nagios plugin or similar monitoring utility -- they just have to check the first line of the bad_*.log file. Two bare-bone nagios plugins are included as examples.

Requires BeautifulSoup and requests.
