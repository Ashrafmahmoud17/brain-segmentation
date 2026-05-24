🦷 Dental Clinic Management System
Python + Tkinter + SQLite | Full Desktop Application
📌 Overview

A complete desktop dental clinic management system built with Python and Tkinter. The system covers the full patient lifecycle — from registration and appointment scheduling to visit tracking, treatment recording, billing, and financial reporting — all backed by a local SQLite database.
🖥️ Application Screenshots
Screen 	Description
Login 	Secure username/password authentication
Dashboard 	Overview with live patient & visit stats
Patients 	Full patient records management
Appointments 	Interactive calendar with scheduling
Visits 	Daily visit tracking per doctor
Payments 	Invoice creation and billing
Patient History 	Full financial report per patient
🗂️ Project Structure

dental-clinic/
│
├── log_c.py                  # ✅ Main entry point (recommended)
├── db.py                     # Database connection manager
├── database.sql              # Database schema (all tables)
├── init_db.py                # Initialize the database
│
├── patients.py               # Patient management module
├── appointments.py           # Appointment calendar module
├── visits.py                 # Visit tracking module
├── payments.py               # Billing & invoices module
├── history_of_patients.py    # Financial history per patient
│
└── clinic.db                 # SQLite database file (auto-created)

⚙️ Requirements
Python Version

Python 3.8+

Libraries

All libraries are built into Python — no pip install needed:

tkinter      # GUI framework (built-in)
sqlite3      # Database (built-in)
datetime     # Date handling (built-in)
calendar     # Calendar widget (built-in)
re           # Phone validation (built-in)
pickle       # Not used in core app

🚀 Getting Started
Step 1 — Initialize the Database

Run this once to create all tables:

python init_db.py

Output:

Connected to SQLite ✅
Database Created ✅

Step 2 — Create Admin User

In db.py, the create_admin_user() function creates the default admin:

Username: admin
Password: admin123

Run it once:

python db.py

Step 3 — Launch the Application

python log_c.py

🗄️ Database Schema

patients          → Core patient records
appointments      → Scheduled appointments (linked to patients)
visits            → Actual clinic visits (linked to patients)
treatments        → Dental procedures per visit
bills             → Invoices per visit
bill_items        → Individual services per invoice
payments          → Payment transactions per bill
dental_chart      → Tooth status per patient
users             → System login credentials

Key Relationships

patients ──┬── appointments
           ├── visits ──┬── treatments
           │            └── bills ──┬── bill_items
           │                        └── payments
           └── dental_chart

All foreign keys use ON DELETE CASCADE — deleting a patient removes all their linked records automatically.
📋 Modules Guide
👥 Patients (patients.py)

    Add, update, delete patient records
    Fields: Name, Age, Gender, Phone, Address, Medical History
    Egyptian phone number validation (01[0125]XXXXXXXX)
    Live search by name
    Duplicate detection (same name + address)

📅 Appointments (appointments.py)

    Interactive monthly calendar view
    Color coding:
        🟢 Green = has appointments
        ⬜ Gray = empty day
        🔴 Red = 5+ appointments
    Smart patient name autocomplete
    Filter by status: Scheduled / Completed / Cancelled
    Visit types: General, Consultation, Follow-up, Emergency

🏥 Visits (visits.py)

    Record daily patient visits with doctor name
    Date format: YYYY-MM-DD
    Linked to patient records
    Sorted by date (newest first)

💳 Payments (payments.py)

    Create itemized invoices per visit
    Add multiple services with prices
    Track: Total amount / Paid amount / Remaining balance
    Payment methods: Cash / Card / Transfer
    Auto-calculates remaining balance

📜 Patient History (history_of_patients.py)

    Smart search with autocomplete dropdown
    Financial summary cards:
        Total treatment cost
        Total paid
        Remaining debt
    Three detailed tables:
        Bills history
        Treatment procedures
        Payment transactions

📊 Dashboard (log_c.py)

    Live stats with auto-refresh every 3 seconds
    Total Patients counter
    Today's Visits (falls back to last recorded date if no visits today)
    System Status indicator

🔐 Login Versions

The project has multiple login UI versions developed iteratively:
File 	Dashboard Style 	Stats
log_c.py 	Sidebar + Stats cards 	✅ Live auto-refresh
log_g.py 	Sidebar + Stats cards 	✅ Auto-refresh
log2.py 	Sidebar 	Static
login.py 	Card grid layout 	None
login1.py 	Simple buttons 	None

    Use log_c.py — it is the most complete version.

🎛️ Configuration
Change Database File

In db.py:

conn = sqlite3.connect("clinic.db")   # Change filename here

Change Auto-Refresh Rate

In log_c.py:

dash.after(3000, auto_refresh)   # 3000ms = 3 seconds

Change Default Admin Credentials

In db.py:

username = "admin"
password = "admin123"

🔧 Common Issues & Fixes
"No module named tkinter"

# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk

Database not found

python init_db.py   # Run this first

Stats showing 0 visits

The visit date must be stored as YYYY-MM-DD. Check that the date field in the Visits form matches today's date format.
👤 Author

Ashraf Mahmoud Computer Sciences — New Mansoura University
📄 License

This project is for educational purposes.
