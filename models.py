import peewee

database = peewee.SqliteDatabase("facebook_dump.db")

class Permalink(peewee.Model):
    slug = peewee.CharField()
    
    class Meta:
        database = database


if __name__ == "__main__":
    try:
        Permalink.create_table()
    except peewee.OperationalError:
        print "Permalink table already exists!"