import json
from random import choice
import shutil


j=1

while j<=4872:
    shutil.copy("outputfiles/images/" + str(j) + ".png", "output/images/" + str(j-1) + ".png")
    a_file = open("outputfiles/json/" + str(j) + ".json", "r")
    json_object = json.load(a_file)
    print(json_object)

    json_object["name"] = "Phat Cubz #" + str(j-1)

    json_object["image"] = "ipfs://NewUriToReplace/" + str(j-1) + ".png"

    json_object.update(
        {
            "symbol": "PC",
            "seller_fee_basis_points": 1000,
            "external_url": "",
            "edition": "" + str(j-1) + "",
            "properties": {
                "files": [
                    {
                        "uri": "" + str(j-1) + ".png",
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

    jsonFile = open("output/json/" + str(j-1) + ".json", "w")
    jsonFile.write(json.dumps(res, indent=4))

    print(json_object)

    jsonFile.close()
    j = j + 1