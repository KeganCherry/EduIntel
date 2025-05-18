
# EduIntel

EduIntel is a data-centric academic dashboard designed for students at **Tomball High School**. The application pulls data directly from the **Tomball ISD Home Access Center (HAC)** to provide detailed grade analysis, GPA calculations, course planning assistance, and predictive academic tools. This project focuses on giving students deeper visibility into their academic performance through structured data processing and intelligent features.

---

## Features

### Secure HAC Integration
Automates login to the Home Access Center using a headless browser. User credentials are never stored beyond session use, ensuring data privacy.

### Grade Data Extraction
Scrapes and structures grade data from all active courses, including averages, individual assignment scores, categories, and teacher information. This data is stored locally for fast access and future analysis.

### Local Grade Database
All extracted data is stored in a local SQLite database to allow offline access, historical tracking, and efficient querying.

### GPA Calculation & Forecasting
Calculates both unweighted and weighted GPA using customizable scales. Includes features for projecting GPA based on hypothetical future scores and missing assignments.

### What-If Grade Simulator
Allows students to simulate changes in individual grades or upcoming assignments to answer questions such as:
- "What do I need on my final exam to get an A in this class?"
- "If I fail this test, what will my semester average be?"

### AI-Based Course Counselor *(Planned)*
An AI assistant trained on the Tomball course catalog and academic pathways. Helps students understand elective choices, prerequisites, endorsement tracks, and long-term graduation planning.

### Academic Trends & Insights *(Planned)*
Future versions will visualize academic performance over time, highlight grade volatility, and provide custom insights about workload balance and risk areas.

### Themed for Tomball High School
The UI reflects school colors, mascots, and relevant terminology to make the experience familiar and tailored to THS students.

---

## Technical Stack

- **Python 3.11+** — Core logic and scraping
- **Playwright** — Headless browser automation for HAC login and scraping
- **SQLite + SQLAlchemy** — Lightweight, local database for grade data
- **Flet** — Cross-platform Python UI framework (Windows, Web, Mobile)
- **FastAPI** *(planned)* — For backend API services, especially for mobile/web deployment
- **HuggingFace Transformers / OpenAI GPT** *(planned)* — For AI counselor module

---

## Installation

### Prerequisites
- Python 3.11 or newer
- Node.js (required for Playwright browser setup)

### Setup Instructions

```bash
git clone https://github.com/yourusername/EduIntel.git
cd EduIntel

# Set up a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up Playwright browser
playwright install
```

---

## Running the App

```bash
python app.py
```

This will launch the local desktop app or browser interface. You will be prompted to log into HAC on the first run. After login, the app will retrieve your grades, store them locally, and present your dashboard.

---

## Roadmap

- [x] HAC login and scraper
- [x] Local database schema for storing grades
- [x] Initial UI with grade overview
- [ ] GPA calculator with weight support
- [ ] What-if grade simulator
- [ ] AI class planning assistant
- [ ] Longitudinal academic insights
- [ ] Web and mobile deployment

---

## License

This project is licensed under the [MIT License](./LICENSE). You are free to use, modify, and distribute the software with appropriate credit.

---

## Contributions

Contributions from Tomball High School students, alumni, or developers interested in educational tools are welcome. If you’d like to contribute a feature, fix a bug, or improve the documentation, feel free to open an issue or submit a pull request.
