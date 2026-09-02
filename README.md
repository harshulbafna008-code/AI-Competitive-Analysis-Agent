# 📊 Competitive Analysis Agent

A multi-agent AI system that researches any company using live web search and generates a structured competitive analysis report — built with CrewAI, Gemini, and Streamlit.

![Demo](demo_screenshot.png)

## How it works
1. **Researcher Agent** — searches the web in real time (Tavily API) for company info, pricing, and competitors
2. **Analyst Agent** — synthesizes findings into a structured SWOT-style markdown report
3. **Streamlit UI** — enter a company name, get a live-generated report, download as markdown

## Tech Stack
- **CrewAI** — multi-agent orchestration
- **Google Gemini** — LLM reasoning
- **Tavily API** — real-time web search
- **Streamlit** — interactive UI
- **Python**

## Setup
\`\`\`bash
cd competitive-analysis-agent
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
cp .env.example .env       # add your API keys
streamlit run app.py
\`\`\`

## CLI version
\`\`\`bash
python -m src.main
\`\`\`

## Future Improvements
- PDF export
- Confidence scoring on extracted data points
- Multi-company side-by-side comparison
