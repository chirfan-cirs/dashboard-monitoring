import detik
import bmkg
"""
Main Application For Data Scrapping Data from Detik.com and BMKG
"""

if __name__ == "__main__":
    print("Main Application Data from Detik")
    result = detik.extrac_data()
    detik.view_data(result)

    print("")
    print("Main Application Data from BMKG")
    result = bmkg.extrac_data()
    bmkg.view_data(result)
