import json
from random import choice
import shutil

save_number = []

j=1

while j<=5:
    random_id=choice([i for i in range(1,6) if i not in save_number])
    print("Serial: "+str(j), "Random: "+str(random_id))
    shutil.copy("files/images/ ("+str(j)+").png", "outputfiles/images/"+str(random_id)+".png")

    a_file = open("files/json/ ("+str(j)+").json", "r")
    json_object = json.load(a_file)
    print(json_object)

    json_object["name"] = "Whanki #"+str(random_id)

    json_object["file_url"] = "ipfs://NewUriToReplace/"+str(random_id)+".png"

    json_object["custom_fields"]["edition"] = random_id

    jsonFile = open("outputfiles/json/"+str(random_id)+".json", "w")
    jsonFile.write(json.dumps(json_object))

    print(json_object)

    jsonFile.close()
    save_number.append(random_id)
    j=j+1

