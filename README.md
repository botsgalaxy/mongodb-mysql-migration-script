# MongoDB to MySQL Migration Script

This script is designed to migrate data from a MongoDB collection to a MySQL table. It includes logging for easy monitoring of the migration process.

## Prerequisites

Before running the script, ensure that the following prerequisites are met:

1. **Python 3.x** is installed.
2. **MongoDB** and **MySQL** servers are accessible and running.
3. Required Python packages are installed.

### Installing Dependencies

Install the required Python packages using the command:

```bash
pip3 install -r requirements.txt
```

## Configuration

### The script requires configuration for connecting to both MongoDB and MySQL databases.

MongoDB Configuration:

- Connection URI
- Database name
- Collection name

MySQL Configuration:

- Host
- User
- Password
- Database name
- Insert query and fields

### Running the Script

Once the configurations are set, run the migration script using the following command:

```bash
python3 main.py
```
