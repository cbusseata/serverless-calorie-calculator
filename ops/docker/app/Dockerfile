FROM lambci/lambda:build-python3.6

RUN yum update -y
# Need my preferred CLI text editor
RUN yum install -y vim

# Install node to install serverless plugins and run serverless-offline
RUN yum install -y curl 
# Need to add the node repository before we can install node
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash
RUN yum install -y nodejs

RUN pip install pipenv

# Create an installation directory
RUN mkdir /tmp/install

# Install python modules
WORKDIR /tmp/install
ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pipenv install --dev --system

# Install node modules
ADD package.json package.json
ADD package-lock.json package-lock.json
RUN npm install -g serverless
RUN npm install

WORKDIR /app

# Move over the install files
RUN cp -r /tmp/install/* .

# Startup serverless offline
CMD serverless offline start --host=0.0.0.0 --stage local --apiKey local-test
