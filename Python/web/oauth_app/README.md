# auth_app

### Install

```bash
 $ pip install .
```

### Configuring the Database

```bash
 $ flask --app flaskr shell
>>> from flaskr.models import db
>>> db.create_all()
```

### Run the Project

```bash
 $ flask --app flaskr run --cert=adhoc
```
