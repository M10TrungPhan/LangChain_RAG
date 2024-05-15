FROM python:3.9

# Set the path to the API directory
WORKDIR /app/api

# Copy the codebase into the container
COPY . .

# # Install the requirements
# RUN apt-get update && apt-get install -y curl zip unzip
# RUN curl -s 'https://get.sdkman.io' | bash
# RUN /bin/bash -c "source $HOME/.sdkman/bin/sdkman-init.sh; sdk version; sdk install java 8.0.302-open; sdk install maven 3.8.6"

# apt-get install -y default-jre
# # Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y default-jre && \
    apt-get install -y ant && \
    apt-get clean;
    
# # Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# # Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME


RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8888

ENTRYPOINT ["uvicorn", "main:app", "--host", "api", "--port", "8888", "--reload"]