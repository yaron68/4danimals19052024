FROM  python:3.11.7-alpine3.19
WORKDIR app
RUN pip3 install flask==2.1.2
RUN pip3 install Werkzeug==2.1.1
COPY main.py .
EXPOSE 5000
ENTRYPOINT [ "python3" , "main.py" ]