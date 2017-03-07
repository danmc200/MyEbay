#!/usr/bin/python
import connection
fle = open("app_id.txt", 'r')
app_id = fle.readline()[:-1]
connect = connection.Connection(app_id)
connect.build()
connect.run()
