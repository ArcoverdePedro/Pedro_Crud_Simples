pipeline {
    agent any
    environment {
        REPO_PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    sh '''
                        echo "Build Stage"
                        cd "${REPO_PATH}"
                        docker compose build --no-cache
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                        echo "Test Stage"
                        cd "${REPO_PATH}"
                        docker compose up --build -d --remove-orphans
                    '''
                }
            }
        }
        stage('Limpeza Containers e Imagens') {
            steps {
                script {
                    sh '''
                        echo "Limpando imagens não utilizadas..."
                        docker system prune -af
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executado com sucesso!'
        }
        failure {
            echo 'Pipeline falhou!'
        }
    }
}
