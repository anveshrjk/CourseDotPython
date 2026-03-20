import requests


def fetch_random_user_freeapi():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        # username = user_data["login"]["username"]
        name = user_data["name"]["title"] + ' ' + user_data["name"]["first"] + ' ' +  user_data["name"]["last"]
        country = user_data["location"]["country"]
        return name, country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        name, country = fetch_random_user_freeapi()
        print(f"Name: {name} \nCountry: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
