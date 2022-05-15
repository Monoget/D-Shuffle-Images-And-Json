from xlrd import open_workbook
import json
from random import choice
import shutil

wb = open_workbook('data/new.xls')
# print 'Sheet:',s.name
values = []
for s in wb.sheets():
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value = (s.cell(row, col).value)
            try:
                value = str(int(value))
            except:
                pass
            col_value.append(value)
        values.append(col_value)

print(values)

j = 1
save_number = []

while j <= 16:
    random_id = choice([i for i in range(1, 4873) if i not in save_number])
    shutil.copy("data/images/" + str(j) + ".png", "data/oimages/" + str(random_id) + ".png")
    a_file = open("data/json/" + str(j) + ".json", "r")
    json_object = json.load(a_file)
    print(json_object)

    json_object["name"] = "Phat Cubz #" + str(random_id)

    json_object["image"] = "ipfs://NewUriToReplace/" + str(random_id) + ".png"

    json_object.update(
        {
            "attributes": [
                {
                    "trait_type": "Name",
                    "value": "" + str(values[j][0]) + ""
                },
                {
                    "trait_type": "Background",
                    "value": "" + str(values[j][1]) + ""
                },
                {
                    "trait_type": "Back",
                    "value": "" + str(values[j][2]) + ""
                },
                {
                    "trait_type": "Skin",
                    "value": "" + str(values[j][3]) + ""
                },
                {
                    "trait_type": "Clothes",
                    "value": "" + str(values[j][4]) + ""
                },
                {
                    "trait_type": "Eyes",
                    "value": "" + str(values[j][5]) + ""
                },
                {
                    "trait_type": "Eyewear",
                    "value": "" + str(values[j][6]) + ""
                },
                {
                    "trait_type": "Neck",
                    "value": "" + str(values[j][7]) + ""
                },
                {
                    "trait_type": "Head",
                    "value": "" + str(values[j][8]) + ""
                },
                {
                    "trait_type": "Mouth",
                    "value": "" + str(values[j][9]) + ""
                },
                {
                    "trait_type": "Accessories",
                    "value": "" + str(values[j][10]) + ""
                }
            ]
        }
    )

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

    jsonFile = open("data/ojson/" + str(random_id) + ".json", "w")
    jsonFile.write(json.dumps(res, indent=4))

    print(json_object)

    jsonFile.close()
    j = j + 1
