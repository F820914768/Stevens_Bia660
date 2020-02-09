'''
Yubo Feng stevens
HW 2

send requests to wikepedia, then save body of response into a html file locally
'''

import requests

from config import get_headers_from_config, get_url_from_config


if __name__ == '__main__':
    '''
    send requests to wikepedia, then save body of response into a html file locally
    '''
    url = get_url_from_config() # load url from config.ini
    headers = get_headers_from_config() # load headers from config.ini

    response = requests.get(url, headers = headers) # send requests to url

    html_body = response.content
    print(response.status_code)
    print(response.headers)
    
    with open('top-level-domain.html', 'wb') as htmlfile: # save html file locally
        htmlfile.write(html_body)


    
