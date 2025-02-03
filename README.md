# fastapi_starter
FastAPI backend starter code

## Directory Structure
Note: __init__.py is included in each subdirectory, but not shown for the clarity of structure.

```
.
├── README.md
├── requirements.txt
├── .env                  # Environment vaiables
├── [.env.example]        # Environment template
├── tests                 # All test files
│   ├── root.http         # root endpoint http test client 
│   ├── [conftest.py]
│   ├── [unit]
│   └── [integration]
└── app
    ├── core              # For core application settins/config
    │   ├── config.py     # Pydantic settings
    │   └── ...
    ├── [data]              # Any local data (JSON, fixtures, etc.)
    │   ├── app.json      # app data
    │   └── sample.json   # sample data     
    ├── [db]
    │   ├── session.py    # Database connection
    │   └── migrations    # Alembic directory
    ├── dependencies.py   # FastAPI common deps
    ├── [middleware]      # For classes and functions that handle request/response transformations or othe“middleware-ish” logic.
    │   ├── logging.py    # Request logging
    │   └── security.py   # Security headers
    ├── [models]            # Database ORM models
    ├── [schemas]           # Pydantic models
    ├── routers           # For fast API route definitions
    │   └── root.py
    ├── [services]          # Business logic
    ├── [static]
    ├── utils             # Helper functions
    │   ├── api_key.py    # api key helper
    │   └── logger_helper.py   # helper file for logging    
    └── main.py           # App initialization
```