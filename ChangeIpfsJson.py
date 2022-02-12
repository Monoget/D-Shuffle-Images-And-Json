import json

j=1

while j<=5:
    a_file = open("outputfiles/json/" + str(j) + ".json", "r")
    json_object = json.load(a_file)
    print(json_object)

    json_object["file_url"] = "ipfs://QmYS59gA8ZdBdC6ew9D2RwiwBGyLABRn4TJLzCUmacyoZV/" + str(j) + ".png"

    jsonFile = open("outputfiles/ipfs_json/" + str(j) + ".json", "w")
    jsonFile.write(json.dumps(json_object))

    print(json_object)
    jsonFile.close()

    j = j + 1