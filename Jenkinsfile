pipeline{
    agent any
    REPO = "/home/pedro/Documentos/gittyup/projeto_aerotur"
    stages{
        stage('build'){
            steps{
                echo "Hello"
                sh "cd $REPO"
                sh "docker build -t"
            }
        }
        stage('test'){
            steps{
                echo "World"
                sh "cd $REPO"
                sh "docker compose up -d"
            }
        }
    }
}