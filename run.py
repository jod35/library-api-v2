from api import create_app
from api.config import app_config
from decouple import config

app=create_app(config('DEVELOPMENT'))


if __name__ == "__main__":
    create_app(config('DEVELOPMENT'))    
