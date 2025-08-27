# AI-Document-Insight-Tool 🚀

A lightweight yet powerful full-stack web application that turns your PDF résumés into concise, AI-generated insights.

<img width="952" height="444" alt="image" src="https://github.com/user-attachments/assets/48bcbfad-67a4-44b0-b6c7-213b5be19bc9" />


---

## 📌 Overview
AI-Document-Insight-Tool lets you drag-and-drop any PDF résumé, instantly receive an AI-powered summary, and keep a searchable history of every upload.  
Built with **FastAPI**, **React**, and **Sarvam AI**, it gracefully falls back to keyword extraction if the AI service is unavailable—so you’re never left without insight.

---

## ✨ Features
| Feature | Description |
|---------|-------------|
| 📄 **PDF Upload** | Drag-and-drop résumés via a clean React UI. |
| 🧠 **AI Summarization** | Leverages Sarvam AI to extract key points (skills, experience, education). |
| 🛡️ **Fallback Analysis** | If AI fails, auto-generates the top-5 most frequent meaningful keywords. |
| 🗄️ **Persistent History** | SQLite keeps every upload & its summary—browse & search in the “History” tab. |
| ⚡ **Modern Stack** | FastAPI backend, React frontend, RESTful JSON API. |

---

## 🏗️ Architecture
```text
+--------------------+      +---------------------+       +---------------------+
|   React Frontend   | <--> |   FastAPI Backend   | <----> |   Sarvam AI API     |
+--------------------+      +---------------------+       +---------------------+
           |                          |                           |
           |        SQLite Database    |                           |
           +--------------------------+---------------------------+
