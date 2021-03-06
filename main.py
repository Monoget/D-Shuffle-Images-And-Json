import json
from random import choice
import shutil

save_number = []

j=1

while j<=4872:
    random_id=choice([i for i in range(1,4873) if i not in save_number])
    print("Serial: "+str(j), "Random: "+str(random_id))
    shutil.copy("files/images/ ("+str(j)+").png", "outputfiles/images/"+str(random_id)+".png")

    a_file = open("files/json/ ("+str(j)+").json", "r")
    json_object = json.load(a_file)
    print(json_object)

    json_object["name"] = "Phat Cubz #"+str(random_id)

    json_object["image"] = "ipfs://NewUriToReplace/"+str(random_id)+".png"

    json_object.update(
        {
            "symbol": "PC",
            "seller_fee_basis_points": 1000,
            "external_url": "",
            "edition": "" + str(random_id) + "",
            "properties": {
                "files": [
                    {
                        "uri": "" + str(random_id) + ".png",
                        "type": "image/png"
                    }
                ],
                "category": "image",
                "creators": [
                    {
                        "address": "Ha9dPpf4rDNAXsnQAi9qWWrKP5FKyPvV5buK6A4SiiD6",
                        "share": 100
                    }
                ]
            }
        }
    )

    ord_list = ['name', 'symbol', 'description', 'seller_fee_basis_points', 'image', 'external_url', 'edition',
                'attributes', 'properties']

    res = dict()
    for key in ord_list:
        res[key] = json_object[key]

    jsonFile = open("outputfiles/json/" + str(random_id) + ".json", "w")
    jsonFile.write(json.dumps(res, indent=4))

    print(json_object)

    jsonFile.close()
    save_number.append(random_id)
    j=j+1

