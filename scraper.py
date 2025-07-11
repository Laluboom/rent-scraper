
import requests 

london_rent_urls = [
    "https://www.rightmove.co.uk",
    "https://www.zoopla.co.uk",
    "https://www.openrent.co.uk",
    "https://www.foxtons.co.uk",
    "https://www.primelocation.com",
    "https://www.gumtree.com",
    "https://www.spareroom.co.uk",
    "https://www.lovetorent.co.uk",
    "https://www.idealflatmate.co.uk",
    "https://www.roomgo.co.uk",
    "https://www.onthemarket.com",
    "https://www.marshandparsons.co.uk",
    "https://www.kfh.co.uk",        
    "https://www.chancellors.co.uk",
    "https://www.dexters.co.uk",
    "https://www.housescape.org.uk",
    "https://www.barnardmarcus.co.uk",
    "https://www.winkworth.co.uk",
    "https://www.ludlowthompson.com",
    "https://www.lurotbrand.co.uk"
]

for link in london_rent_urls: 
    html_page = requests.request('GET',link,)
    print(link)
    print(html_page)
