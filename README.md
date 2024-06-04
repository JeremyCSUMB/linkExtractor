# Link Extractor

## Description

This script retrieves discussion posts and replies from a specified Canvas course discussion topic, extracts LinkedIn URLs (handling cases where `https://` is omitted), fetches the user's email addresses, and compiles the data into a CSV file. The CSV file will contain three columns: `user_name`, `email`, and `linkedin_url`.

## Prerequisites

Ensure you have Python 3 installed on your machine. You will also need to install the required Python libraries listed below.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/jeremyCSUMB/linkExtractor
   cd linkExtractor
   ```

2. **Install the Required Python Libraries:**
   ```sh
   pip install canvasapi pandas beautifulsoup4 python-dotenv
   ```

3. **Create a `.env` File:**
   Create a file named `.env` in the same directory as your script and add the following lines. Replace `YOUR_API_KEY` with your actual Canvas API key.
   ```plaintext
   CANVAS_API_URL=https://cti-courses.instructure.com
   CANVAS_API_KEY=YOUR_API_KEY
   ```

## Usage

1. **Update Course and Discussion Topic IDs:**
   Open the script file `linkExtractor.py` and update the `course_id` and `discussion_topic_id` variables with the appropriate values from your Canvas course.

2. **Run the Script:**
   ```sh
   python3 linkedin_link_extractor.py
   ```

3. **Output:**
   The script will generate a `linkedin_urls.csv` file in the same directory, containing three columns: `user_name`, `email`, and `linkedin_url`.
