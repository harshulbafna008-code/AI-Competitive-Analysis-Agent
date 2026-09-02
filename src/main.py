import os
from dotenv import load_dotenv
from src.agent import build_crew

load_dotenv()

def main():
    company_name = input("Enter a company name to analyze: ").strip()
    if not company_name:
        print("Please enter a valid company name.")
        return

    crew = build_crew(company_name)
    result = crew.kickoff()

    print("\n\n=== FINAL REPORT ===\n")
    print(result)

    # Save to file
    with open(f"{company_name.replace(' ', '_')}_analysis.md", "w", encoding="utf-8") as f:
        f.write(str(result))
    print(f"\nReport saved to {company_name.replace(' ', '_')}_analysis.md")

if __name__ == "__main__":
    main()