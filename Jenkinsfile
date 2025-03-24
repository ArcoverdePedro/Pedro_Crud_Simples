pipeline{
    agent any
    environment{
        PATH = "/home/pedro/Documentos/gittyup/projeto_aerotur/"    
    } 
    stages{

        stage('build'){
            steps{
                sh """
                cd ${PATH}
                ls
                """
                
            }
        }
        stage('test'){
            steps{
                sh "cd ${PATH}"
                echo "World"
                sh "pwd"
            }
        }
    }
}

