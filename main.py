import detik
import bmkg
"""
Main Application For Data Scrapping Data from Detik.com
"""

if __name__ == "__main__":
    print("Main Application Data from Detik")
    result = detik.extrac_data()
    detik.view_data(result)
    print("Main Application Data from BMKG")
    result = bmkg.extrac_data()
    bmkg.view_data(result)
# import bmkg
#
# """
# Main Application For Data Scrapping Website BMKG Done
# """
#
# if __name__ == "__main__":
#     print("Main Application")
#     result = bmkg.extrac_data()
#     bmkg.view_data(result)
