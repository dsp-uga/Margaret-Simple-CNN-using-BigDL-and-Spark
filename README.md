# Malware Classification

For this project, we are using the data from the Microsoft Malware Classification Challenge,
which consists of nearly half a terabyte of uncompressed data. There are no fewer
than 9 classes of malware, but unlike the documents from P1, each instance of malware
has one, and only one, of the following family categories:

1. Ramnit
2. Lollipop
3. Kelihos_ver3
4. Vundo
5. Simda
6. Tracur
7. Kelihos_ver1
8. Obfuscator.ACY
9. Gatak

## Getting Started

All the documents are in hexadecimal format, in their own files (one file per document); these files are located here:
https://storage.googleapis.com/uga-dsp/project2/data/bytes/


### Prerequisites

What things you need to install the software and how to install them

BigDL  
Python  
Spark  
JAVA  

### Installing

pip install default-java   
sudo apt-get install python-dev python-setuptools     
sudo apt-get install zip gcc    
sudo easy_install pip    
Pip install pysaprk    
pip install BigDL    
sh instance_startup.sh   
sh python_package.sh   




## Deployment

BigDL is supported only by Python 2.7, 3.5 and 3.6 for now. 
BigDL can be installed directly from pip when it is to be used in local mode. When deploying it to the cluster mode requires pip installing without pip. A detailed description of the procedures of how to install it with out pip have been provided in the BigDL repo.

Repo Link:  https://github.com/intel-analytics/BigDL/

BigDL Installation without pip: https://github.com/intel-analytics/BigDL/blob/master/docs/docs/PythonUserGuide/install-without-pip.md

A virtual environment will be created with BigDL, Spark, Python along with the dependent packages which can be zipped and added as archives when submitting the task to the cluster. This helps in saving the time for installation as simillar environment and dependent packages should be present in all the workers. Scripts for creating the env and installing all the neccesary packages can found at:
          https://github.com/intel-analytics/BigDL/tree/master/pyspark/python_package
         
These scripts have been customized according to the projects purpose and were available in scripts directory. 

Inorder to deploy, adding all the virtual env to the archives during cluster deployement can done through 'scripts/python_submit_yarn.sh'.

## Built With

* [Google Cloud Platform](https://cloud.google.com/) - Everything You Need To Build And Scale

## Contributors

Please read [CONTRIBUTORS.md](https://github.com/dsp-uga/Margaret/blob/master/CONTRIBUTORS.md) for details on our code of conduct

## Authors

* **Nihal Soans** - [nihalsoans91](https://github.com/nihalsoans91)
* **Raunak Dey**  - [PurpleBooth](https://github.com/raun1)
* **Vamsi Nadella** - [vamsi3309](https://github.com/vamsi3309)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
