apt-get install python-dev
easy_install pip
mkdir softwares
cd softwares
wget http://www.gtlib.gatech.edu/pub/apache/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz
tar -xvzf *.tgz
mkdir bigdl
cd bigdl
wget https://oss.sonatype.org/content/groups/public/com/intel/analytics/bigdl/dist-spark-2.2.0-scala-2.11.8-linux64/0.4.0-SNAPSHOT/dist-spark-2.2.0-scala-2.11.8-linux64-0.4.0-20171123.040728-14-dist.zip
unzip *.zip
cd ..

