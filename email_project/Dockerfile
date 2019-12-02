FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Kolkata

RUN sed -i -e 's/http:\/\/archive/mirror:\/\/mirrors/' -e 's/http:\/\/security/mirror:\/\/mirrors/' -e 's/\/ubuntu\//\/mirrors.txt/' /etc/apt/sources.list && \
    echo "Acquire {http {Timeout \"60\";}; ftp {Timeout \"60\";};};" > /etc/apt/apt.conf.d/custom-apt.conf && \
    apt-get update && apt-get dist-upgrade --yes && \
	apt-get install -y libpq-dev python3-dev python3-pip curl && \
	apt-get autoremove -y && apt-get clean -y && \
	pip3 install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to
WORKDIR /root/source/

# Only requirements.txt is copied so Docker build cache doesn't get invalidated
# every time we change other files in the project
COPY requirements.txt /root/source/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r /root/source/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /root/source

# Run the app
ENTRYPOINT ["/bin/sh", "-c", "python3 manage.py runserver 0.0.0.0:8000"]

EXPOSE 8000