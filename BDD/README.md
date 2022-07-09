## Generating logs from BDD test step by step

1 - Install allure-behave package with pip

```bash
# sudo apt install default-jre -y
# sudo apt install default-jdk -y
# pip install allure-behave
```

2 - Generate logs from features

```bash
# behave -f allure_behave.formatter:AllureFormatter -o report ./features1/
```
**Note:** you should stay on directory that has app folder.

3 - Install allure servic to serve server for graphical usage of logs

```bash
# wget https://github.com/allure-framework/allure2/releases/download/2.7.0/allure-2.7.0.zip
# unzip allure-2.7.0.zip
# ./allure-2.7.0/bin/allure serve ./report1 ./report2 ...
```
