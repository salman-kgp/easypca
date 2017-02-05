import sys
import os
import re

def isnumeric(data):
	if re.match("^[1-9]\d*(\.\d+)?$",data):
		return True
	return False

def get_number_of_features(data_point):
	data_point=data_point.strip().split(" ")
	if isnumeric(data_point[0]):
		features=data_point[1].split(",")
		for f in features:
			if not isnumeric(f):
				raise ValueError("Feature is not numeric at line 1")
		return len(features)
	raise ValueError("Class label is not numeric at line 1")
		

def validata(data_point,no_of_features,line_no):
	data_point=data_point.strip().split(" ")
	if isnumeric(data_point[0]):
		features=data_point[1].split(",")
		if len(features)!=no_of_features:
			raise ValueError("No of features do not match at line "+str(line))
		for f in features:
			if not isnumeric(f):
				raise ValueError("Feature is not numeric at line "+str(line_no))
		return True
	raise ValueError("Class label is not numeric at line "+str(line_no))

def check_data(file_name):
	if not os.path.exists(file_name):
		raise IOError(file_name+" not found, please check the file name")
	
	data_file_handle=open(file_name,'r')
	line=data_file_handle.readline()
	no_of_features=get_number_of_features(line)
	line_no=1
	line=data_file_handle.readline()
	while line:
		if  validata(line,no_of_features,line_no+1):
			line=data_file_handle.readline()
			line_no+=1
			continue
	return True
	
	


if __name__=="__main__":
	if len(sys.argv)!=2:
		print "USAGE: python check_data.py datafile.txt"
		exit()
		
	inp_file=sys.argv[1]
	if check_data(inp_file):
		print "Data is valid" 