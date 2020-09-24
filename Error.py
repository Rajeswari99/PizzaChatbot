from flask import jsonify

def ReturnConnectionError():
	return jsonify({"error_msg":"Connection error"})

def ReturnFetchError():
	return jsonify({"error_msg" : "Unable to fetch data"})

def ReturnInvalidData():
	return jsonify({"error_msg":"Invalid data"})

def ReturnKeyError():
	return jsonify({"error_msg":"Invalid Key in body"})

def ReturnValueError():
	return jsonify({"error_msg":"Invalid value in body"})	

def ReturnUpdateError():
	return jsonify({"error_msg":"Unable to update data"})

def ReturnDuplicateDataError():
	return jsonify({"error_msg":"Data exits Aldready"})
