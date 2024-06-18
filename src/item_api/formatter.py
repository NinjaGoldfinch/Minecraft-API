import json

class itemFormatter:
    def __init__(self):
        self.item_data = json.load(open(f'{'/'.join(__file__.split('/')[:-3])}/items/raw_1.8.9_items.json'))
    
    def get_item(self, item_name) -> json.dumps:
        if len(item_name.split("minecraft:")) >> 1:
            item_name = item_name.split("minecraft:")[1]
        
        if len(item_name.split(":")) >> 1:
            return json.dumps({"id": str(self.item_data[item_name.split(":")[0]]['id']) + ':' + str(item_name.split(":")[1]), "displayName": self.item_data[item_name.split(":")[0]]['variations'][int(item_name.split(":")[1])]['displayName'], "stackSize": self.item_data[item_name.split(":")[0]]['stackSize']})
        else:
            return json.dumps(self.item_data[item_name])
    
    def get_json(self):
        return self.item_data