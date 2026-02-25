import requests
from generate import *

INBOUND_URL = "https://test.vortexwebre.com/rest/1/qh06bncey8lvvz3u/"

"""
INBOUND_URL = "https://test.vortexwebre.com/rest/1/qh06bncey8lvvz3u/"
methods = "crm.lead.add"
"""

def bitrix_cmd(method, payload):
    return requests.post(
        f"{INBOUND_URL}{method}",
        json=payload
    ).json().get("result", [])

def generate_lead():
    for i in range(1, 101):
        title = generate_title()
        name = generate_name()
        phone = generate_phone()

        payload = {
            "fields": {
                "TITLE": title,
                "NAME": name,
                "PHONE": [{"VALUE": generate_phone(), "VALUE_TYPE": "WORK"}],
            },
            "params": {"REGISTER_SONET_EVENT": "Y"}
        }
        lead_response = bitrix_cmd(method="crm.lead.add", payload=payload)
        print(f"{i}. {title} has been added to lead")

        spa_payload = {
            "entityTypeId": 1042,
            "fields": {
                "TITLE": f"SPA Record for Lead {lead_response}",
                "ufCrm5Name": name,
                "ufCrm5Phone": phone, 
                "parentId2": lead_response
            }
        }
        spa_response = bitrix_cmd(method="crm.item.add", payload=spa_payload)
        print("Lead added to the SPA")


if __name__ == "__main__":
    generate_lead()
    print("All the leads has been added to the crm")