# fastapi_starter
FastAPI backend starter code

## Original Directory Structure
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py
│   ├── data
│   │   ├── data.json
│   │   └── test.json
│   ├── logger.py
│   ├── main.py
│   ├── middleware
│   │   ├── TaskHandler.py
│   │   ├── MyService.py
│   │   ├── __init__.py
│   │   └── logger_helper.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── task.py
│   │   └── service.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── api_1.py
│   │   └── api_2.py
│   └── test
│       ├── __init__.py
│       └── test.http
└── requirements.txt
```

## Directory Structure recomended
```
.
├── README.md
├── requirements.txt
├── .env.example          # Environment template
├── tests                 # All test files
│   ├── conftest.py
│   ├── unit
│   └── integration
└── app
    ├── __init__.py
    ├── core
    │   ├── config.py     # Pydantic settings
    │   └── logger.py     # Logging configuration
    ├── db
    │   ├── session.py    # Database connection
    │   └── migrations    # Alembic directory
    ├── dependencies.py   # FastAPI common deps
    ├── middleware
    │   ├── logging.py    # Request logging
    │   └── security.py   # Security headers
    ├── models            # ORM models
    ├── schemas           # Pydantic models
    ├── routers
    │   ├── items.py
    │   └── users.py
    ├── services          # Business logic
    ├── static
    ├── utils             # Helper functions
    └── main.py           # App initialization
```

## Another suggested directory structure
```
.
├── README.md
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── alembic/
│   └── migrations/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py      # New
│   │   └── database.py      # SQLModel setup
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py
│   │   └── service.py
│   ├── schemas/             # New (Pydantic models)
│   │   └── ...
│   ├── api/                 # Rename "routers" to "api"
│   │   ├── v1/             # Versioning
│   │   │   ├── endpoints/
│   │   │   └── router.py
│   │   └── dependencies.py # Auth dependencies
│   ├── services/            # New (business logic)
│   │   └── ...
│   ├── utils/               # New (replaces logger.py)
│   │   ├── logging.py
│   │   └── ...
│   ├── tests/               # Move tests here
│   │   ├── conftest.py
│   │   ├── test_api.py
│   │   └── ...
└── └── middleware/
    │   └── ...

```

## Final Directory Structure
Note: __init__.py is included in each subdirectory, but now shown for clarity of directory structure.
```
.
├── README.md
├── requirements.txt
├── .env.example          # Environment template
├── tests                 # All test files
│   ├── conftest.py
│   ├── unit
│   └── integration
└── app
    ├── core              # For core application settins/config
    │   ├── config.py     # Pydantic settings
    │   └── logger.py     # Logging configuration
    ├── data or any local data (JSON, fixtures, etc.)
    │   ├── app.json      # app data
    │   └── sample.json   # sample data     
    ├── db
    │   ├── session.py    # Database connection
    │   └── migrations    # Alembic directory
    ├── dependencies.py   # FastAPI common deps
    ├── middleware For classes and functions that handle request/response transformations or othe“middleware-ish” logic.
    │   ├── logging.py    # Request logging
    │   └── security.py   # Security headers
    ├── models            # Database ORM models
    ├── schemas           # Pydantic models
    ├── routers           # For fast API route definitions
    │   ├── items.py
    │   └── users.py
    ├── services          # Business logic
    ├── static
    ├── utils             # Helper functions
    ├── logger.py         # Logger init
    └── main.py           # App initialization
```