

TORTOISE = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "localhost",
                "port": "4406",
                "user": "root",
                "password": "123456",
                "database": "tortoise_orm"
            }
        }
    },
    'apps': {
        'models': {
            'models': ['aerich.models', 'fastAPI.user_service.models'],
            'default_connection': 'default'
        }
    }
}