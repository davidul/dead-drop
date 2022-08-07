# Dead drop
Sample project written in Flask. 

You can store text as encrypted payload in Sqllite database
and retrieve it via a URL and password or REST call.

Password isn't stored anywhere, once lost, data are lost.

SQLLite isn't protected by authentication, it is just a file.
You can only protect it on the filesystem privileges.

## Init-db
Create db file

```shell
export FLASK_APP=dd-app
flask init-db
```

Run the app

```shell
flask run
```

Running the app with unicorn use the
`run.sh` shell script

## REST API

Insert data into db

|Method| Endpoint            |
|------|---------------------|
|POST  | /dropme             |
| GET | /retrieve/{path_id} |

Example:

Request
```shell
curl --location --request POST 'http://127.0.0.1:5000/drop/dropme' \
--header 'Content-Type: application/json' \
--data-raw '{"data": "Hello"}'
```

Response
```json
{
    "path": "d5403407214540ceba92b2cf2bb498b6",
    "success": true
}
```

Use the returned `path` to retrieve the data.
Request example:

```shell
curl --location --request GET 'http://127.0.0.1:5000/drop/retrieve/d5403407214540ceba92b2cf2bb498b6'
```

Returned decrypted data

```json
{
    "data": "Hello",
    "success": true
}
```

## Docker

First build the image

```shell
docker build -t dead-drop .
```

Run in docker

```shell
docker run -p 9090:8080 dead-drop
```

