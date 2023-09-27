import bmkg

"""
Main Application For Data Scrapping Website BMKG Done
"""

if __name__ == "__main__":
    print("Main Application")
    result = bmkg.extrac_data()
    bmkg.view_data(result)
