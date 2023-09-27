import requests
from bs4 import BeautifulSoup


def extrac_data():
    # Data BMKG per 26 September 2023
    try:
        link = requests.get('https://www.bmkg.go.id/')
        print(link.status_code)  # Cek Status Request
    except Exception:
        return None

    if link.status_code == 200:
        soup = BeautifulSoup(link.text, 'html.parser')  # Tell BS4 we using HTML Link

        result = soup.find('span', {'class': 'waktu'})  # Search Tag Span on HTML with Key is Class and Value is Waktu
        result = result.text.split(', ')  # Spliting Tanggal and Waktu into List
        tanggal = result[0]
        waktu = result[1]

        # Find New Tag that split from Span Tag
        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        # Default Value
        i = 0
        magnitudo = None
        kedalaman = None
        lu = None
        bt = None
        lokasi = None
        diraskan = None

        # Change the HTML Text into List, and print it using For in
        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                lu = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                diraskan = res.text
            i = i + 1

        data = dict()  # Dictionary
        data['tanggal'] = tanggal
        data['waktu'] = waktu
        data['magnitudo'] = magnitudo
        data['kedalaman'] = kedalaman
        data['koordinat'] = {'lu': lu, 'bt': bt}
        data['lokasi'] = lokasi
        data['dirasakan'] = diraskan
        return data


def view_data(result):  # Show The Result From extract_data Function
    print(result)
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : LU = {result['koordinat']['lu']} BT = {result['koordinat']['bt']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Dirasakan : {result['dirasakan']}")
