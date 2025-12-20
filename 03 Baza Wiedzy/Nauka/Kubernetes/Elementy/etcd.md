# Co to jest ?

1.  Jest to key value store
2.  Jest: Proste, Bezpieczne, Szybkie
3.  Jest to słownik jakby czy nawet hashmapa
4. Trzyma dane w stylu key:value/values

# Jak działa ? 

 1.  Instalujesz i uruchamiasz
 2.  Startuje Serwis na porcie 2379
 3.  Dodajesz klienta etcd Client
 4. Komendy:
	 1.  ./etcdctl put key1 value1
	 2.  ./etcdctl get key1 -> value1
	 3. /etcdctl - > specific data: version itp.
 5. etcd Versions:
	 ![[Pasted image 20251212232916.png]]


# Rola w K8s ?

1.  Przetrzymuje informacje o wszytskim min,:
	1. Nodes
	2. Pods
	3. Configs
	4. Secrets
	5. Accounts
	6. Roles
	7. Binding
	8. Others
2.  Manualnie można pobrać i uruchomić jako serwis
3.  Można użyć kubeadm
	1. Będzie jako pod w cluster
	2. Dane są utrzymywane w czym w stylu ścieżki Registry/(Minions, Pods, ReplicaSets, Deployments, Roles, Secrets)
4.  Gdy masz kilka etcd to musisz je poinformować o ich własnym istnieniu


# Komendy - KodeKloude Notes:

ETCDCTL is the CLI tool used to interact with ETCD.ETCDCTL can interact with ETCD Server using 2 API versions – Version 2 and Version 3. By default it’s set to use Version 2. Each version has different sets of commands.

For example, ETCDCTL version 2 supports the following commands:

```
etcdctl backup
etcdctl cluster-health
etcdctl mk
etcdctl mkdir
etcdctl set
```

Whereas the commands are different in version 3

```
etcdctl snapshot save
etcdctl endpoint health
etcdctl get
etcdctl put
```

To set the right version of API set the environment variable ETCDCTL_API command

```
export ETCDCTL_API=3
```

When the API version is not set, it is assumed to be set to version 2. And version 3 commands listed above don’t work. When API version is set to version 3, version 2 commands listed above don’t work.

Apart from that, you must also specify the path to certificate files so that ETCDCTL can authenticate to the ETCD API Server. The certificate files are available in the etcd-master at the following path. We discuss more about certificates in the security section of this course. So don’t worry if this looks complex:

```
--cacert /etc/kubernetes/pki/etcd/ca.crt
--cert /etc/kubernetes/pki/etcd/server.crt
--key /etc/kubernetes/pki/etcd/server.key
```

So for the commands, I showed in the previous video to work you must specify the ETCDCTL API version and path to certificate files. Below is the final form:

```
kubectl exec etcd-controlplane -n kube-system -- sh -c "ETCDCTL_API=3 etcdctl get / \
  --prefix --keys-only --limit=10 / \
  --cacert /etc/kubernetes/pki/etcd/ca.crt \
  --cert /etc/kubernetes/pki/etcd/server.crt \
  --key /etc/kubernetes/pki/etcd/server.key"
```
