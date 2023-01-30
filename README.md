# machine_learning_project
# this is my first machine learning project.




# Software and account requirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)



creating conda environment
```

conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
o
or
```
conda activate venv
```
```
command to install requirements
```
pip install -r requirements.txt
```

to add files to git
```
git add .
```

or
```
git add <file_name>
```

to ignore file or folder from git we can write name of file/folder in .gitignore file

to check the git ststus
```

git status
```
to check all version maintained by git
```
git log
```

to create version/commit all changes by git
```

git commit -m "message"

to send version/changes to github
```

git push origin main
```

to check remote url
```
git remote -v








To setup CI/CD pipeline in heroku we need 3 info
1. HEROKU_EMAIL = 
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = 

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

note: the name of the docker image will be the lower case

 ```
 to list docker image

 ```
docker images
 ```
to run docker image

```
docker run -p 5000:5000 -e PORT=5000 <image id>
```
to check running container in docker
```
docker ps
```
to stop image
```
docker stop <containerid>
```