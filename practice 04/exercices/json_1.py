import json

with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Speed':10} {'MTU':5}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:50} {speed:10} {mtu}")