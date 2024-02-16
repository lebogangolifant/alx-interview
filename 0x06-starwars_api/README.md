# 0x06. Star Wars API

## Overview

This project contains a Node.js script (`0-starwars_characters.js`) that interacts with the Star Wars API to retrieve and print characters of a specified Star Wars movie. The script accepts the movie ID as a command-line argument and utilizes the `request` module for making HTTP requests to the API. Additionally, error handling is implemented to manage potential errors during the HTTP requests.

## Files

- **0-starwars_characters.js**: Contains the script to fetch and print characters of a Star Wars movie.

## Concepts Covered

- **RESTful API**: The script demonstrates interaction with a RESTful API, specifically the Star Wars API, to retrieve data related to Star Wars movies and characters.

- **Asynchronous Programming**: The implementation utilizes asynchronous programming techniques, such as callbacks or promises, to handle asynchronous HTTP requests for fetching character details.

- **Error Handling**: Error handling is implemented to handle potential errors during HTTP requests, ensuring robustness and reliability of the script.

## Usage

To test the `0-starwars_characters.js` script: 
- Make the script executable:
```bash
chmod +x 0-starwars_characters.js
```
- Run the script with the movie ID as a command-line argument:

```bash
./0-starwars_characters.js <movie_id>
```

Replace `<movie_id>` with the ID of the Star Wars movie for which you want to retrieve characters. This will print the names of characters from the specified movie.

