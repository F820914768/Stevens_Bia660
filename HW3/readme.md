
# Crawler to fetch all emails from stevens

Three objects is defined:

### Crawler: 
To send requests to url with selenium and chromedriver

### UrlQueue: 
Inherit from queue.Queue object. put method and initialization is rewriten. Before put an url into queue, the queue object will check if the url has been visited before and if the url is of standard input.

### Writer: 
To write iterable object into text file.
