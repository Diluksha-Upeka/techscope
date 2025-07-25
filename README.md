# Techscope

Techscope is a full-stack web application that combines a Python backend and a React frontend. It is designed to provide a modern, scalable, and maintainable platform for technology-related data management and presentation.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Structure

```
techscope/
├── techscope-backend/   # Python backend (API, database, scraping, etc.)
├── techscope-frontend/  # React frontend (user interface)
└── README.md            # Project documentation
```

---

## Features
- Modern React frontend for a responsive user experience
- Python backend with RESTful API, database integration, and scraping capabilities
- Modular and extensible codebase
- Easy local development and deployment

---

## Prerequisites

- [Node.js](https://nodejs.org/) (v16 or higher recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- [Python 3.10+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

---

## Getting Started

### Backend Setup
1. Open a terminal and navigate to the backend directory:
   ```sh
   cd techscope-backend
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure environment variables as needed (see `.env.example` if available).
5. Run the backend server:
   ```sh
   python main.py
   ```

### Frontend Setup
1. Open a new terminal and navigate to the frontend directory:
   ```sh
   cd techscope-frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend development server:
   ```sh
   npm start
   ```
4. The app will be available at [http://localhost:3000](http://localhost:3000)

---

## Usage

1. Ensure both backend and frontend servers are running.
2. Access the frontend in your browser at [http://localhost:3000](http://localhost:3000).
3. The frontend communicates with the backend API for data operations.

---

## Development

- Backend code: `techscope-backend/`
- Frontend code: `techscope-frontend/`
- Use pull requests for all changes.
- Follow code style and best practices for Python and React.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or support, please contact the project maintainer:

- GitHub: [Diluksha-Upeka](https://github.com/Diluksha-Upeka)

---


cd techscope-backend

.\venv\Scripts\Activate.ps1

uvicorn main:app --reload --port 8000

http://localhost:8000/docs