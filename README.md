# Key value injector

Injects a pair of key and value to a header of an HTTP request. 

Currently, GET and POST are implemented

GET endpoint returns a response header composed by sequential key and random value.

POST endpoint injects key and value sent in the payload (body) to the response header.

# Project Structure

All source codes are located inside "src" directory.

The project is structured in directories, using the MVC model as the basis. 

The controller directory contains the logic of REST endpoints.

The model directory contains the definition for the injector object (resource for GET endpoint) and request object (resource for POST endpoint).

The test directory contains the unit tests, designed using the unittest framework.


## REST Endpoints

Endpoints have been implemented for the basic operations of the REST model. These endpoints and a brief summary of what they do is below:

```
get key_value - Returns key_value header composed of sequential key and random value
post key_value - Returns key_value header composed of key and value taken from the request body
```


### Prerequisites

```
requests 
fastapi 
pydantic
```



## Usage

The application works as a restful server, listening by default on port 8000. Possible requests are indicated above (REST endpoints).

GET sequential key and random value

```
curl -L -X GET 'http://localhost:8000/key_value'
```
Sends key and value via POST request
```
curl -L -X POST 'http://localhost:8000/key_value' \
-H 'Content-Type: application/json' \
--data '{
  "key": "dummy key",
  "value": "dummy value"
}'
```


## Running the tests

To run all unit tests use the command:

```
python -m unittest discover -s test -t src
```

To run injector model tests use the command:

```
python -m unittest src/test/test_injector.py 
```

To run request model tests use the command:

```
python -m unittest src/test/test_request.py
```

To run controller (endpoints) tests use the command:

```
python -m unittest src/test/test_resource.py
```

## Built With

* Python 3.6 - Language and version
* [fastapi](https://fastapi.tiangolo.com/) - The web framework used

## Authors

* **Guilherme Martins** - *Initial work* - [martinsguilherme](https://github.com/martinsguilherme)

## License

This project is licensed under the MIT License
