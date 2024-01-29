import os

DEBUG_MODE: bool = os.getenv('DEBUG_MODE', False)
DATABASE_HOST: str = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT: str = os.getenv('DATABASE_PORT', '3306')
DATABASE_USER: str = os.getenv('DATABASE_USER')
DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
DATABASE_ENDPOINT: str = f'mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}'
DATABASE_NAME: str = os.getenv('DATABASE_NAME', 'libz')
DATABASE_URL: str = f'{DATABASE_ENDPOINT}/{DATABASE_NAME}'
