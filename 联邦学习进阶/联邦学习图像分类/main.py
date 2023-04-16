import argparse, json
import datetime
import os
import logging
import torch, random

from server import *
from client import *
import models, datasets

	

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Federated Learning')
	parser.add_argument('-c', '--conf', dest='conf')
	args = parser.parse_args()
	

	with open('./utils/conf.json', 'r') as f:
		conf = json.load(f)	
	
	
	train_datasets, eval_datasets = datasets.get_dataset("./data/", conf["type"])    # cifar数据集
	
	server = Server(conf, eval_datasets)
	clients = []
	
	for c in range(conf["no_models"]):    #10
		clients.append(Client(conf, server.global_model, train_datasets, c))    # c是从0到10  也就是id
		
	print("\n\n")
	for e in range(conf["global_epochs"]):     #global epoch   20
	
		candidates = random.sample(clients, conf["k"])     #k=5  随机采样5个
		
		weight_accumulator = {}
		
		for name, params in server.global_model.state_dict().items():   # 聚合过程   先置0  后面添加到weight accumulator
			weight_accumulator[name] = torch.zeros_like(params)
		
		for c in candidates:
			diff = c.local_train(server.global_model)
			
			for name, params in server.global_model.state_dict().items():
				weight_accumulator[name].add_(diff[name])
				
		
		server.model_aggregate(weight_accumulator)
		
		acc, loss = server.model_eval()
		
		print("Epoch %d, acc: %f, loss: %f\n" % (e, acc, loss))
				
			
		
		
	
		
		
	