# Campus Compass Database Schema

[![GitHub version](https://badge.fury.io/gh/CampusCompass%2FCampusCompass.svg)](https://badge.fury.io/gh/CampusCompass%2FCampusCompass)

## Overview

This document outlines the database schema for the Campus Compass project. The schema defines the structure of the database used to store information related to educational institutions, including their names, locations, financial data, and control status. This schema is designed to help organize and manage data efficiently for the project.

## Tables

The database consists of the following tables:

1. **`school` Table**
    - Stores information about educational institutions.

    | Column Name   | Data Type | Description                  |
    |---------------|-----------|------------------------------|
    | `id`          | INTEGER   | Primary key                  |
    | `name`        | TEXT      | School name (unique)         |
    | `url`         | TEXT      | School website URL           |

2. **`location` Table**
    - Stores location data for each school.

    | Column Name   | Data Type | Description                  |
    |---------------|-----------|------------------------------|
    | `id`          | INTEGER   | Primary key                  |
    | `school_id`   | INTEGER   | Foreign key to school        |
    | `city`        | TEXT      | City                         |
    | `zipcode`     | TEXT      | ZIP code                     |
    | `state`       | TEXT      | State                        |
    | `region`      | TEXT      | Region                       |
    | `locale`      | TEXT      | Locale                       |

3. **`finance` Table**
    - Stores financial data for each school, including costs and tuition.

    | Column Name   | Data Type | Description                  |
    |---------------|-----------|------------------------------|
    | `id`          | INTEGER   | Primary key                  |
    | `school_id`   | INTEGER   | Foreign key to school        |
    | `year`        | DATE      | Year of financial data       |
    | `cost4a`      | REAL      | Cost for category 4a         |
    | `in_state_tuition`  | REAL | In-state tuition             |
    | `out_state_tuition` | REAL | Out-of-state tuition         |

4. **`control` Table**
    - Stores control status and degree information for each school.

    | Column Name          | Data Type | Description                  |
    |----------------------|-----------|------------------------------|
    | `id`                 | INTEGER   | Primary key                  |
    | `school_id`          | INTEGER   | Foreign key to school        |
    | `under_investigation` | BOOLEAN   | Under investigation status  |
    | `predominant_deg`    | TEXT      | Predominant degree awarded  |
    | `highest_deg`        | TEXT      | Highest degree awarded      |
    | `control`            | TEXT      | Control of institution      |

## Contributing

If you plan to contribute to the database schema or have suggestions for improvements, please open an issue or create a pull request in the project repository.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jonathjd/CampusCompass/blob/main/LICENSE) file for details.

## Contact

For questions or support, please contact [Jonathan Dickinson](mailto:jon.dickinson17@gmail.com).

This README outlines the database schema for the CampusCompass project, providing an overview of the tables and their structures. You can customize it with specific details or additional sections as needed for your project.
