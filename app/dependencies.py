# app/depedencies.py

import logging
from app.core.config import settings

def get_logger():
  # find a return a logger by name - for dependency injection
  return logging.getLogger(settings.LOG_NAME)