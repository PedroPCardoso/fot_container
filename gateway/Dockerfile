FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Bundle app source
COPY gateway_cloud.py /src/gateway_cloud.py

#mapea a porta que eu quero ?
EXPOSE  20001


CMD ["python", "/src/gateway_cloud.py"]