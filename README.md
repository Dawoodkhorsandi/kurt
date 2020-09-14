# kurt
Yet another Django URL shortener API

## Features
- Uses the model id,  and encode it to an arbitrary base 57(all numbers, lowercase and uppercase letter except for 0,O,1,I,l) as shorted url
- Swagger and reDoc Documentaion are available

## End points
### Get all shorted URL 
```
    GET /api/v1
```
#### result:
```javascript

  {
    "id": 1,
    "detail_url": "http://domain/api/v1/1/",
    "long_url": "https:google.com/some-extra-parameters",
    "short_url": "http://domain/3/",
    "times_viewed": 1
  },
  ....
  {
    "id": 4,
    "detail_url": "http://domain/api/v1/4/",
    "long_url": "https://mail.google.com/mail/ca/u/0/#inbox",
    "short_url": "http://domain/6/",
    "times_viewed": 0
  }

```

### Create a new shorted URL
```
    POST /api/v1
```
#### parameters
 ` {"long_url" : "an url"}`
  
#### result
` response code 201  and returns URL instance and its details`

### A specific URL detail page
```
GET /v1/{id}/
```

#### parameters
 ` {"id" : "an integer, unique ID"}`

#### result
```javascript
  {
    "id": 4,
    "detail_url": "http://domain/api/v1/4/",
    "long_url": "https://mail.google.com/mail/ca/u/0/#inbox",
    "short_url": "http://domain/6/",
    "times_viewed": 0
  }
```

### Delete a specific URL instance
```
DELETE /v1/{id}/
```
#### parameters
 ` {"id" : "an integer, unique ID"}`

  
#### result
` response code 240, meaning instance has been deleted.`




## Todo
- [X] Write test
- [X] Auto custom short URL option
- [X] compelete README.md

