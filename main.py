# -*- coding: utf-8 -*-

from configparser import ConfigParser

from langchain.llms import OpenAI


config = ConfigParser()
config.read(".env")


OPEN_AI_KEY = config["secrets"].get("OPEN_AI_KEY", "")


llm = OpenAI(model="text-davinci-003", openai_api_key=OPEN_AI_KEY)


prompt = "Con chi confina l'Italia?"

resp = llm.predict(prompt)

print(resp)
