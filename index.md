from pathlib import Path

# Set the content of the index.md based on the user's poster content
index_md_content = """
# Fast Break to Las Vegas: A Market Driven Approach to NBA Franchise Relocation

## Introduction
The NBA is rapidly evolving in terms of viewership, fan engagement, and revenue growth. However, some franchises are falling behind in competitiveness and market potential. This project investigates the strategic relocation of an underperforming NBA franchise to Las Vegas, utilizing data-driven decision-making and modern IT tools.

## Background & Motivation
This project stems from the growing conversations around NBA expansion and relocation. With Las Vegas emerging as a major sports hub and the league emphasizing market performance, there's a unique opportunity to propose a model for moving a franchise. Personally, it blends my passion for sports management and analytics.

**Elevator Pitch (2-min Video Coming Soon)**

## Methodology
- **Data Collection:** Gathered franchise revenue, attendance, social media engagement, and market data from public sources like Basketball Reference, Statista, and census data.
- **Tools Used:** Python (Pandas, Matplotlib), Streamlit, Canva, Excel
- **Approach:**
  - Identified a relocation candidate (e.g., New Orleans Pelicans)
  - Analyzed Las Vegas’s market appeal
  - Modeled fanbase impact and marketing opportunities
  - Built a dashboard using Streamlit to showcase findings

## Results & Findings
- Las Vegas ranks high in:
  - Tourism (40M+ visitors/year)
  - Lack of NBA competition
  - Proven success with NHL & NFL franchises
- Streamlit Dashboard: [nbarelocationcapstone.streamlit.app](https://nbarelocationcapstone.streamlit.app)
- Forecast: Boosted revenue, stronger fanbase, enhanced NBA branding

## Discussion & Future Work
- **Lessons Learned:**
  - Importance of location-based revenue modeling
  - Fan engagement now includes digital channels
- **Limitations:**
  - Assumes willing ownership and NBA approval
  - Doesn’t factor legal/political hurdles
- **Next Steps:**
  - Interview stakeholders
  - Simulate relocation for other cities (e.g., Seattle)

## Feedback
Please leave your comments or suggestions at:
📧 [ct.taber.capstone@gmail.com](mailto:ct.taber.capstone@gmail.com)

## Acknowledgments
Special thanks to:
- Professor Ford for guidance
- CSUCI Computer Science & Business programs
- Canva & Streamlit communities
"""

# Save the content as a Markdown file
index_md_path = Path("/mnt/data/index.md")
index_md_path.write_text(index_md_content)

index_md_path
