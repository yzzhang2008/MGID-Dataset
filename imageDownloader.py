# coding:utf-8
# Note that this is an example code with single thread.
import os
import csv

import urllib.request

def main():
	image_url_dir = '...\\dev\\dev.csv' #the url data path
	data_label = "dev"
	i = 1
	target_path = '...\\downloadimage\\dev\\' # your download path

	csv_file = csv.reader(open(image_url_dir))
	for item in csv_file:
		image_url = item[4]
		if image_url != "Image URL":
			# print(image_url)
			try:
			    if not os.path.exists(target_path):
			    	os.makedirs(target_path) 
			    image_name = data_label+"_"+str(i)+".jpg"
			    print(image_name)

			    target_path_name = '{}{}'.format(target_path, image_name) #拼接文件名。
				# print(target_path_name)

			    urllib.request.urlretrieve(image_url, filename=target_path_name) 
			    print("succeed..------>"+image_name)
			    i += 1

			except IOError as e:
			    print(1, e)

			except Exception as e:
			    print(2, e)


if __name__ == '__main__':
	main()