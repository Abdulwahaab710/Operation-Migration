## Stack used
- Flask
- Tensorflow
- android studio
- google maps

## Database Migration

To migrate the database run the following commands in table

| Command | Description |
| ------- | ----------- |
| `python3 db.py db init` | Generate a migration |
| `python3 db.py db migrate` | Migrate db |
| `python3 db.py db upgrade` | Upgrade |

## API
| Method |	path |	parameters |	route description |
| ------ | ----- | ----------- | ---------------- |
| POST | http://mz7xlyzuh2ua67.speedy.cloud/search | gps, image, timestamp | This route add a spotted bird to database |
| GET | http://mz7xlyzuh2ua67.speedy.cloud/get-bird | bird-name | This route fetches migration data |
