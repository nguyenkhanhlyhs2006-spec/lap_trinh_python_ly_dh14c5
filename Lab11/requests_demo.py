
import requests

# Bai tap 5.1: Goi API GitHub
print("===== API GITHUB =====")

url_github = "https://api.github.com/repos/python/cpython"

response = requests.get(url_github, timeout=15)

if response.status_code == 200:

    du_lieu = response.json()

    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao:", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])

else:
    print("Goi API that bai, ma loi:", response.status_code)


# Bai tap 5.2: Goi API ty gia ngoai te
print("\n===== API TY GIA NGOAI TE =====")

url_ty_gia = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url_ty_gia, timeout=15)

if response.status_code == 200:

    du_lieu = response.json()

    if du_lieu["result"] == "success":

        ty_gia_vnd = du_lieu["rates"]["VND"]

        print(f"1 USD = {ty_gia_vnd:,.0f} VND")

    else:
        print("API khong tra ve du lieu hop le")

else:
    print("Goi API that bai, ma loi:", response.status_code)
