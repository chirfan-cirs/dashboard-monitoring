def extrac_data():
    data = dict()
    data['date'] = '26 September 2023'
    data['magnitudo'] = 6.3
    data['deep'] = 115
    return data


def view_data(result):
    print(result)
    print(f"Date : {result['date']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Deep : {result['deep']}")


if __name__ == "__main__":
    print("Main Application")
    result = extrac_data()
    view_data(result)

