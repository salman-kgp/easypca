import check_data

class Data:
	def __init__(self):
		self.X=[]
		self.Y=[]
		self.no_of_features=0
		
	def read_from_file(self,file_name):
		if check_data.check_data(file_name):
			data_file_handle=open(file_name,'r')
			line=data_file_handle.readline()
			while line:
				line_tocks=line.strip().split(" ")
				self.Y.append(float(line_tocks[0]))
				feature_set=line_tocks[1].split(",")
				self.X.append([float(f) for f in feature_set])
				line=data_file_handle.readline()
			if len(self.X)>0:
				self.no_of_features=len(self.X[0])
				
	def get_X(self):
		return self.X
	
	def get_Y(self):
		return self.Y
	
	def get_feature_count(self):
		return self.no_of_features
		
	def add_data(self,X,Y):
		self.X.append(X)
		self.Y.append(Y)
		
