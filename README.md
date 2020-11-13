# Multicontainer Orchestration

A retail app that maintains a separate active directory for the user and DB to store product information.

*Each Module in this application is decoupled to create a microservice architecture*


![Workflow and basic architecture](Images/Architecture.png | width=400)


###Installation GUIDE

Required Modules
* KOPS
* HELM
* Kubectl
* Docker 

## Setup k8 dashboard

 =============K8s DASHBOARD=============
#### Step 1 Get dashboard pod
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
```

#### Step 2 Set Service account

```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
EOF
```

#### Step 3: Set Role binding for the cluster
```
cat <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
EOF
```

#### Step 4: Get Secret Token

```
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
```

#### Step 5: Set proxy
```
kubectl proxy
```