# aws-scripts

## Prereqs

- ####Software

    - [Python 3.9](https://www.python.org/downloads/)
    - [Poetry](https://python-poetry.org/)

        Python packaging and dependency management
        
       #### Installation
        
        osx / linux
        
          curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    
        windows powershell
        
          (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

- ####Initializing 
    
      poetry install

## Scripts

- ./bin/modify_instance_user_data.py
        
    ###Executing
    
      poetry run ./bin/modify_instance_user_data.py -t '{"Name":"foobar-server-name"}' -f ./testing.sh
    