from telethon import TelegramClient
import pytest
import requests
import allure
import asyncio
import pytest_asyncio


header = {"Authorization": "Basic dGVzdHVzZXI6dGVzdHBhc3M="}
urlChildrenList = "https://sandbox.1-gadget.com/api/v1/children/"
urlChildrenUpdate = "https://sandbox.1-gadget.com/api/v1/children/1/"
urlProfileCreate = "https://sandbox.1-gadget.com/api/v1/profiles/me/"
urlMainGoalList = "https://sandbox.1-gadget.com/api/v1/main-goals/"
urlMissionsList = "https://sandbox.1-gadget.com/api/v1/missions/"
urlTelegramGenerete = "https://sandbox.1-gadget.com/api/v1/telegram/generate-code/"
urlTelegramMe = "https://sandbox.1-gadget.com/api/v1/telegram/me/"
api_id = 16086290
api_hash = '1a497b918232ca670bbfa7d12fdee7da'
client = TelegramClient('anon', api_id, api_hash)

def mains(user,message):
    return client.send_message(user,message)
