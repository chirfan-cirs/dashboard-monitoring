import requests
from bs4 import BeautifulSoup
def extrac_data():
    # Data BMKG per 26 September 2023
    try:
        link = requests.get('https://bmkg.go.id/')
        print(link.status_code)
        # print(link.text)
    except Exception:
        return None

    if link.status_code == 200:
        soup = BeautifulSoup(link.text, 'html.parser') #Tell BS4 we using HTML Link

        result = soup.find('span', {'class': 'waktu'}) #Search Tag Span on HTML with Key is Class and Value is Waktu
        result = result.text.split(', ') #Spliting Tanggal and Waktu into List
        tanggal = result[0]
        waktu = result[1]

        data = dict()
        data['tanggal'] = tanggal #'26 September 2023'
        data['waktu'] = waktu #'08:39:47 WIB'
        data['magnitudo'] = 6.3
        data['deep'] = 115
        data['location'] = {'lu': 4.63, 'bt': 127.38}
        return data


def view_data(result):
    print(result)
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Deep : {result['deep']}")
    print(f"Location : LU = {result['location']['lu']} BT = {result['location']['bt']}")

