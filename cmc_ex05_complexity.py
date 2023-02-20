# Title: cmc_ex_05_complexity
# Purpose : To review the idea of complex code
# Instructions : Review the code below and determine the
# complexity
import urllib.request
from bs4 import BeautifulSoup as bs

def word_count(target, search_word):
    '''
    Accepts search_word and returns the number of times seen in links on a page
    :param target: base url to search
    :param search_word: word to search for
    :return:
    '''
    response = urllib.request.urlopen(target)
    total_hit_count = 0

    if response is not None:
        html_page = bs(response, 'html.parser')

        word_hit_links = [link for link in html_page.select('a')
                     if search_word in link]

        if len(word_hit_links) >0 :
            for link in word_hit_links:
                total_hit_count += link.count(search_word)
                if total_hit_count > 0:
                    if total_hit_count < 10:
                        print('Less than 210 found')
                    elif total_hit_count >10 and total_hit_count <20:
                        print('there was a standard value found')

    if total_hit_count == 0:
        return "No hits found"
    else:
        return f"There were {total_hit_count} Hits"


were_there_words = word_count('https://en.wikipedia.org/wiki/Natural_gas', 'gas')
print(were_there_words)

