# We're using Ubuntu 20.10
FROM ximfine/xproject:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/ximfine/Xbot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

CMD ["python3","-m","userbot"]
