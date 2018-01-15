FROM python:2.7

MAINTAINER aleksandr.safin@skoltech.ru

RUN pip install numpy scipy sklearn matplotlib

RUN apt-get update && apt-get install texlive -y

RUN apt-get install texlive-bibtex-extra texlive-latex-extra -y

RUN apt-get install biber -y

WORKDIR /example
CMD ls

ADD code ./code
ADD latex ./latex
ADD data ./data
ADD run.sh ./

VOLUME /example/results



RUN chmod +x run.sh

CMD ./run.sh

