# 🤖 AI Chatbot Utility (Streamlit + OpenAI)

## 📌 Overview
This project is a reusable AI chatbot module built using Streamlit and OpenAI's Chat Completion API.
It is designed so developers can plug it into any app — student dashboards, placement systems, EcoServe,
recommendation platforms, etc.

## 🚀 Features
- Intelligent conversation powered by GPT-4
- Clean Streamlit UI
- Modular architecture (logic + UI)
- Compatible with OpenAI v1.0+
- Works with .env API key
- Easily customizable

## 📁 Structure
ChatBot/
│── app.py
│── chatbot.py
│── .env
│── requirements.txt
│── README.md

where  requirements.txt - 
streamlit
python-dotenv
openai>=1.0.0

## 🔐 Setup
1. Install dependencies:
pip install -r requirements.txt

2. Add your OpenAI key in `.env`:


OPENAI_API_KEY=your_key_here

3. Run the app:


streamlit run app.py


## 🌍 Use in EcoServe
This chatbot will serve as an Eco Assistant helping users:

- Track eco-friendly habits
- Learn sustainability tips
- Get personalized recommendations
- Understand their EcoScore
- Navigate the platform
- Improve environmental contribution

## 📜 License
MIT
│── .env                   # API key
│── README.md
