# Flask Challenge

Challenge!

## Quick Start

### Basics

1. Create and activate a virtualenv
1. Install the requirements

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Add Data

```sh
$ python seed.py
```

### Run the Application

```sh
$ python manage.py runserver
```

### Endpoints

| Endpoint             | Method | Payload                   | Action          |
|----------------------|--------|---------------------------|-----------------|
| /api/v1/stats        | GET    | n/a                       | GET all stats   |
| /api/v1/stats/<uuid> | GET    | n/a                       | GET single stat |
| /api/v1/stats        | POST   | project/tests/sample.json | Add data        |

### Test

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
