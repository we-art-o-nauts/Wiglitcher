import json

from dotenv import load_dotenv
from os import environ

load_dotenv()

# Read JSON file
with open('workflow_api_FINAL_IMAGE.json', 'r') as jsonfile:
    jsondata = jsonfile.read()

input = {
    "workflow_json": jsondata,
    "output_quality": 80
}

from replicate.client import Client

replicate = Client(
  api_token=environ.get("REPLICATE_API_TOKEN")
)

output = replicate.run(
    "fofr/any-comfyui-workflow:1d8cbf1c51cf25533ded23aae406aeb228fd8597326bc15952ba6b4b92fd12be",
    input=input
)
print(output)
