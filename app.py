import streamlit as st
from dotenv import load_dotenv
from src.agent import run_analysis

load_dotenv()

st.set_page_config(page_title="Competitive Analysis Agent", page_icon="📊", layout="centered")

st.title("📊 Competitive Analysis Agent")
st.write("Enter a company name to generate a live, AI-researched competitive analysis report.")

company_name = st.text_input("Company name", placeholder="e.g. Notion, BMW, Stripe")

if st.button("Run Analysis", type="primary"):
    if not company_name.strip():
        st.warning("Please enter a company name.")
    else:
        with st.spinner(f"Researching {company_name} and generating report... this may take a minute."):
            try:
                report = run_analysis(company_name.strip())
                st.success("Analysis complete!")
                st.markdown(report)

                st.download_button(
                    label="Download Report (.md)",
                    data=report,
                    file_name=f"{company_name.strip().replace(' ', '_')}_analysis.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")