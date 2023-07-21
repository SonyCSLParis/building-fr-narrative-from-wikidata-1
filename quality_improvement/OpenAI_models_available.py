'''List the available OpenAI models'''
import openai

openai.api_key = "<YOUR OPENAI KEY HERE>"

model_list = openai.Model.list()['data']
model_ids = [x['id'] for x in model_list]
model_ids.sort()
print(model_ids)