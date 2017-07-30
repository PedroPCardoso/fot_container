FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Bundle app source
COPY cloud_serv.py /src/cloud.py

#mapea a porta que eu quero ?
EXPOSE  2004


CMD ["python", "/src/cloud.py"]