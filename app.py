import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Google Gemini AI Model
chat_model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

st.title("AI Career Path Generator")

skill = st.text_input("Enter a skill to generate its career roadmap:")

if st.button("Generate Roadmap"):
    if skill:
        prompt = f"""
       # CONTEXT:
        You are an expert mentor and learning strategist. Your task is to provide a **step-by-step roadmap** for mastering a specific skill. The roadmap should include **fundamental concepts, learning resources, hands-on projects, common mistakes to avoid, and career applications** of the skill.

        # GOAL:
        Help an individual systematically **learn, practice, and master** the skill **{skill}** from beginner to advanced levels. Ensure the roadmap is actionable and practical.

        # RESPONSE GUIDELINES:
        ### **1. Introduction**
        - Explain why **{skill}** is important in today's industry.
        - List the key **use cases and applications**.

        ### **2. Learning Roadmap (Beginner → Advanced)**
        Provide a structured **step-by-step** learning path:
        - **Beginner Level**  
        - Fundamental concepts to learn  
        - Best beginner-friendly resources (books, websites, courses, YouTube channels)  
        - Simple hands-on exercises  

        - **Intermediate Level**  
        - Advanced concepts and problem-solving approaches  
        - Real-world projects to build practical experience  
        - Common challenges and how to overcome them  

        - **Advanced Level**  
        - Mastery-level topics and specialized knowledge  
        - Building production-level applications or solving real-world problems  
        - Open-source contributions, certifications, and expert-level projects  

        ### **3. Essential Tools & Technologies**
        - List the most important **tools, frameworks, and software** required to work efficiently with **{skill}**.

        ### **4. Hands-on Projects**
        - Recommend **3-5 real-world projects** that help in applying the skill.
        - Provide links to **datasets, APIs, or problem statements** for practical implementation.

        ### **5. Common Mistakes & How to Avoid Them**
        - List common mistakes learners make and provide tips to **avoid pitfalls**.

        ### **6. Career Opportunities & Industry Insights**
        - How can someone turn **{skill}** into a career?  
        - Relevant job roles and career paths  
        - Emerging trends and future scope  

        ### **7. Next Steps & Continuous Improvement**
        - How to keep improving and staying updated?  
        - Communities, newsletters, blogs, and conferences to follow.  

        # OUTPUT:
        The response should be a **clear, structured, and actionable learning roadmap** to help someone effectively develop **{skill}**.
        """

        response = chat_model.invoke([HumanMessage(content=prompt)])
        st.write(response.content)
    else:
        st.warning("Please enter a skill.")
