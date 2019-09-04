This is a play area for sybase to oracle migration

# Requirements
- Visual Code 1.34+
- Docker
- Git

# Clone this project
- git clone --recursive https://github.com/hung135/sybase-oracle
- Oracle Docker Image is large, you will have to download the installation files
- This download is 3.2gb
- https://www.oracle.com/database/technologies/oracle12c-linux-12201-downloads.html#license-lightbox
# Move file into path in git project repo
-  mv ~/Downloads/linuxx64_12201_database.zip $(pwd)/docker-images/OracleDatabase/SingleInstance/dockerfiles/12.2.0.1/
#cd into the top level of the git project directory
# Build the local Docker Image
- cd $(pwd)/docker-images/OracleDatabase/SingleInstance/dockerfiles/
-  ./buildDockerImage.sh -v 12.2.0.1 -e
- - yield image name 
- - oracle/database:12.2.0.1-ee
 
# Open Project in Visual Studio Code
- Click on open in container

