def extrac_data():
    # Data BMKG per 26 September 2023
    data = dict()
    data['date'] = '26 September 2023'
    data['magnitudo'] = 6.3
    data['deep'] = 115
    data['location'] = {'lu': 4.63, 'bt': 127.38}
    return data


def view_data(result):
    print(result)
    print(f"Date : {result['date']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Deep : {result['deep']}")
    print(f"Location : LU = {result['location']['lu']} BT = {result['location']['bt']}")

