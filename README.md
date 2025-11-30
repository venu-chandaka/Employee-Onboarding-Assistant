# 🚀 Employee Onboarding Assistant

**Capstone Project for 5-Day AI Agents Intensive Course with Google**

A smart AI-Powered Onboarding Assistant built using **Google Gemini 2.5 Flash**, featuring intelligent routing agents (HR, IT, Compliance) and a modern **Streamlit Chat UI**.

---

## 👨‍💻 Team Members
- Chandaka Venu  
- Karthikeya Reddy  
- Mandre Vamshi Krishna  
- Savio  

---

## 🧠 Project Overview
This project simulates a real-world **employee onboarding assistant** that:  
- Understands user queries  
- Automatically routes questions to the correct department (HR / IT / Compliance)  
- Uses tool functions to fetch dynamic responses  
- Provides a clean, modern chat interface similar to ChatGPT  
- Runs fully locally using **Streamlit**

---

## 🔥 Key Features
### ✔️ AI Routing System
Automatically identifies the category of a user's message and routes it to the correct department.

### ✔️ Department Agents
- **HR Agent** → Leave balance, salary, HR queries  
- **IT Agent** → Laptop issues, login problems, software support  
- **Compliance Agent** → Company policies, training status  
- **General AI Chat** → For all other topics  

### ✔️ Modern Chat UI
- ChatGPT-like interface  
- User + bot message bubbles  
- Sidebar navigation  
- Clean blue theme  

### ✔️ Secure API Key Handling
- Uses `.env` file (not uploaded to GitHub)  

---

## 🛠️ Tech Stack

| Component      | Technology                |
|----------------|--------------------------|
| Language       | Python 3.x               |
| UI             | Streamlit                |
| AI Model       | Google Gemini 2.5 Flash  |
| API            | Google Generative AI SDK |
| Environment    | Dotenv                   |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Employee-Onboarding-Assistant.git
cd Employee-Onboarding-Assistant
```
2️⃣ Install Dependencies
bash
Copy code
```
pip install -r requirements.txt
```
3️⃣ Create a .env file
Create .env inside the project folder:

env
Copy code
GOOGLE_API_KEY=your_api_key_here
⚠️ Do NOT expose your API key in GitHub.

4️⃣ Run the App
bash
Copy code
streamlit run app.py
📸 Screenshots
🟦 Home Screen


🟦 Chat Interface


🗂️ Project Structure
bash
Copy code
📁 Employee-Onboarding-Assistant
│── app.py                # Main application
│── README.md             # Documentation
│── .gitignore            # Prevents uploading API keys
│── .env                  # LOCAL ONLY (not uploaded)
🧪 Example Queries to Test
Department	Example User Input
HR	"How many leaves are left?"
IT	"My laptop is not working."
Compliance	"Is my training completed?"
General	"Explain onboarding process."

🏆 Course Details
Developed as part of the:
Google AI Agents Intensive – 5-Day Bootcamp (2025)
Instructor: Google Developer Relations Team

🤝 Contributors
Special thanks to everyone who worked on this project:

⭐ Karthikeya Reddy –Lead Developer

⭐ Venu Chandaka – Developer

⭐ Mandre Vamshi Krishna – Developer

⭐ Savio – Developer
