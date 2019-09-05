#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# Note: You can use any Debian/Ubuntu based image you want. 
FROM python:3

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Docker Compose version
ARG COMPOSE_VERSION=1.24.0

COPY *requirements.txt /tmp/pip-tmp/

# Configure apt and install packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1 \
    #
    # Verify git, process tools installed
    && apt-get -y install git procps \
    #
    # Install Docker CE CLI
    && apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common lsb-release \
    && curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | (OUT=$(apt-key add - 2>&1) || echo $OUT) \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get install -y docker-ce-cli fish vim postgresql-client \
    && apt-get install -y build-essential unzip python-dev libaio-dev alien \
    #
    # Install Docker Compose
    && curl -sSL "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    #
    # Pylint
    && pip --disable-pip-version-check --no-cache-dir install pylint wget unixodbc-dev  \
    #
    # Pip items
    && if [ -f "/tmp/pip-tmp/requirements.txt" ]; then pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt; fi \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
#oracle client tools you may have to update this if oracle changes this endpoint
RUN wget https://download.oracle.com/otn_software/linux/instantclient/193000/oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm 
RUN wget https://download.oracle.com/otn_software/linux/instantclient/193000/oracle-instantclient19.3-sqlplus-19.3.0.0.0-1.x86_64.rpm
RUN alien -i oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm \
    && alien -i oracle-instantclient19.3-sqlplus-19.3.0.0.0-1.x86_64.rpm 

#https://archive.sap.com/documents/docs/DOC-35857
RUN wget http://d5d4ifzqzkhwt.cloudfront.net/sqla16client/sqla16_client_linux_x86x64.tar.gz
RUN tar -C .. -xvf sqla16_client_linux_x86x64.tar.gz
RUN odbcinst -i -d -f driver template file
# Switch back to dialog for any ad-hoc use of apt-get
ENV LD_LIBRARY_PATH=/usr/lib/oracle/19.3/client64/lib/
ENV DEBIAN_FRONTEND=dialog