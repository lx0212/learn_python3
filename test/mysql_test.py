from peewee import *

# database = MySQLDatabase('test',user='dashi',host='127.0.0.1',port=33306,password='XGcQwLPFMu')
database = MySQLDatabase("test", **{'host':'127.0.0.1', 'password':'XGcQwLPFMu', 'user':'dashi', 'port':33306})
# database = MySQLDatabase('database_name', user='www-data', charset='utf8mb4')

database.connect()

class MisUser2(Model):
    id = IntegerField()
    name = CharField()
    phone = CharField()
    role_id = IntegerField()
    organization_id = IntegerField()
    sign_url = CharField()
    create_time = DateTimeField()
    update_time = DateTimeField()
    status = IntegerField()
    deleted = IntegerField()
    class Meta:
        database = database
        table_name = "mis_user2"

MisUser2.create_table()

        
