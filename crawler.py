# Broken link detector
#
# Traverses website and generates list of broken links and broken images
#

import sys, time, logging

from bs4 import BeautifulSoup
import requests

def main():
    url_stack = []
    visited_urls = set()
    visited_images = set()
    bad_urls = set()
    bad_images = set()

    # Set up logger
    FORMAT = "%(asctime)-15s %(message)s"
    logging.basicConfig(format=FORMAT, filename='crawl.log', filemode='w', level=logging.DEBUG)

    base_url = "http://www.example.com/"
    url_stack.append(base_url)
    
    # Crawl through the site, grab links/images
    while True:
        url = url_stack.pop()
        # Only visit link if it's on our site and we haven't visited it before
        if 'http://' in url and 'jacquette.com' in url and url not in visited_urls:
            resp = requests.get(url)
            if resp.status_code == requests.codes.ok:
                # Check for bad images on page
                for image in parse_for_images(resp):
                    if not check_img(image):
                        bad_images.add(image)
                        logging.info('BAD IMAGE: %s', image)
                # Grab links on page
                found_urls = parse_for_links(resp)
                for found_url in found_urls:
                    # Only push onto stack if we haven't visited it before
                    if found_url not in visited_urls:
                        url_stack.append(found_url)
            else:
                # If we get here, the status code wasn't ok => link is broken
                bad_urls.add(url)
                logging.info('BROKEN LINK: %s returns %s', url, resp.status_code)
            visited_urls.add(url)
            # This is to be nice to the server -- adjust as needed
            time.sleep(.5)            

        # This is the closest thing Python has to a do-while
        if len(url_stack) == 0:
            break

    # Report all the broken links found:
    f = open('bad_links.log', 'w')
    f.write(str( len(bad_urls) ) ) #First line
    for url in bad_urls:
        f.write(url)
    f.close()

    # Report all the bad images found:
    f = open('bad_images.log', 'w')
    f.write(str( len(bad_images) ) ) # First line
    for image in bad_images:
        f.write(image)
    f.close()

    sys.exit()

def parse_for_links(resp):
    """Returns a list of hyperlinks found in response. Empty list is returned if no links found"""
    links = []
    parser = BeautifulSoup(resp.text)
    # find anchor tags and parse for href
    for link in parser.find_all('a'):
        href = link.get('href')
        if href is None:
            print "Weird formatting", link
        else:
            links.append(link.get('href'))
    
    return links

def parse_for_images(resp):
    images = []
    parser = BeautifulSoup(resp.text)
    # find img tags and parse for href
    for image in parser.find_all('img'):
        src = image.get('src')
        if src is None:
            print "Weird formatting", image
        else:
            images.append(image.get('src'))

    return images

def check_img(url):
    resp = requests.get(url)
    return 'image' in resp.headers['content-type']

if __name__ == "__main__":
    main()
