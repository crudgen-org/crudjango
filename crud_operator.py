import kopf
import kubernetes
import yaml

@kopf.on.create('api.crudgen.org', 'v1', 'crud') 
def create_crud(body, spec, **kwargs): 
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    print(body)
    print(spec)

@kopf.on.update('api.crudgen.org', 'v1', 'crud')
def update_crud(body, spec, **kwargs):
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    print(body)
    print(spec)
