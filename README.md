This is a play area for sybase to oracle migration

- Oracle Docker Image is large
- You will have to clone this repot and build it image locally first
- https://github.com/oracle/docker-images
- Download this: 3.2gb
- https://www.oracle.com/database/technologies/oracle12c-linux-12201-downloads.html#license-lightbox
-  mv ~/Downloads/linuxx64_12201_database.zip $(pwd)/docker-images/OracleDatabase/SingleInstance/dockerfiles/12.2.0.1/
- cd cd $(pwd)/docker-images/OracleDatabase/SingleInstance/dockerfiles/
-  ./buildDockerImage.sh -v 12.2.0.1 -e
