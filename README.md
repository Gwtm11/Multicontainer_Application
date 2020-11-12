# Multicontainer Orchestration

This is a simple order managment application


#######Docker Product Push
docker exec -i <CHANGE_TO_CONTAINER_NAME> python add_products.py

###### Docker compose
docker-compose -f docker-compose.deploy.yml up -d

##### Docker-machine
docker-machine create packt-order-management

docker-machine start packt-order-management

docker-machine env packt-order-management
$ eval $(docker-machine env packt-order-management)


docker-machine ip packt-order-management
