import json

data = {
	"income": {
		"salary": 50000,
		"bonus": 20000
	}
}
"""сериализация с записью в файл"""
with open("my_file.json", "w") as write_f:
    json.dump(data, write_f)

"""сериализация без записи"""
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

"""десериализация из файла"""
with open("my_file.json") as read_f:
	data = json.load(read_f)

print(data)
print(type(data))

"""десериализация из строки"""
json_str = """{"income": {"salary": 50000, "bonus": 20000}}"""
data = json.loads(json_str)

print(data)
print(type(data))

