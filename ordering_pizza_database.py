import mysql.connector
from flask import Flask,request
import MysqlConnect as connect
import GenerateResponse as res
import Error as err

app = Flask(__name__)

@app.route('/Index')
def index():
    return render_template('index.html')

def SelectQuery():
	selectquery = ('SELECT * from orderPizza')
	return selectquery

def printData(data):
	for i in data:
		print(i)

@app.route('/DisplayDatas',methods = ['GET']) 
def display():
	conn = connect.ConnectMySql()
	print(f'Connection status : {conn}')
	if(conn is False):
		return err.ReturnConnectionError()
	else:
		try:
			cur = conn.cursor()
			print(f'Cursor object : {cur}')
			query = ('SELECT* from orderPizza') 
			cur.execute(query)
			msg="Data fetched succesfully"
			return res.generateResponse(cur,msg)	
		except Exception as e:
			print(e)
			return err.ReturnFetchError()
		finally:
			conn.close()

@app.route('/fetch',methods = ['GET', 'POST']) 
def fetch():

	body_data = request.json
	print(body_data)
	try:
		status = body_data['status']
		print(status)
		if status == "" or status is None:
			return err.ReturnValueError()
		conn = connect.ConnectMySql()
		print(f'Connection status : {conn.is_connected()}')
		if(conn is False):
			return ReturnConnectionError()
		else:
			cur = conn.cursor()
			print(f'Cursor object : {cur}')
			query = (f'SELECT * from orderPizza where status="{status}"')
			cur.execute(query)	
			msg = "Fetched data succesfully"
			result = res.generateResponse(cur,msg)
			conn.close()
			return result
	
	except KeyError as e:
		return err.ReturnKeyError()
	except Exception as e:
		print(e)
		return err.ReturnFetchError()
	



@app.route('/insert',methods=['GET', 'POST'])
def insert():

	body_data = request.json
	print(body_data)
	try:
		pizza_type = body_data['pizza']
		print(pizza_type)
		pizza_size = body_data['size']
		print(pizza_size)
		pizza_count = body_data["count"]
		print(pizza_count)
		user_name = body_data['name']
		print(user_name)
		mobile_number = body_data['number']
		print(mobile_number)
		address = body_data['address']
		print(address)
		status = body_data['status']
		print(status)
		if (pizza == "" or pizza is None or size == "" or size is None or count == "" or count is None or price == "" or price is None or name == "" or name is None or number == "" or number is None or address =="" or address is None):
			return err.ReturnValueError()
		conn = connect.ConnectMySql()
		print(f'Connection status : {conn.is_connected()}')
		if(conn is False):
			return err.ReturnConnectionError()
		else:
			cur1 = conn.cursor()
			print(f'Cursor object : {cur1}') 
			query = (f'INSERT INTO orderPizza(pizza_type,pizza_size,pizza_count,user_name,mobile_number,address,status)values("{pizza}","{size}",{count}","{name}","{number}","{address}","{status}")')	
			cur1.execute(query)
			cur2 = conn.cursor()
			selectquery = SelectQuery()
			cur2.execute(selectquery)
			msg = "Data inserted succesfully"
			result = res.generateResponse(cur2,msg)
			conn.close()
			return result
	except KeyError as e:
		return err.ReturnKeyError()		
	except  mysql.connector.IntegrityError as e:
		print(f'Exception : {e}')
		return err.ReturnDuplicateDataError()					


@app.route('/Delete',methods = ['get', 'post'])
def delete():
	body_data = request.json
	print(body_data)
	try:
		pizza_type = body_data['pizza']
		print(pizza)

		if pizza_type == "" or pizza_type is None :
			return err.ReturnValueError()	
		conn = connect.ConnectMySql()
		print(f'Connection status : {conn.is_connected()}')
		if(conn is False):
		   return err.ReturnConnectionError()
		else:
			cur1 = conn.cursor()
			print(f'Cursor object : {cur1}') 
			query = (f'DELETE from orderPizza where pizza_type="{pizza}"')
			cur1.execute(query)
			cur2 = conn.cursor()
			selectquery = SelectQuery()
			cur2.execute(selectquery)
			msg = "Data deleted succesfully"
			result = res.generateResponse(cur2,msg)
			conn.close()
			return result

	except KeyError as e:
		return err.ReturnKeyError()		
	except Exception as e:
		print(e)
		return e


if __name__ == '__main__':	
	app.run(debug=True, port=3000)
		





