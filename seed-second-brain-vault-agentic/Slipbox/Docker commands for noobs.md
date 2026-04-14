---
creation date: 2026-01-13 17:15
tags: [concept]
---
![[unnamed.png]]


```bash
docker images
docker run hello-world:latest
docker run hello-world
docker run -ti ubuntu bash
docker ps
docker ps -a
docker commit docker-image-name
docker tag xxxxxxxxxidxxxxxx new-image-name
docker commit old-image new-image-name

```

```bash
docker run --rm -it ubuntu bash -c "sleep 3; echo Im done"

#detached containers, leaving them running
docker run -d -it ubuntu bash

docker attach container-name
# ctrl p, cmd+d detach keyboard shortcut.

docker exec -ti container_name bash

```

```bash
docker run --name some-name -d image-name -c "additional commands"

docker logs some-name

docker kill container-name

docker rm container-name

```

Ports and containers
what is Netcap?
```bash
docker run --rm -ti -p 5000:5000 -p 3000:3000 --name port-cont ubuntu:14.04 bash

nc -lp 5000 | nc -lp 3000

docker port port-cont

docker run -ti -rm -p 5000/udp --name my_con ubuntu:14.04 bash
nc -ulp 5000

# DOn't let your container fetch their dependencies when they start. 
```

Container networks

```bash

```

Managing images

```bash

```

Docker volumes

```bash

```

Docker registries

```bash

```

Container networks

```bash

```

Container networks

```bash

```

Container networks

```bash

```

