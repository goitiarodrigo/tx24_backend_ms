# tx24_backend_ms

## Para correr este servicio pueden correrlo directamente con docker ejecutando:
```javascript
docker build -t tx24_backend .
```
Y luego:
```javascript
docker run -d --env-file .env -p 3000:3000 --name tx24_backend tx24_backend
```
