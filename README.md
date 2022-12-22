# IoT Datastore

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)

- **Documentation:** https://iot-datastore.netlify.app/
- **Source Code:** https://github.com/MMartin09/iot-datastore

> Be aware that MongDB 5.0 or higher is required to support timeseries.

## Requirements

- **MongoDB Atlas Account:** https://www.mongodb.com/atlas

## Quickstart

Install the dependencies:
```bash
poetry install
```

Start the MongoDB container
```bash
docker-compose up
```

Run the RestAPI server:
```bash
poetry run main.py
```

## Contributing

Install the *pre-commit* hooks `pre-commit install`

## Roadmap

- Deploy API on AWS
- Implement sensor authentication
