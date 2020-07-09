# DBProj

Database Course Project -- 豆豉电影

## Usage

```bash
python -m DBProj  # With console output
pythonw -m DBProj # Without console output
```

### Extra scripts

`Initialization.py` can load database data from a given Microsoft Excel sheet. Handy for database initialization.

## Requirements

- Microsoft ODBC Driver 17 for SQL Server
- Qt 5 for Python (PyQt5)
- Other python package dependencies (see `requirements.txt`)
- A valid SQL Server database (see `config.yaml`)
- A secret `.env` file for database connection

## Feature

### Guests

- Receive daily global film recommendation on homepage
- Search films with filter and order conditions
- View detailed information of films, including detailed information of directors and casts
- Browse ratings and comments of films by users
- View user pages with personal information and comment histories, and jump to commented films
- Register as new users and enjoy more [↓](#Users)

### Users

- Receive personalized film recommendation
- Make comments and rate films
- View own comment history and jump to commented films
- Change personal information and password
- Contact us to become administrators and enjoy more [↓](#Administrators)

### Administrators

- Add administrator prefix on user name
- Manage film information (insert, modify, delete)
- Manage sub information (companies, genres, directors, casts)

## Author

This database course project is presented by Ding Y. W., Hang J. N., Yuan Y. L. and Liang J. C. as one project group.

### Acknowledgements

- Prof. Zheng W. G. and TAs for database course teaching
- [Douban/豆瓣](https://www.douban.com/) for precious film data
