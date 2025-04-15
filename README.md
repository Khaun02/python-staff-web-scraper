# Scholarship Outreach Automation Tool

A Python-based automation tool for scraping and filtering administrative staff contact data from high school websites to support targeted scholarship outreach.

This project was developed in collaboration with Madison College's NSF S-STEM Scholarship program and helped streamline communication with over 300 relevant faculty and staff across six local high schools.

---

## Features

- Scrapes staff directories from multiple high school websites using Selenium
- Filters contacts based on relevant roles (e.g., counselor, principal, admin)
- Outputs a structured `.csv` file for easy mass outreach
- Designed to assist real-world educational programs with automation and efficiency

---

## Technologies Used

- Python 3
- Selenium
- pandas
- ChromeDriver

---

## File Structure

scholarship-outreach-automation/ ├── main.py # Main script to run the scraper ├── chromedriver # Your ChromeDriver executable (not included) ├── s-stem_school_contacts.csv # Generated output file └── README.md

---

## How to Use

1. Clone this repository:

git clone https://github.com/yourusername/scholarship-outreach-automation.git cd scholarship-outreach-automation

2. Install required libraries:

pip install selenium pandas

3. Download the correct version of ChromeDriver:
   https://sites.google.com/chromium.org/driver/

   Place the `chromedriver` file in the project folder.

4. Run the script:

python main.py

5. The contact data will be saved in:

s-stem_school_contacts.csv

---

## Example Output

| Name        | Role       | Email               | School                  |
|-------------|------------|---------------------|--------------------------|
| Jane Doe    | Counselor  | jdoe@school.org     | East High School         |
| John Smith  | Principal  | jsmith@school.org   | La Follette High School  |

---

## License

This project is intended for educational use and internal outreach efforts only.  
Not affiliated with or endorsed by any school district listed.

---

## Author

**Shaun Khang**  
Created in collaboration with the Madison College S-STEM Scholarship initiative.