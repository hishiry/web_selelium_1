pipeline {
    agent {
      label 'web'
    }

    tools {
      allure 'allure'
      git 'Default'
      maven 'Default'
    }

    // tools {
    //     // Install the Maven version configured as "M3" and add it to the path.
    //     maven "M3"
    // }

    stages {
        stage('Clean') {
            steps {
                sh 'rm -rf allure junit.xml'
            }
        }
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
//                 git branch: 'main', url: 'https://gitlab.stuq.ceshiren.com/hogwarts/spring-petclinic.git'
                git branch: 'main', url: 'https://gitlab.com/hishiry/web_selelium_1.git'
            }
        }
        stage('Tests') {
            parallel {
                stage('Test2') {
                    steps {
                        sh 'echo Test2'
                    }
                }
                stage('Test3') {
                    steps {
                        sh 'echo Test3'
                    }
                }
                stage('Test1') {
                    steps {
                        sh 'ls'
                        sh 'python3 -m pytest --alluredir=allure --junitxml=junit.xml tests/test_search_page.py'
                    }
                    post {
                        success {
                            junit 'junit.xml'
                            archiveArtifacts 'junit.xml'
                            allure includeProperties: false, jdk: '', results: [[path: 'allure']]
                        }
                    }
                }
            }
        }
    }
}
