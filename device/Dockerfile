FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Bundle app source
COPY device.py /src/device.py

CMD ["python", "/src/device.py"]