import requests



def postData(number: int):

    for number in range(number):
        requests.post("http://127.0.0.1:8000/todo",
                             json={"id": number,
                                   "item": f"nummer{number}",
                                   "status": "God"
                                   }
                             ).json()


def getDatalist():
    data = requests.get("http://127.0.0.1:8000/todo").json()
    return data


postData(10)
data = (getDatalist())

for d in data["todos"]:
    print(d)



