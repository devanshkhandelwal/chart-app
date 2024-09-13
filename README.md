# Next.js and Django Dashboard Application

## Overview

This project is a web application featuring a basic dashboard page with four types of charts: Candlestick, Line Chart, Bar Chart, and Pie Chart. The frontend is built using Next.js, and the backend is powered by Django. The data for the charts is hardcoded in the Django API and retrieved by the Next.js frontend to dynamically render the charts.

## Project Structure

- `frontend/` - Contains the Next.js application.
- `backend/` - Contains the Django API backend.

## Prerequisites

Ensure you have the following installed:

- Node.js (for Next.js frontend)
- Python (for Django backend)
- pip (Python package manager)

## Frontend (Next.js)

### Setup

1. Navigate to the `frontend/` directory:

   ```bash
   cd frontend
   ```

2. Install the required dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

4. Access the application at `http://localhost:3000`.

### Libraries Used

- Next.js
- Chart.js (or any other charting library used)
- Axios (for API calls)

## Backend (Django API)

### Setup

1. Navigate to the `backend/` directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations and run the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Libraries Used

- Django

## Approach

1. **Frontend**: Implemented using Next.js. The frontend fetches data from the Django API and renders the charts using Chart.js (or another chosen charting library). API calls are made using Axios.

2. **Backend**: Built with Django. Created API endpoints to serve hardcoded data for each chart type. The data structure adheres to what is expected by the charting library.

## Additional Information

- **Error Handling**: The frontend gracefully handles API errors by displaying appropriate messages.
- **UI/UX**: Designed a clean and responsive dashboard for an intuitive user experience.

## Running the Application

1. Start the Django backend server as described above.
2. Start the Next.js frontend server as described above.
3. Open the application in your browser to view the dashboard.
