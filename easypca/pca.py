from data import Data
import sys
import numpy as np
from sklearn.preprocessing import StandardScaler
from operator import itemgetter

def get_optimum_k(cum_varience,min_variance):
	k=0
	for val in cum_varience:
		if val >min_variance:
			k+=1
			break
	print "value k= {} cover the variance of {}".format(k,cum_varience[k-1])
	return k
	
def write_to_file(Y,transformed_matrix,out_file):
	out_file_handle=open(out_file,'w')
	for i in range(len(Y)):
		out_str=str(Y[i])+" "
		out_str+=",".join([str(val) for val in transformed_matrix[i]])
		out_file_handle.write(out_str+"\n")
	out_file_handle.close()
	
	

def pca(data,min_variance,out_file):
	X=np.array(data.get_X())
	Y=np.array(data.get_Y())
	X_std=StandardScaler().fit_transform(X)
	mean_vec=np.mean(X_std,axis=0)
	covariance_matrix=((X_std-mean_vec).T.dot((X_std-mean_vec)))/(X_std.shape[0]-1)
	eigen_vals,eigen_vecs=np.linalg.eig(covariance_matrix)
	eigen_pairs=[(np.abs(eigen_vals[i]),eigen_vecs[:,i]) for i in range(len(eigen_vals))]
	eigen_pairs_sorted=sorted(eigen_pairs,key=itemgetter(0),reverse=True)

	eigen_val_sum=sum(eigen_vals)
	varience=[(i[0]/eigen_val_sum)*100 for i in eigen_pairs_sorted]
	cum_varience = np.cumsum(varience)
	k=get_optimum_k(cum_varience,min_variance)
	if k<2:
		k=2
		print "minimum k value should be 2, so going on with 2"
	projection_matrix=np.hstack(((eigen_pairs_sorted[0][1].reshape(data.get_feature_count(),1)),(eigen_pairs_sorted[1][1].reshape(data.get_feature_count(),1))))
	for i in range(2,k):
		projection_matrix=np.hstack((projection_matrix,eigen_pairs_sorted[i][1].reshape(data.get_feature_count(),1)))
	transformed_matrix=X_std.dot(projection_matrix)
	write_to_file(Y,transformed_matrix,out_file)
	
def compute_pca(data_file,min_variance,out_file):
	data=Data()
	data.read_from_file(data_file)
	pca(data,min_variance,out_file)