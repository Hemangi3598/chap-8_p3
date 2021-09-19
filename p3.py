# wamdpp to keep a track on covid count in mumbai stns
# CRUD create, read, update, delete

cc = {}
while True:
	op = int(input("1 create, 2 read, 3 update, 4 delete and 5 exit "))
	if op == 1:
		stn_name = input("enter station name to be created ")
		if(cc.get(stn_name) is None):
			co = int(input("enter count "))
			cc[stn_name] = co
			print(stn_name, "created")
		else:
			print(stn_name, "already exists ")
	elif op == 2:
		print(cc)
	elif op == 3:
		stn_name = input("enter station name to be updated ")
		if(cc.get(stn_name) is None):
			print(stn_name, "does not exists ")
		else:
			co = int(input("enter new count "))
			cc[stn_name] = co
			print(stn_name, "updated")
	elif op == 4:
		stn_name = input("enter station name to be deleted ")
		if(cc.get(stn_name) is None):
			print(stn_name, "does not exists ")
		else:
			cc.pop(stn_name)
			print(stn_name, "deleted")
	elif op == 5:
		break
	else:
		print("invalid option")
