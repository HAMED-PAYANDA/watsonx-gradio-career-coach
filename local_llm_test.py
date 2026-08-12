from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters

# Set up the API key and project ID for IBM Watson 
watsonx_API = "PASTE_YOUR_API_KEY_HERE" 
project_id = "PASTE_YOUR_PROJECT_ID_HERE" 

# Generation parameters
params = TextChatParameters(
    temperature=0.7,
    max_tokens=1024
)

model = ModelInference(
    model_id='meta-llama/llama-4-maverick-17b-128e-instruct-fp8', 
    params=params,
    credentials={
        "apikey": watsonx_API,
        "url": "https://us-south.ml.cloud.ibm.com"
    },
    project_id=project_id
    )

q = "How to be happy?"
messages = [
		{
			"role": "user",
			"content": [
				{
					"type": "text",
					"text": q
				},
			]
		}
	]

generated_response = model.chat(messages=messages)
print(generated_response['choices'][0]['message']['content'])

