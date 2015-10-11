import peewee

database = peewee.SqliteDatabase("facebook_dump.db")

class Permalink(peewee.Model):
    slug = peewee.CharField()
    
    class Meta:
        database = database

class Potato(peewee.Model):
	slug = peewee.CharField()
	traveler = peewee.CharField()
	traveler_slug = peewee.CharField()
	question = peewee.TextField()
	timestamp = peewee.CharField()

class Comment(peewee.Model):
	potato = peewee.ForeignKeyField(Potato, related_name='comments')
	helper = peewee.CharField()
	helper_slug = peewee.CharField()
	power = peewee.IntegerField()
	timestamp = peewee.CharField()
	answer = peewee.TextField()


if __name__ == "__main__":
    try:
        # Permalink.create_table()
        Potato.create_table()
        Comment.create_table()
    except peewee.OperationalError:
        print "Permalink table already exists!"