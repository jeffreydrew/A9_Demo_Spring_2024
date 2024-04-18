#!/usr/bin/python3
import time
import httpx
import asyncio


class EdenAPI:
    # init
    def __init__(self, model="gpt-3.5-turbo-instruct"):
        self.api_key = "Bearer {api_key}"
        self.url = "https://api.edenai.run/v2/text/generation"
        self.provider = "openai"
        self.model = model
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.api_key,
        }

    async def ask(self, input):
        payload = {
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_original_response": False,
            "settings": {self.provider: self.model},
            "temperature": 0,
            "max_tokens": 250,
            "providers": self.provider,
            "text": input,
        }

        async with httpx.AsyncClient(http2=True) as client:
            response = await client.post(self.url, json=payload, headers=self.headers)
        reponse_text = response.json()[self.provider]["generated_text"]
        return reponse_text


if __name__ == "__main__":
    eden = EdenAPI()
    message = "explain the traces metrics and logs from the telemtry data exported by the jaeger tracer"

    print(asyncio.run(eden.ask(message)))
