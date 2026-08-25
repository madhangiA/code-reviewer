# 🤖 AI Code Reviewer using Generative AI

An **AI-powered code review assistant** that analyzes source code using **Gemini 2.5 Flash**, identifies bugs and code-quality issues, provides improvement suggestions, generates corrected code, and creates downloadable PDF reports.

## ✨ Features

* 🔍 AI-powered code analysis
* 🐞 Bug and issue detection
* 📊 Code Quality Score (0–10)
* 🚨 Severity classification — Critical, High, Medium, Low
* 💡 Code improvement suggestions
* 🛠️ Automatically generated corrected code
* 📄 Downloadable PDF review reports
* 🌐 Multi-language support

### Supported Languages

**Python | Java | JavaScript | C++ | SQL**

---

## 🏗️ Architecture

```text
User
  ↓
Streamlit UI
  ↓
Prompt Generation
  ↓
Gemini 2.5 Flash
  ↓
Code Analysis
  ↓
Review Processing
  ↓
┌───────────────────┬──────────────────┐
│ Review Results    │ PDF Report       │
│ & Fixed Code      │ Generation       │
└───────────────────┴──────────────────┘
```

---

## 🛠️ Tech Stack

| Layer          | Technology       |
| -------------- | ---------------- |
| UI             | Streamlit        |
| Backend        | Python           |
| AI Model       | Gemini 2.5 Flash |
| AI Integration | Gemini API       |
| PDF Generation | ReportLab        |

---

## 🔄 How It Works

1. Select the programming language.
2. Enter or paste your source code.
3. Submit the code for review.
4. Gemini analyzes the code.
5. The application displays:

   * Code quality score
   * Bugs and issues
   * Severity
   * Explanations
   * Suggestions
   * Corrected code
6. Generate and download the PDF review report.

---

## 📊 Example Review

```text
Code Quality Score: 8.5 / 10

Severity: Medium

Issue:
Missing exception handling.

Suggestion:
Add appropriate exception handling to improve
application reliability.

Fixed Code:
<AI-generated improved code>
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/AI-Code-Reviewer.git
cd AI-Code-Reviewer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add application screenshots here:

```markdown
![AI Code Reviewer](screenshots/code-review.png)
```

---

## 🔮 Future Enhancements

* GitHub Pull Request integration
* Automated code review for repositories
* Code diff analysis
* Unit test generation
* Code complexity analysis
* Review history
* Docker & cloud deployment
* CI/CD integration
* Multi-agent code review

---

## 🎯 Key Learning

This project demonstrates practical implementation of:

**Generative AI • LLM Integration • Prompt Engineering • Gemini API • Python • Streamlit • AI-based Code Analysis • PDF Generation**

---

## 👩‍💻 Author

**Madhangi A**
Java Full Stack Developer | Generative AI Developer | AI & LLM Enthusiast

⭐ If you find this project useful, consider starring the repository!
