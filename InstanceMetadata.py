#Name: Saumya 
#Challenge #2
#We need to write code that will query the meta data of an instance within AWS or Azure or GCPand provide a json formatted output. 
import requests
import json

def get_instance_details(key=None):
    metadata_url = "http://169.254.169.254/latest/meta-data/"
    if key:
        metadata_url += key

    try:
        response = requests.get(metadata_url)
        if response.status_code == 200:
            metadata = response.text
            return metadata if key else {"metadata": metadata}
        else:
            return {"error": "Couldnot fetch details"}

    except Exception as e:
        return {"error": str(e)}

input_key = "instance-id" 
output = get_instance_details(input_key)
print(output)
