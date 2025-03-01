import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from textblob import TextBlob

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Missing Google API Key. Please check your .env file.")
else:
    chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)

st.title(" AI Roadmap Generator")

skill = st.text_input("🔍 Enter a skill to generate its career roadmap:")

def correct_spelling(text):
    return str(TextBlob(text).correct())

if st.button("Generate Roadmap"):
    if skill:
        skill = correct_spelling(skill)  
        
        st.info(f"Generating roadmap for **{skill}**... Please wait!")
        
        prompt = f"""
        You are an expert mentor and learning strategist. Your task is to provide a **step-by-step roadmap** for mastering **{skill}**.
        Ensure it includes fundamental concepts, learning resources, hands-on projects, common mistakes to avoid, and career applications.

        ### **1. Introduction**
        - Why is **{skill}** important in today's industry?
        - Key **use cases and applications**.

        ### **2. Learning Roadmap (Beginner → Advanced)**
        #### **Beginner Level**
        - Core concepts to learn.
        - Best beginner-friendly resources (books, websites, courses).
        - Simple hands-on exercises.

        #### **Intermediate Level**
        - Advanced concepts, real-world projects, common challenges.

        #### **Advanced Level**
        - Mastery-level knowledge, production applications, open-source contributions.

        ### **3. Essential Tools & Technologies**
        - List the most important **tools, frameworks, and software**.

        ### **4. Hands-on Projects**
        - Recommend **3-5 real-world projects** with links to **datasets, APIs**.

        ### **5. Common Mistakes & How to Avoid Them**
        - Identify common pitfalls and provide solutions.

        ### **6. Career Opportunities & Industry Insights**
        - Relevant job roles, career paths, future trends.

        ### **7. Next Steps & Continuous Learning**
        - Communities, blogs, newsletters to stay updated.
        """

        try:
            response = chat_model.invoke([HumanMessage(content=prompt)])
            st.success(f"✅ Career roadmap for **{skill}** generated successfully!")
            st.write(response.content)
        except Exception as e:
            st.error("❌ Failed to generate a roadmap. Please try again.")
            st.write(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter a skill.")
