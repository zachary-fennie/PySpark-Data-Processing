[![CI_CD](https://github.com/zachary-fennie/PySpark-Data-Processing/actions/workflows/CI_CD.yml/badge.svg)](https://github.com/zachary-fennie/PySpark-Data-Processing/actions/workflows/CI_CD.yml)

# PySpark Data Processing
## PySpark is used to perform data processing on a large dataset with at least one Spark SQL query and one data transformation. The project's emphaisis is on Data processing functionality, use of Spark SQL and transformations, and the CI/CD pipeline.

<img width="463" alt="Screenshot 2024-11-03 at 7 55 33 PM" src="https://github.com/user-attachments/assets/27361169-78fa-4bfa-8f6d-6a3187c8901f">

## Structure
The `python_library` directory contains `my_tool.py` which contains all the necessary functions including `load` to transform and load local raw data from a `.csv` to a SQLite database, and `crud_query.py` to perform simple SQL operations. The files serve as a template to be customized for your own data project, and `main.py` is used for testing of the complete operations prior to conversion to a command line tool.

## Successful SQL Operations
<img width="1071" alt="Screenshot 2024-10-20 at 8 30 17 PM" src="https://github.com/user-attachments/assets/165c22af-3ddb-4b20-b66e-7adcd54a13a3">

### Core Files of the Repo:
* `python_library.py`
    - `transform_load.py`
    - `crud_query.py`
    - `requirements.txt`
    - `Makefile`
* `sqlite` rust folder
    - `library.rs`
    - `main.rs`
* `Cargo.toml`
* CI/CD pipeline
* `README.md`