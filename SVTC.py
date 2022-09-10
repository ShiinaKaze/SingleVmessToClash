import base64
import sys
import yaml

vmessLink = sys.argv[1]
# print(vmessLink[8:])
decodeVmessLink = base64.b64decode(vmessLink[8:])
decodeVmessLink = str(decodeVmessLink)
decodeVmessLink = eval(decodeVmessLink[2:len(decodeVmessLink)-1])
# print(decodeVmessLink,type(decodeVmessLink))


with open("template.yaml", encoding="utf-8") as file:
    file_data = file.read()

yamlObject = yaml.load(file_data, yaml.FullLoader)
print("before----------------------------------------")
print(yamlObject["proxies"][0])

proxies = yamlObject["proxies"][0]
proxies["server"] = decodeVmessLink["add"]
proxies["uuid"] = decodeVmessLink["id"]
proxies["ws-opts"]["path"] = decodeVmessLink["path"]
print("after----------------------------------------")
print(proxies)
yamlObject["proxies"][0] = proxies

with open("SVTC.yaml", "w", encoding="utf-8") as file:
    yaml.dump(yamlObject, file, encoding="utf-8")
print("Success!")