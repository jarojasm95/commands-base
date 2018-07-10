FROM alpine:3.6

RUN apk add --update python py-pip vim curl bash 

WORKDIR /code

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY command.py .

# Inherit from this docker and copy your project's commands directory to /code/commands folder and any other necessary files into the code directory

ENTRYPOINT tail -f /dev/null # Sleep infinity equivalent in alpine
