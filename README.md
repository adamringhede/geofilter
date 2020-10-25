


### Run tests
Run the following command using Docker to run all tests.
```bash
docker run -v "$(pwd):/opt" -w "/opt" python:3.7 python -m unittest tests/*.py
```

### Run application
You can use Docker to run the application locally. A file with name "output.txt" will be created in the project root directory.
```bash
docker run -v "$(pwd):/opt" -w "/opt" python:3.7 python main.py
```
