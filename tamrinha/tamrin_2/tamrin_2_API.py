#این کد برای سال های شمسی استفادهمیشود
import requests
 
year = input("Enter a Persian year: ")
url = f"https://api.ineo-team.ir/kabiseh.php?year={year}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data["result"]["is_kabiseh"] == "yes":
        print(f"{year} is a leap year in the Persian calendar.")
    else:
        print(f"{year} is not a leap year in the Persian calendar.")
else:
    print("Error retrieving data from API")
    

