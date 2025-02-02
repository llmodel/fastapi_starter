# app/main.py

##### To start the FastAPI app
#####   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

import logging
from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.utils.logger_helper import StatusCodeLoggerMiddleware,configure_fastapi_logging, setup_logger
from app.core.config import settings
from app.routers import root


#####  STARTUP / SHUTDOWN EVENTS  #####
@asynccontextmanager
async def lifespan(app: FastAPI):
    ##### STARTUP ACTIONS #####
    logger.info('asynccontexmanager - app startup')
    yield

    ##### SHUTDOWN ACTIONS #####
    logger.info("Application shutdown")
    ## TODO You might want to add code here to gracefully shut down the watcher process

#####  MAIN SECTION  #####
app = FastAPI(lifespan=lifespan)

# Setup shared logger
logger = setup_logger(
    name=settings.LOG_NAME,
    log_file=settings.LOG_FILE,
    log_level=logging.INFO
)

# Configure FastAPI and Uvicorn logging in the logging middleware
configure_fastapi_logging(logger=logger)

# Add middleware for request/response logging
app.add_middleware(
    StatusCodeLoggerMiddleware, 
    logger=logger
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(root.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
