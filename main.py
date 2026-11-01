
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found. Check your .env file.")
    exit()

client = genai.Client(api_key=api_key)


def generate_content(prompt):
    try:
        print("\nGenerating content... Please wait.\n")

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        if response.text:
            print("\n========== AI GENERATED RESULT ==========\n")
            print(response.text)
        else:
            print("No content generated.")

    except Exception as e:
        print("Error:", e)


def notes_generator():
    print("\n===== AI NOTES GENERATOR =====")

    subject = input("Enter Subject: ")
    topic = input("Enter Topic: ")

    prompt = f"""
    Generate simple and exam-oriented study notes.

    Subject: {subject}
    Topic: {topic}

    Include:
    1. Introduction
    2. Definition
    3. Important Concepts
    4. Features
    5. Examples
    6. Conclusion

    Use simple language and proper headings.
    """

    generate_content(prompt)


def question_generator():
    print("\n===== AI QUESTION GENERATOR =====")

    subject = input("Enter Subject: ")
    topic = input("Enter Topic: ")

    prompt = f"""
    Generate practice questions for students.

    Subject: {subject}
    Topic: {topic}

    Include:
    1. Five Multiple Choice Questions with four options and answers.
    2. Five Short Answer Questions.
    3. Three Long Answer Questions.

    Use simple academic language.
    """

    generate_content(prompt)


def writing_enhancer():
    print("\n===== AI WRITING ENHANCER =====")

    print("Enter your academic text:")
    academic_text = input("> ")

    prompt = f"""
    Rewrite the following text in formal academic language.

    Improve:
    1. Grammar
    2. Sentence Structure
    3. Clarity
    4. Coherence
    5. Readability
    6. Academic Tone

    Preserve the original meaning.
    Do not add unsupported facts.

    Original Text:
    {academic_text}
    """

    generate_content(prompt)


def research_generator():
    print("\n===== AI RESEARCH IDEA GENERATOR =====")

    subject = input("Enter Subject Domain: ")
    keywords = input("Enter Keywords: ")
    interest = input("Enter Research Interest: ")

    prompt = f"""
    Act as an academic research assistant.

    Subject Domain: {subject}
    Keywords: {keywords}
    Research Interest: {interest}

    Generate:

    1. Possible Research Areas
    2. Five Interdisciplinary Research Topics
    3. Research Objectives
    4. Preliminary Research Outline
    5. Suggested Research Methodology
    6. Expected Outcomes

    Use simple academic language and proper headings.
    """

    generate_content(prompt)


while True:

    print("\n====================================")
    print("          AI STUDY ASSISTANT")
    print("====================================")

    print("\nChoose an option:\n")

    print("1. AI Notes Generator")
    print("2. AI Question Generator")
    print("3. AI Writing Enhancer")
    print("4. AI Research Idea Generator")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        notes_generator()

    elif choice == "2":
        question_generator()

    elif choice == "3":
        writing_enhancer()

    elif choice == "4":
        research_generator()

    elif choice == "5":
        print("\nThank you for using AI Study Assistant!")
        break

    else:
        print("\nInvalid choice. Please select 1-5.")
