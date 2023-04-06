from peewee import SqliteDatabase, Model, CharField, IntegerField, DateTimeField, FloatField, BigIntegerField, TextField, DateField, TimestampField
from datetime import datetime
from pandas import DataFrame

db = SqliteDatabase('tractor2.db')



class project(Model):
    tag = CharField(null=True)
    number = CharField(null=True)
    name = CharField(null=True)
    info = CharField(null=True)
    updated = CharField(null=True)

    class Meta:
        database = db
        table_name = 'project'

class schedule(Model):
    project = CharField(null=True)
    milestone = CharField(null=True)
    wbs = CharField(null=True)
    task = CharField(null=True)
    outline = CharField(null=True)
    resource = CharField(null=True)
    start = CharField(null=True)
    finish = CharField(null=True)
    complete = IntegerField(null=True)
    weight = IntegerField(null=True)
    updated = CharField(null=True)

    class Meta:
        database = db
        table_name = 'schedule'

class issue(Model):
    project = CharField(null=True)
    level = CharField(null=True)
    status = CharField(null=True)
    name = CharField(null=True)
    wbs = CharField(null=True)
    action = CharField(null=True)
    tracker = CharField(null=True)
    due = CharField(null=True)
    journal = CharField(null=True)
    updated = CharField(null=True)

    class Meta:
        database = db
        table_name = 'issue'

class timesheet(Model):
    project = CharField(null=True)
    name = CharField(null=True)
    wbs = CharField(null=True)
    journal = CharField(null=True)
    workhour = IntegerField(null=True)
    date = CharField(null=True)
    updated = CharField(null=True)

    class Meta:
        database = db
        table_name = 'timesheet'


class finance(Model):
    project = CharField(null=True)
    date = CharField(null=True)
    label = CharField(null=True)
    amount = IntegerField(null=True)
    wbs = CharField(null=True)
    comment = CharField(null=True)
    updated = CharField(null=True)

    class Meta:
        database = db
        table_name = 'finance'

db.create_tables([project])
db.create_tables([schedule])
db.create_tables([issue])
db.create_tables([timesheet])
db.create_tables([finance])
# db.create_tables([cost])

def submit(table, data):
    return table.insert_many(data).execute()


def display(table, project_name):
    return list(table.select().where(table.project == project_name).dicts())

def clear(table, project_name):
    return table.delete().where(table.project == project_name).execute()

