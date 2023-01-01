RUN apt-get update -y && apt-get upgrade -y
RUN apt-get installl python3 -y
RUN apt-get install git -y

RUN git clone https://github.com/Jaswanthravichandran/NetRecon.git -y

RUN cd Net-Recon

RUN pip install -r requirements.txt

RUN python3 Net_Recon.py