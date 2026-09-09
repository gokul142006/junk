pipeline{
    agent any stages{
        stage('checkout'){
            steps{
                git branch : 'main' , url :'https://github.com/gokul142006/junk.git'
            }
        }

        stage('install Dependencies'){
            steps{
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ru Unit Tests'){
            steps{
                bat 'pytest test_app.py'
            }
        }

    }
}