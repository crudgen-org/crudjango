import kopf
import kubernetes
import yaml
import json
from crudgen_django.services import SimpleRestService
import subprocess

@kopf.on.create('api.crudgen.org', 'v1', 'crud') 
def create_crud(body, spec, patch, **kwargs):
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    apiDescription = body['spec']['apiDescription']
    service = SimpleRestService.from_dict(json.loads(apiDescription))
    dest_path = f'/tmp/{namespace}/{name}/'
    docker_image = f'pooriazmn/{namespace}-{name}'
    service.transform(dest_path)

    process = subprocess.Popen(['docker', 'build', dest_path, '-t', docker_image],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("docker build failed")
        raise Exception("docker build failed")
    process = subprocess.Popen(['docker', 'push', docker_image],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("docker push failed")
        raise Exception("docker push failed")

    patch.status['imageReady'] = True
    patch.status['port'] = 8020
    patch.status['image'] = docker_image

@kopf.on.update('api.crudgen.org', 'v1', 'crud')
def update_crud(body, spec, **kwargs):
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    print(body)
    print(spec)
