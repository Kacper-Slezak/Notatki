# Co to ?

1. Narzędzie odpowiedzialne za utrzymanie określonej ilosci podów 
2. Posługuje się [[kube-apiserver]]
3. Wykorzytujemy go też do [[Loadbalancing]] i Scalingu 
4. Został wyparty przez [[ReplicaSet]] ale różnice nie są duże

# Jak używać

1. apiVersion: v1
2. kind: ReplicationController
3. metadata: to samo co w pod
4. spec: 
	1. template:
		1. wklejamy tu metada i spec pod'a który nas interesuje 
	2. replicas

