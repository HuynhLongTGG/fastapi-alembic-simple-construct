FROM dragon093979/ubuntu:py3.10

# Create directory for the application
RUN mkdir /workspace

WORKDIR /workspace

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN apt install libgdiplus libc6-dev -y

# Install Python dependencies
COPY requirements.txt /workspace
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

RUN alias python='/usr/bin/python3.10'
RUN python3.10 -c "import nltk;nltk.download('punkt');nltk.download('wordnet')"
# Copy the application code
COPY . /workspace
WORKDIR /workspace/app

