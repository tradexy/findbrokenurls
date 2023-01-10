# Force Scaling Containers

## Check Requirements in AWS
_EC2 Only_
1. Go to the _Task Definitions_ page, in AWS, and find your microservice
2. Look at the CPU and Memory Requirements of the microservice (Make a note of these)

![force_scaling1](../../assets/how-to-force-scale-containers/force_scale_containers1.png)


## Check Available Capacity for Cluster
_EC2 Only_
1. Go to the Clusters Page and select the cluster relevant to the microservice (FED or DAL)
2. Select the ECS instances tab in the page
3. Check if the container instances listed have enough CPU and Memory available for what you want to scale up by
    - If you are scaling by multiple instances then remember to calculate how much capacity is needed by _all_ of them. For 2 instances of the above there needs to be 1024 CPU availability and 2048 MiB Memory available (but this can be split over multiple containers - ie each container has capacity for 512 CPU and 1024 Memory)

![force_scaling2](../../assets/how-to-force-scale-containers/force_scale_containers2.png)

4. If there is not enough capacity then increase the desired capacity of EC2 in the autoscaling group

## Check Persistent Storage Means (DataDog)
1. Look at the Persistent Storage dashboard in DataDog ([here](https://app.datadoghq.com/dashboard/p99-8um-6sk/prod1-persistent-storage?from_ts=1602745286740&live=true&to_ts=1602748886740))
2. Give it a sanity check to make sure there is enough capacity on persistent dependencies (DB connections, Redis connection, elastic search utilisation etc.)


## Change Capacities in Release (Azure)
_NOTE: If you want to change the variables of a specific release, follow the guide [here](https://vfuk-digital.visualstudio.com/Digital/_wiki/wikis/Digital%20X.wiki/5369/Force-Scaling-Containers-(old)) instead_
1. In Azure, navigate to Releases and find the release for your microservice 
![force_scaling3](../../assets/how-to-force-scale-containers/force_scale_containers3.png)
2. Click Edit. Open the Variables Tab and select Variable groups
3. On the list find the correct variable group (it will have the scope of the relevant environment as well)
![force_scaling4](../../assets/how-to-force-scale-containers/force_scale_containers4.png)
4. In this example we want to scale web-voxi on the dev1 environment
5. Expand the list for your chosen variable group
![force_scaling5](../../assets/how-to-force-scale-containers/force_scale_containers5.png)
6. Click on the name of the variable group and change the numbers for Desired Count, Min Capacity and Max Capacity to fit what you need (Save the changes)
![force_scaling6](../../assets/how-to-force-scale-containers/force_scale_containers6.png)
7. Create a new release using the last successful build (Make sure ID number is the same and other environment variables have not changed)

https://aaaaaaaaaaaaaa.corn