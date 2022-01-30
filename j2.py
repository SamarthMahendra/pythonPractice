import simplejson as json
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age


u=user("Mike",22)
def encodeuser(o):
    if isinstance(o,user):
        return {"name":o.name,"age":o.age,o.__class__.__name__:True}
    else:
        raise TypeError(" error")


ujson=json.dumps(u,indent=4,separators=(';','='), default=encodeuser)
print(ujson)
with open('u.json','w') as file:
    json.dumps(u,file,default=encodeuser)
with open('u.json','r') as file:
    uu=json.load(file)
    print(uu)

