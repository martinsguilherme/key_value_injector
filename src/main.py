import controller.resource as resource
import os

if __name__ == '__main__':
    endpoint = resource.app
    #creates the uvicorn ASGI server
    os.system("uvicorn main:resource.app --reload")


