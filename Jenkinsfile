pipeline{
    agent any
    environment{
        PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"    
    } 
    stages{
        stage('build'){
            steps{
                sh 'cd ${PATH}'
                echo 'Hello'
                sh 'ls'
                
            }
        }
        stage('test'){
            steps{
                sh 'cd ${PATH}'
                echo 'World'
                sh 'pwd'
            }
        }
    }
}

