FROM lambci/lambda:build-python3.7

RUN yum update -y
RUN yum install -y vim 
RUN yum install -y curl 
# Need to add the node repository before we can install node
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash
RUN yum install -y nodejs

RUN mkdir /tmp/install
WORKDIR /tmp/install
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD package.json package.json
ADD package-lock.json package-lock.json
RUN npm install -g serverless
RUN npm install

WORKDIR /app

RUN cp -r /tmp/install/* .

CMD serverless offline start --host=0.0.0.0 --stage local --apiKey local-test
