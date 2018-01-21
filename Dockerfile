FROM python:3.6

MAINTAINER aleksandr.safin@skoltech.ru

RUN pip3 install numpy scipy sklearn matplotlib

RUN apt-get update && apt-get install texlive -y

RUN apt-get install texlive-bibtex-extra texlive-latex-extra -y

RUN apt-get install biber -y

RUN pip3 install nltk networkx

RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader averaged_perceptron_tagger

WORKDIR /example


ADD code ./code
ADD latex ./latex
ADD data ./data
ADD run.sh ./

VOLUME /example/results



RUN chmod +x run.sh

CMD ./run.sh


