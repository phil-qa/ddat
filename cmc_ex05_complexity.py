# Title: cmc_ex_05_complexity
# Purpose : To review the idea of complex code
# Instructions : Review the code below and determine the
# complexity
import urllib.request
import BeautifulSoup as bs

def word_count(search_word, target):
    '''
    Accepts search_word and returns the number of times seen in links on a page
    :param target: base url to search
    :param search_word: word to search for
    :return:
    '''

    target_url = target
    response = urlli(target.format(search_word))
    total_hit_count = 0

    if response is not None:
        html_page = bs(response, 'html.parser')

        word_hit_links = [link for link in html_page.select('a')
                     if link['href'].find(search_word)]

        if len(word_hit_links) >0 :
            total_hit_count += count(search_word, )

