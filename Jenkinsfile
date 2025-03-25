pipeline {
    agent any
    environment {
        REPO_PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"
        CONTAINER_NAME = "projeto_aerotur_container" // Nome do seu container
        IMAGE_NAME = "projeto_aerotur" // Nome da sua imagem
    }
    stages {
        stage('build') {
            steps {
                script {
                    sh '''
                        echo "Current REPO_PATH: ${REPO_PATH}"
                        cd ${REPO_PATH}
                        docker-compose build --no-cache -t ${IMAGE_NAME} .
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
                        docker-compose up --build -d
                    '''
                }
            }
        }
        stage('Limpeza Containers e Imagens') {
            steps {
                script {
                    sh '''
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