# Base image
FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Copy the local requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# pip install all the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy local code into the container image
COPY ./app /code/app

# The command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
