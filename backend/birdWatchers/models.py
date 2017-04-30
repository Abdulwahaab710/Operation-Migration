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


