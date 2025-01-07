# Twitter Replica Using Python and MongoDB

## General Overview

This project simulates a basic Twitter-like functionality using Python and MongoDB. It is divided into two phases:

1. **Building the Document Store**: 
   - Takes a JSON file as input and constructs a MongoDB collection.
   - Creates a database named `291db` with a collection of tweets.
   - Requires the input of a JSON file name and the port number where the MongoDB server is running.

2. **Operating the Document Store**:
   - Connects to the `291db` database.
   - Provides a menu-driven interface for users to interact with the database.
   - Features include:
     - Searching for tweets or users.
     - Listing top tweets and users based on specific metrics.
     - Composing new tweets.
     - Exiting the program.

---

## User Guide

### Functionalities

1. **Search for Tweets**:
   - Input a keyword or multiple keywords to display a list of tweets containing the keywords.
   - Select a tweet by user ID to view its detailed information.
   - Quit the search by entering `q`.

2. **Search for Users**:
   - Input a keyword or multiple keywords to display users whose name contains the keywords.
   - Displayed information includes username, display name, and location.
   - Select a user by username to view detailed user data.
   - Quit the search by entering `q`.

3. **List Top Tweets**:
   - Select a field to rank tweets:
     - `1`: `retweetCount`
     - `2`: `likeCount`
     - `3`: `quoteCount`
   - Specify the number of top tweets to display.
   - View details such as tweet ID, date, content, username, and the chosen metric.

4. **List Top Users**:
   - Enter a number `n` to display the top `n` users based on `followersCount`.
   - View details of a selected user by username.
   - Quit by entering `q`.

5. **Compose a Tweet**:
   - Enter the content of the new tweet.
   - Metadata (username: `291user`, current date, other fields: zero or null) is automatically added.
   - Quit by entering `q`.

6. **Logout**:
   - Exit the program and return to the command line.

---

## Design

### Phase 1: Load JSON
- `load-json.py` creates the `291db` database with a `tweets` collection.
- Drops existing documents and populates the collection with data from the input JSON file.

### Phase 2: Main Interface
- Provides a menu for six functionalities:
  1. Search for tweets.
  2. Search for users.
  3. List top tweets.
  4. List top users.
  5. Compose a tweet.
  6. Logout.
- Returns to the main menu after each functionality.

---

## Testing Strategy

### Common Bugs and Solutions
- **Input Bugs**:
  - Tested various edge cases with capitalized letters, numbers, and special characters.
  - Used `try` and `except` clauses for invalid inputs.

- **Formatting Bugs**:
  - Adjusted output formatting to ensure proper display of information.

- **Function Call Errors**:
  - Verified function calls return to the correct sub-functions.

- **Variable Bugs**:
  - Ensured consistent variable usage when integrating different parts of the code.

- **Manipulating Field Values**:
  - Tested edge cases with extreme values for fields like `followersCount`.

---

## Group Work Strategy

### Team Contributions
- **Khym Nad**:
  - Responsibilities: Search for users, `load-json.py`, documentation, testing.
  - Time Allocated: 10 hours.

- **Akila Edirisinghe**:
  - Responsibilities: Search for tweets, `load-json.py`, testing, documentation.
  - Time Allocated: 10 hours.

- **Samuel Chan**:
  - Responsibilities: List top tweets, `load-json.py`, documentation, testing.
  - Time Allocated: 10 hours.

- **Andrew Zhang**:
  - Responsibilities: List top users, compose tweet, `load-json.py`, documentation, testing.
  - Time Allocated: 10 hours.

### Coordination
- Conducted on-campus meetings for collaborative debugging and integration.
- Used a Discord group chat for updates and discussions.

---

## Requirements

### Software
- Python 3.x
- MongoDB server

### Dependencies
Install required Python libraries using:
```bash
pip install -r requirements.txt
