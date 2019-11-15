from pathlib import Path
from pprint import pprint

import pandas as pd
from requests_html import HTMLSession

if __name__ == '__main__':
    DATA = Path(__file__).parent / "data"
    GA_COUNTIES = ["Appling", "Atkinson", "Bacon", "Baker", "Baldwin", "Banks",
                   "Barrow", "Bartow", "Ben Hill", "Berrien", "Bibb",
                   "Bleckley", "Brantley", "Brooks", "Bryan", "Bulloch",
                   "Burke", "Butts", "Calhoun", "Camden", "Candler", "Carroll",
                   "Catoosa", "Charlton", "Chatham", "Chattahoochee",
                   "Chattooga", "Cherokee", "Clarke", "Clay", "Clayton",
                   "Clinch", "Cobb", "Coffee", "Colquitt", "Columbia", "Cook",
                   "Coweta", "Crawford", "Crisp", "Dade", "Dawson", "De Kalb",
                   "Decatur", "Dodge", "Dooly", "Dougherty", "Douglas",
                   "Early", "Echols", "Effingham", "Elbert", "Emanuel",
                   "Evans", "Fannin", "Fayette", "Floyd", "Forsyth", "Franklin",
                   "Fulton", "Gilmer", "Glascock", "Glynn", "Gordon", 'Grady',
                   "Greene", "Gwinnett", "Habersham", "Hall", "Hancock",
                   "Haralson", "Harris", "Hart", "Heard", "Henry",
                   "Houston", "Irwin", "Jackson", "Jasper", "Jeff Davis",
                   "Jefferson", "Jenkins", "Johnson", "Jones", "Lamar",
                   "Lanier", "Laurens", "Lee", "Liberty", "Lincoln", "Long",
                   "Lowndes", "Lumpkin", "Macon", "Madison", "Marion",
                   "McDuffie", "McIntosh", "Meriwether", "Miller", "Mitchell",
                   "Monroe", "Montgomery", "Morgan", "Murray", "Muscogee",
                   "Newton", "Oconee", "Oglethorpe", "Paulding", "Peach",
                   "Pickens", "Pierce", "Pike", "Polk", "Pulaski", "Putnam",
                   "Quitman", "Rabun", "Randolph", "Richmond", "Rockdale",
                   "Schley", "Screven", "Seminole", "Spalding", "Stephens",
                   "Stewart", "Sumter", "Talbot", "Taliaferro", "Tattnall",
                   "Taylor", "Telfair", "Terrell", "Thomas", "Tift", "Toombs",
                   "Towns", "Treutlen", "Troup", "Turner", "Twiggs", "Union",
                   "Upson", "Walker", "Walton", "Ware", "Warren", "Washington",
                   "Wayne", "Webster", "Wheeler", "White", "Whitfield",
                   "Wilcox", "Wilkes", "Wilkinson", "Worth", ]

    url = "https://broadbandnow.com/Georgia"
    session = HTMLSession()
    response = session.get(url)
    print(response)
    response.html.render()
    broadban = []
    broadban_append = broadban.append
    for idx in range(3, 162):
        sel = f'#svg-map > svg > path:nth-child({idx})'
        info = response.html.find(sel)
        broadban_append(info[0].attrs["fill-opacity"])

    ga_broadband = dict(zip(GA_COUNTIES, broadban))
    ga_df = pd.DataFrame.from_records([ga_broadband])

    ga_df.T.to_excel((DATA / "ga_broadband.xlsx"))
