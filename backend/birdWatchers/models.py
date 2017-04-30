from birdWatchers import db
class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bird_name = db.Column(db.String(255))
    spotted_bird = db.db.relationship(
        'Bird',
        backref='spotted_bird',
        lazy='dynamic'
    )
    def __init__(self, bird_name):
        self.bird_name = bird_name

class SpottedBird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gps_lat = db.Column(db.string(db.Float))
    gps_long = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    bird_id = db.Column(
        db.Integer,
        db.ForeignKey('bird.id')
    )
    def __init__(self, gps_lat, gps_long, timestamp, bird_id):
        self.gps_lat = gps_lat
        self.gps_long = gps_long
        self.timestamp = timestamp
        self.bird_id = bird_id
