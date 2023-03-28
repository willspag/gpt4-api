from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import openai



# Make sure your OpenAI API Key is set as an environment variable
if os.environ.get('OPENAI_API_KEY') is None:
    raise Exception("OPENAI_API_KEY environment variable is not set")


app = Flask(__name__)
api = Api(app)

class GPT4API(Resource):
    def get(self):
        return "No GET Options Available", 401

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('prompt', type=str, required=True)
        args = parser.parse_args()

        print("\n\n\nPrompt Received! Calling OpenAI API...\n\n\n")

        message_list = [
             {"role": "system", "content": "You are a helpful AI Assistant."},
             {"role": "user", "content": str(args["prompt"])}
        ]

        if os.environ.get('MODEL') is None:
             model = "gpt-4"
        else:
            model = str(os.environ.get('MODEL'))

        if os.environ.get('MAX_TOKENS') is None:
            max_tokens = 1024
        else:
            max_tokens = int(os.environ.get('MAX_TOKENS'))
        
        if os.environ.get('TEMPERATURE') is None:
            temperature = 0.9
        else:
            temperature = float(os.environ.get('TEMPERATURE'))
        
        gpt_response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=message_list,
                        max_tokens=max_tokens,
                        n=1,
                        temperature=temperature
                    )
        
        print("\n\n\nOpenAI API Response Received! Parsing and returning to User...\n\n\n")

        # Parse response
        gpt_message = gpt_response["choices"][0]["message"]["content"]

        # Create return dictionary
        data = {
                "status_code": 200,
                "text": gpt_message
                }
        return data, 200
            
            

    def delete(self):
        return "No DELETE Options Available", 401

api.add_resource(GPT4API, '/gpt')

if __name__ == '__main__':

    app.run(
        debug=True,
        host=os.environ.get('PORT', '0.0.0.0'),
        port=int(os.environ.get('PORT', 8080))
    )

