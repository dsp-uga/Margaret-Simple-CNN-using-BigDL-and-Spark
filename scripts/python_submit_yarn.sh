#!/bin/sh
#
# Copyright 2016 The BigDL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This template is to show how to submit python job with dependencies on spark yarn clusters.
 
BigDL_HOME=/home/vamsi/softwares/bigdl
SPARK_HOME=/home/vamsi/softwares/spark-2.2.0-bin-hadoop2.7
PYTHON_API_PATH=${BigDL_HOME}/lib/bigdl-0.4.0-SNAPSHOT-python-api.zip
BigDL_JAR_PATH=${BigDL_HOME}/lib/bigdl-SPARK_2.2-0.4.0-SNAPSHOT-jar-with-dependencies.jar
PYTHONPATH=${PYTHON_API_PATH}:$PYTHONPATH

PYSPARK_PYTHON=/home/vamsi/softwares/venv/bin/python
${SPARK_HOME}/bin/spark-submit \
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./venv.zip/venv/bin/python \
--driver-cores 1 \
--executor-memory 10g \
--driver-memory 10g \
--executor-cores 1 \
--num-executors 2 \
--properties-file ${BigDL_HOME}/conf/spark-bigdl.conf \
--jars ${BigDL_JAR_PATH} \
--py-files ${PYTHON_API_PATH} \
--archives venv.zip \
--conf spark.dynamicAllocation.enabled=false \
--conf spark.driver.extraClassPath=bigdl-SPARK_2.2-0.4.0-SNAPSHOT-jar-with-dependencies.jar \
--conf spark.executor.extraClassPath=bigdl-SPARK_2.2-0.4.0-SNAPSHOT-jar-with-dependencies.jar \
cnn.py
