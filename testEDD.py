# File:         JSON Mode Test File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

import Storage  as j

# assume no data exist or execute the next optional drop function
j.dropAll()

# test Databases CRUD
print(j.createDatabase('db1'))  # 0
print(j.createDatabase('db1'))  # 2
print(j.createDatabase('db4'))  # 0
print(j.createDatabase('db5'))  # 0
print(j.createDatabase(0))  # 1
print(j.alterDatabase('db5', 'db1'))  # 3
print(j.alterDatabase('db5', 'db2'))  # 0
print(j.dropDatabase('db4'))  # 0
print(j.showDatabases())  # ['db1','db2']

# test Tables CRUD
print(j.createTable('db1', 'tb4', 3))  # 0
print(j.createTable('db1', 'tb4', 3))  # 3
print(j.createTable('db1', 'tb1', 3))  # 0
print(j.createTable('db1', 'tb2', 3))  # 0

print(j.alterAddPK('db1', 'tb1', [0, 1]))  # 0
print(j.showTables('db1'))  # ['tb1', 'tb2']
# print(j.alterDropPK('db1','tb1'))       # 0
print(j.alterDropPK('db1', 'tb2'))  # 4
print(j.insert('db1', 'tb1', [1, 'A', 1]))  # 0
print(j.insert('db1', 'tb1', [2, 'B', 3]))  # 0
print(j.insert('db1', 'tb1', [3, 'C', 4]))  # 0
print(j.insert('db1', 'tb1', [4, 'D', 6]))  # 0
print(j.insert('db1', 'tb1', [5, 'E', 1]))  # 0
# print(j.insert('db1', 'tb1', [4, 'hola', 2, 5]))  # 5
# print(j.insert('db1', 'tb1', [3, 'hola', 1]))  # 4

# print(j.extractTable("db1", "tb1"))
# print(j.extractRow("db1","tb1",[1,"hola"]))
# print(j.extractRow("db1","tb1",[3,"hola"]))
# print(j.delete("db1","tb1",[1,'hola']))   #0
# print(j.extractTable("db1", "tb1"))
# print(j.update("db1","tb1",{1: 'probando update'}, ['2','hola'])) #0
# print(j.update("db1","tb1",{1: 'probando update', 0:'2'}, ['3','hola'])) #1
# print(j.extractTable("db1", "tb1"))         #[]
# print(j.loadCSV("./tb1.csv","db1","tb5"))
# print(j.extractTable("db1", "tb5"))         #[0,0,0,0,0]

print(j.extractRangeTable("db1", "tb1", 0, 1, 3))
# print(j.dropTable("db1","tb1"))