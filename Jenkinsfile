pipeline {
    agent any
    environment {
        REPO_PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"
    }
    stages {
        stage('build') {
            steps {
                script {
                    // Adicionando um comando de depuração para garantir que o PATH seja correto
                    echo "Current PATH: ${env.PATH}"
                    sh '''
                        echo "Before CD"
                        ls -la
                        cd ${REPO_PATH}
                        echo "After CD"
                        ls -la
                        echo 'Hello'
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
