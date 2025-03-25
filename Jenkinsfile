pipeline {
    agent any
    environment {
        REPO_PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"
        IMAGE_NAME = "projeto_aerotur"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    sh '''
                        echo "Entrando no diretório: ${env.REPO_PATH}"
                        cd "${env.REPO_PATH}"
                        docker-compose build
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                        echo "Test Stage"
                        cd "${env.REPO_PATH}"
                        docker-compose up --build -d
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
