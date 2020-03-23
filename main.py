import os
import requests
import time
from bs4 import BeautifulSoup


# RUBY terminal-notifier INITIATOR FUNCTION
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# FUNCTION TO LOAD THE URL AND FETCH HTML
def get_data(url):

    r = requests.get(url)

    return r.text

# FUNCTION TO PRETTIFY DATA FOR PAKISTAN
def parse_data_pakistan(soup):

     count = 1

     initial = soup.find("div", class_="col-12 col-md-6 wow fadeInUp")

     string = "Total : " + initial.h1.text + "  "

     for div in soup.findAll("div", {"class": "col-12 col-md-4"}):

         string = string + div.h6.text +": " + div.h4.text + "  "
    
     return string

# FUNCTION TO PRETTIFY DATA FOR STATES
def parse_data_states(soup):

     count = 1


     string = ""

     for div in soup.findAll("div", {"class": "col"}):

         string = string + div.h6.text +": " + div.h4.text + "  "
    
     return string

         

        

if __name__ == "__main__" :

    
    while True :
    
            # Official Pakistan covid response website
            my_url = get_data("http://www.covid.gov.pk/")
            
            soup = BeautifulSoup(my_url, 'html.parser')
        
            parsed_data_pakistan = parse_data_pakistan(soup)
            parsed_data_states = parse_data_states(soup)

            notify(title    = 'Corona Virus Statistics',subtitle = 'Overall Pakistan',message  = parsed_data_pakistan)

            time.sleep(10)

            notify(title    = 'Corona Virus Statistics',subtitle = 'Individual States',message  = parsed_data_states)

            time.sleep(500)

    

    


 

  





