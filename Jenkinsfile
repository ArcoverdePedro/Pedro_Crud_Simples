pipeline {
    agent any
    environment {
        REPO_PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"
    }
    stages {
        stage('build') {
            steps {
                script {
                    // Usando REPO_PATH ao invés de PATH
                    sh '''
                        echo "Current REPO_PATH: ${REPO_PATH}"
                        cd ${REPO_PATH}
                        echo 'Hello'
                        ls
                    '''
                }
            }
        }
        stage('test') {
            steps {
                script {
                    sh '''
                        echo "Test Stage"
                        cd ${REPO_PATH}
                        echo 'World'
                        pwd
                    '''
                }
            }
        }
    }
}
