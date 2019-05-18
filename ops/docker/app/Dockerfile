FROM lambci/lambda:build-python3.6

RUN yum update -y
# Need my preferred CLI text editor
RUN yum install -y vim

# Install node to install serverless plugins and run serverless-offline
RUN yum install -y curl 
# Need to add the node repository before we can install node
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash
RUN yum install -y nodejs

# Create an installation directory
RUN mkdir /tmp/install

# Install python modules
WORKDIR /tmp/install
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install node modules
ADD package.json package.json
ADD package-lock.json package-lock.json
RUN npm install -g serverless
RUN npm install

WORKDIR /app

# Move over the install files
RUN cp -r /tmp/install/* .

# Setup virtual environment for when we need to add modules later, otherwise we pip freeze every global module
#  in the app container
ADD requirements.txt requirements.txt
RUN python -m venv .
RUN bash --rcfile "/app/venv/bin/activate" -i && pip install --ignore-installed --user -r requirements.txt

# Startup serverless offline
CMD serverless offline start --host=0.0.0.0 --stage local --apiKey local-test
