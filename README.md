# pavilioncms-python

This is the Python Library for PavilionCMS

## Documentation
A comprehensive documentation of our API is available [here](https://docs.pavilioncms.com)


### Installation
You can install the library from Pypi using `pip` which is Python's Package manager

```sh
$ pip install pavilioncms-python
```

### Usage
Using the PavilionCMS python library is relatively easy after installation. 

In your python script, simple import the library and instantiate it with your read token. 

> You can find the Read Token on the Blog detail page. Each Readtoken is unique and is tied only to a singlular blog

```python
from pavilion_cms import PavilionCMS

client = PavilionCMS(read_token="your-read-token")
```

#### Functions

_*`tags`*_ => Get all your tags

The client's tags function has the `all`, `get`, `next` and `previous` methods for making requests. 

The `all` and `get` functions also accept an optional `params` argument to add additional data to the response. 

The `next` and `previous` functions accept only a url which is gotten from the response of the `all` method. 

> Reponses that request for a list are paginated. 

Example Usage
```python
response = client.tags.all()

tags = response["results"] 
# data results

count = response["count"]  
# Get all tags count (for pagination)

next_url = response["next"] 
# Get the url for the next page. Defaults to None if there's no data. You can pass this url into the `next` function

previous_url = response["previous"] 
# Get the url for the previous page. Defaults to None if there's no data. You can pass this url into the previous function

print(tags[0])
 #{
 #   'id': '0b4cff81-c655-452a-881f-3a8eeab7ed09', 
 #   'name': 'top table', 
 #   'detail_url': '/api/v1/tag/0b4cff81-c655-452a-881f-3a8eeab7ed09/view/'
 # }
 ```

 _*`categories`*_ => Get all your categories

 Same function call as tags. Has the `all`, `get`, `next` and `previous` calls. 

 Tags and Categories both share the same data structure



