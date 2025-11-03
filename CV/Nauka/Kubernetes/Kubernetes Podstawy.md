## Node process:

- One Node with 2 pods inside:
	- Container runtime should be installed inside
	- Kublet - interact with container and node 
	- Kube porxy - forwards the requests
-  How to interact with it ?
	- Master process:
	- Master Node - control the cluster
		- API Server - validates requests
		- Scheduler - Schedule new Pod, assign to worker NOD (Where to put the POD by resources available) exectude by Kubelt
		- Controller manager - recover dead pod 
		- etcd - cluster brain, key valu store