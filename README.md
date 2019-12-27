# Smart aquarium
水槽の水温、水質を管理するアプリケーション

## Features
- Backend
    - Python3.x
    - Flask
- Frontend
    - node (v12.13.1)
    - npm (v6.12.1)
    - TypeScript(v3.5.3)
    - SCSS(v4.12.0)
    - Vuejs (cli v4.0.5)
    - Buefy
    - Bulma

## Build database
``` sh
cd /path/to/smart-aquarium
export FLASK_APP=./manage.py
flask run create-db
```

## Development
### Start up local server
### Frontend
``` sh
cd /path/to/smart-aquarium/frontend
npm run serve
```

### Backend
``` sh
cd /path/to/smart-aquarium
python3 -B dev.py
```
