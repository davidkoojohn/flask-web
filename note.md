
## SQLAIchemy

```
pip install flask-sqlalchemy

# 数据库之间的连接器
# mysql
pip install PyMySql
...

>>> db.create_all()
>>> db.drop_all()
>>> admin_role = Role(name='Admin')
>>> db.session.add(admin_role)
>>> db.session.add_all([admin_role, ..., user_john, user_david])
>>> db.session.commit()

# update
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> db.session.commit()

# delete
>>> db.session.delete(mod_role)
>>> db.session.commit()

# query
>>> Role.query.all()
>>> User.query.filter_by(role=user_role).all()
>>> user_role = Role.query.filter_by(name='User').first()
```

## SQLAIchemy URL

```
#mysql
mysql+pymysql://user:password@ip:port/db_name
```

## Flask-Migrate

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```





