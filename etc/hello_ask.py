CONFIG = {
    'mode': 'django',
    'working_dir': '/home/box/web/ask', 
    'user': 'www-data', 
    'group': 'www-data',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=16',
        '--timeout=60',
        'ask.wsgi',
    ),
}