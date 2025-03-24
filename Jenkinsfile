pipeline{
    agent any 
    stages{
        stage('build'){
            steps{
                echo "Hello"
                sh 'pwd'
                cd '/home/pedro/Documentos/gittyup/projeto_aerotur/'
                sh 'ls -l'
            }
        }
        stage('test'){
            steps{
                echo "World"
                sh 'pwd'
            }
        }
    }
}

