# gpt4-api


This is a nasic flask_restful api to receive text, call GPT4 on it, and return the response to the response to simplify setting up the OpenAI API call/parse response for easier usage with iPhone shortcuts. Dockerfile is included for easy deployment to Google Cloud Run.


The goal is to create an iPhone shortcut that allows you to easily ask GPT4 questions through Siri. However, setting up the args/POST request and parsing the full response dict directly in iPhone shortcuts was causing errors since extracting the response text requires both dictionary and array indexing which the iPhone shortcut app wouldn't let me do. To solve this, I just built a simple Rest API that simplifies everything by just taking in a simple text input and returning the GPT4 response text as a single argument that can be easily retrieved through iPhone Shortcuts.

