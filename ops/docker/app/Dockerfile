FROM lambci/lambda:python3.7

RUN apt-get update
RUN apt-get install -y vim curl nodejs

RUN mkdir /tmp/install
WORKDIR /tmp/install
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD package.json package.json
ADD package.lock package.lock
RUN npm install -g serverless
RUN npm install

WORKDIR /app

RUN cp -r /tmp/install/* app

CMD serverless offline start --host=0.0.0.0 --stage local --apiKey local
