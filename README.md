# GradeBoost
GradeBoost - Peer-to-Peer Tutoring Web App
Welcome to GradeBoost, the ultimate peer-to-peer tutoring platform designed to connect students with top-rated tutors for personalized learning experiences. Whether you're looking for a tutor to help you improve in a specific subject or want to share your expertise with others, GradeBoost provides an intuitive and efficient way to make it happen.

Features:
Student & Tutor Profiles: Detailed profiles for both students and tutors, including personal information, subject expertise, availability, and ratings.

Booking System: Seamlessly book custom_sessions with tutors based on availability and your schedule.

Onsite Tutoring: custom_sessions can be conducted on-campus (using school timetable integration) or off-campus (home tutoring with additional charges).

Tutor Ratings & Reviews: Students rate and review tutors after custom_sessions, and tutors' ratings are displayed prominently.

Payment System: Integrated payment options, including Orange Money and Mobile Money, for a secure and convenient transaction process.

Session Tracking & Progress: Students can track their progress and improvements based on their grades, feedback, and tutor comments.

Reporting & Moderation: A reporting system for students and tutors to flag any issues, misbehavior, or platform-related problems.

Admin Control Panel: Admins manage user accounts, oversee platform activity, handle disputes, and ensure smooth platform operation.

Video Conferencing Integration: Online custom_sessions are supported with video conferencing tools for remote learning.

Technologies Used:
Backend: Django (Python)

Frontend: React.js

Database: MySQL (Relational Database Management System)

Authentication: Django REST Framework (JWT Authentication)

Payment Integration: Orange Money, Mobile Money

APIs: Google Maps API (for home tutoring location sharing)

Version Control: Git, GitHub

Deployment: Docker, Nginx (for web server), and Gunicorn (for WSGI server)

Project Setup Instructions:
1. Clone the Repository:

git clone https://github.com/Romuald-DJAGNISIGNING/GradeBoost.git
cd GradeBoost
2. Backend Setup (Django)
Create a Virtual Environment:


python -m venv venv
source venv/bin/activate 
# On Windows, use `.venv\Scripts\activate`
Install Dependencies:


pip install -r requirements.txt
Create a MySQL Database:

Make sure MySQL is installed and running. Create a new database and update DATABASES in settings.py with your MySQL credentials.

Apply Migrations:


python manage.py makemigrations
python manage.py migrate
Create a Superuser for Admin Access:


python manage.py createsuperuser
3. Frontend Setup (React.js)
Install Frontend Dependencies:


cd frontend
npm install
Start the React Development Server:


npm start
The frontend will now be available at http://localhost:3000/.

4. Running the Development Server:
Once the backend and frontend are set up, you can start the Django development server:


python manage.py runserver
The backend will now be running at http://localhost:8000/.

5. Deployment:
For production, deploy your app using Docker, Nginx, and Gunicorn. Configuration files for these technologies can be found in the repository.

API Documentation:
The GradeBoost web app uses a RESTful API to handle user authentication, bookings, payments, and other operations. You can find the API documentation in the /docs folder. For easy integration with the frontend, we use the Django REST Framework.

Example Endpoints:
POST /api/auth/register/ - Register a new user (Student/Tutor)

POST /api/auth/login/ - User login

GET /api/tutors/ - Fetch list of available tutors

POST /api/custom_sessions/ - Book a tutoring session

POST /api/payments/ - Process payment for a session

GET /api/progress/ - Get student progress report

Contributing:
We welcome contributions to GradeBoost. If you have an idea for a feature or have found a bug, please follow these steps to contribute:

Fork the repository.

Create a new branch: git checkout -b feature-name

Make your changes and commit: git commit -am 'Add new feature'

Push to the branch: git push origin feature-name

Create a new pull request.

Please ensure that all code is properly documented, and consider writing tests for new features.

Licensing:
This project is licensed under the MIT License - see the LICENSE file for details.

Contact Information:
For any questions, feedback, or inquiries, feel free to reach out:

Email: support@gradeboost.com

GitHub: https://github.com/Romuald-DJAGNISIGNING/GradeBoost

Acknowledgments:
Django for the amazing web framework.

React.js for building dynamic and responsive user interfaces.

Google Maps API for location services.

Mobile Money and Orange Money for payment integrations.






# GradeBoost 

**Peer‑to‑Peer Tutoring Platform** — Cameroon Edition

**GradeBoost** connects students with qualified university tutors for in‑person (on‑campus or off‑campus) and virtual sessions. It features role‑based access, social login, mobile‑money payments, assignment handling, progress tracking, reporting, messaging, ratings, and admin moderation.

---

## 🚀 Features

### 1. Authentication & User Management
- **Register & Login** via:
  - **Username / Email (Gmail only)** / Phone + Password
  - **Google OAuth2** (optional; only Gmail accounts)
- **Custom User Model** (fields):
  - `email`, `phone_number`, `gender`, `role` (student/tutor/admin)
  - `profile_pic` (default if none uploaded)
  - `id_card` upload (mandatory for all)
  - `transcript` + `subjects` (tutors only)
  - `timetable` OR `latitude`+`longitude` (students only)
- **Admin** can:
  - Promote/demote users to/from `tutor` or `admin`
  - Suspend, warn, or delete accounts
  - Pay tutors manually

### 2. Session Booking
- **On‑campus**:  
  - Students upload their PDF timetable  
  - System auto‑assigns free classrooms
- **Off‑campus**:  
  - Students pin their home location on a **Leaflet.js** map (OpenStreetMap)  
  - Extra session fee applied

### 3. Assignments & Progress
- Tutors assign exercises/homework to students
- Students upload submissions via platform
- Tutors grade & comment
- Students view progress as charts (grade vs. time + tutor feedback)

### 4. Payments
- **Fixed session rate** (set by Admin) + **off‑campus extra fee**
- Students pay via:
  - **Orange Money Cameroon** API
  - **MTN Mobile Money Cameroon** API
- Admin triggers tutor payouts

### 5. Messaging & Notifications
- In‑app chat between students and tutors
- File attachments (images/docs)

### 6. Ratings & Reviews
- After each session, students rate tutors (1–5 stars) and leave feedback
- Tutor listings sorted by **average rating** (top first)

### 7. Reporting & Moderation
- Students & tutors submit misconduct reports
- Admin reviews, updates status (`Pending`, `In Progress`, `Resolved`, `Dismissed`)

### 8. Dashboards
- **Admin Dashboard**: user stats, session & payment overviews, reports, reviews  
- **Tutor Dashboard**: booked sessions, homework stats, earnings  
- **Student Dashboard**: upcoming sessions, assignment status, progress charts  

### 9. Media Handling
- **Uploads**:  
  - `media/profile_pics/`  
  - `media/id_cards/`  
  - `media/transcripts/`  
  - `media/timetables/`  
  - `media/assignments/`

---

## 📁 Project Structure

gradeboost-backend/ ├── gradeboost/ # Django project │ ├── settings.py # All settings (Leaflet, Allauth, MoMo, media, etc.) │ ├── urls.py # Root URLconf │ ├── wsgi.py, asgi.py │ └── validators.py # Gmail-only, phone validators │ ├── users/ # Authentication, profiles, roles ├── sessions/ # Session booking logic ├── assignments/ # Assignment models & views ├── progress/ # Student progress & charts ├── payments/ # Mobile money integrations & payment settings ├── messaging/ # Chat models & endpoints ├── reviews/ # Tutor rating & feedback ├── reports/ # Misconduct reports ├── dashboard/ # Role‑based dashboards ├── templates/ # HTML templates (login, location pickers, etc.) ├── static/ # Static files (CSS/JS) ├── media/ # User‑uploaded files ├── manage.py └── requirements.txt

yaml


---

## ⚙️ Installation & Setup

1. **Clone & install**
   ```bash
   git clone https://github.com/your-username/gradeboost-backend.git
   cd gradeboost-backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
Configure environment Create a .env file or export environment variables:

ini
Copier
Modifier
SECRET_KEY=<your-secret-key>
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=<google-client-id>
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=<google-client-secret>
ORANGE_MONEY_API_KEY=<orange-money-key>
MTN_MOBILE_MONEY_API_KEY=<mtn-money-key>
Migrate & create superuser


python manage.py migrate
python manage.py createsuperuser
Run the server


python manage.py runserver
Access

API root: http://localhost:8000/

Admin: http://localhost:8000/admin/

Leaflet map (set/view location):

http://localhost:8000/users/set-location/

http://localhost:8000/users/view-location/
