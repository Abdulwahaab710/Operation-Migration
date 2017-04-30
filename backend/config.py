import dotenv
DOTENV_PATH = join(dirname(__file__), '.env')
USERNAME = dotenv.get('USERNAME')
PASSWORD = dotenv.get('PASSWORD')
DATABASE = 'birdWatchers'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost/{}'.formt(
    USERNAME,
    PASSWORD,
    DATABASE
)
