
from  flask import jsonify

def generateResponse(data,msg):
	response_data = {}
	data_list = []
	try:
		for i in data:
			temp={}
			temp["id"] = i[0]
			temp["pizza"] = i[1]
			temp["size"] = i[2]
			temp["count"] = i[3]
			temp["price"] = i[4]
			temp["name"] = i[5]
			temp["number"] = i[6]
			temp["address"] = i[7]
			temp["status"] = i[8]
			data_list.append(temp)
			response_data["data"]=data_list

		response_data["msg"]=msg
		print(f'Respone data : {response_data}')
		return jsonify(response_data)

	except IndexError as e:
		print(e)
		return ReturnInvalidData()


