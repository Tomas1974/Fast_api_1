import requests




print(requests.post("http://127.0.0.1:8000/todo",
                    json = {"id" : 1,
                            "item": "test1",
                            "status": "God"
                    }                  
                    ).json())


print(requests.get("http://127.0.0.1:8000/todo").json())

