# Dead drop
Sample project written in Flask. 

You can store text as encrypted payload in in-memory database
and retrieve it via a URL and password or REST call.

Password isn't stored anywhere, once lost, data are lost.

## Init-db
Create in memory db

```shell
export FLASK_APP=dd-app
flask init-db
```