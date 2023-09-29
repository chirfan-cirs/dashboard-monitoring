import requests
from bs4 import BeautifulSoup


def extrac_data():
    # Data BMKG per 26 September 2023
    try:
        link = requests.get('https://www.detik.com/')
        # print(link.status_code)  # Cek Status Request
    except Exception:
        return None

    if link.status_code == 200:
        soup = BeautifulSoup(link.text, 'html.parser')  # Tell BS4 we using HTML Link

        result = soup.find('div', {'class': 'berita-utama mgb-12'})  # Search Tag div on HTML with Key is Class and
        # Value is berita-utama mgb-12 (Scraping Data From 'Berita Utama')
        result = result.findChildren('h2')  # Get the Children element from class media_text (h2) / media title

        # Default Value
        i = 0
        nol = None
        satu = None
        dua = None
        tiga = None
        empat = None

        # Change the HTML Text into List, and print it using For in
        for res in result:
            # print(i, res)  # Using this code for showing witch data will show up
            if i == 0:
                nol = res.text
            elif i == 1:
                satu = res.text
            elif i == 2:
                dua = res.text
            elif i == 3:
                tiga = res.text
            elif i == 4:
                empat = res.text
            i = i + 1

        data = dict()  # Dictionary
        data['nol'] = nol
        data['satu'] = satu
        data['dua'] = dua
        data['tiga'] = tiga
        data['empat'] = empat
        return data


def view_data(result):  # Show The Result From extract_data Function
    # print(result)
    print(f"Berita Populer 1 : {result['nol']}")
    print(f"Berita Populer 2 : {result['satu']}")
    print(f"Berita Populer 3 : {result['dua']}")
    print(f"Berita Populer 4 : {result['tiga']}")
    print(f"Berita Populer 5 : {result['empat']}")
