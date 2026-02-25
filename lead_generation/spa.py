import requests

INBOUND_URL = "https://test.vortexwebre.com/rest/1/qh06bncey8lvvz3u/"
SPA_TYPE_ID = 1042 

def mirror_lead_to_spa():
    # Example data to generate
    for i in range(1, 6):
        test_name = f"Client Alpha {i}"
        test_phone = f"+91987654321{i}"
        
        lead_payload = {
            "fields": {
                "TITLE": f"New Lead: {test_name}",
                "NAME": test_name,
                "PHONE": [{"VALUE": test_phone, "VALUE_TYPE": "WORK"}]
            }
        }
        lead_response = requests.post(f"{INBOUND_URL}crm.lead.add", json=lead_payload).json()
        lead_id = lead_response.get("result")

        if not lead_id:
            print(f"Failed to create lead {i}: {lead_response}")
            continue

        spa_payload = {
            "entityTypeId": SPA_TYPE_ID,
            "fields": {
                "TITLE": f"SPA Record for Lead {lead_id}",
                "UF_CRM_5_NAME": test_name,
                "UF_CRM_5_PHONE": test_phone, 
                "parentId2": lead_id 
            }
        }
        
        spa_response = requests.post(f"{INBOUND_URL}crm.item.add", json=spa_payload).json()
        
        if "result" in spa_response:
            spa_item_id = spa_response['result']['item']['id']
            print(f"Success: Lead {lead_id} mirrored to SPA Item {spa_item_id}")
        else:
            print(f"SPA Error: {spa_response.get('error_description')}")

if __name__ == "__main__":
    mirror_lead_to_spa()