from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

resume_text = """
ABISHEK VP
Senior Software Engineer – Platform Engineering, Security Integrations & Automation
Portfolio: https://abishek.in

SUMMARY
Platform-focused Software Engineer with experience building secure automation workflows, cloud and identity integrations, and developer-centric platform features for cybersecurity products. Skilled in Python, Django, Terraform, Jenkins, Azure AD, Google Workspace, and DevOps tool integration. Winner of Smart India Hackathon 2024. Strong background in product development, security-driven engineering, and mentoring.

TECH STACK
Backend: Python, Django, FastAPI, REST APIs
Automation: Selenium, Playwright, BeautifulSoup
Platform & DevOps: Terraform, Jenkins, Ansible, Chef, Puppet
Cloud & Identity: Azure AD, Google Workspace, LDAP, OAuth, SAML
Frontend: React, Ember.js, JavaScript, HTML, CSS, AJAX
Tools: GitHub, VS Code, Figma, Postman
Domains: Cybersecurity, Secure Automation, Platform Engineering

EXPERIENCE
Software Engineer – Securden (Aug 2024 – Present)
- Built browser extension-based secure credential automation modules
- Integrated Jenkins, Terraform, Ansible, Chef, Puppet into platform
- Implemented Azure AD and Google Workspace integration
- Developed secure REST APIs and internal automation tooling

Software Engineer – DAAT (2023 – 2024)
- Developed internal SaaS tooling for data automation and reporting
- Built backend modules using Python + Django
- Deployed projects using CI/CD pipelines

Software Engineer – ROOK Software (2022 – 2023)
- Built full-stack applications with Django + React
- Managed deployments and client delivery

HACKATHON WIN
Winner – Smart India Hackathon 2024
Project: GrantBase.gov.in – Real-time research grant aggregation platform using Python web scraping and alerting engine.

LEADERSHIP
- Conducted placement training on web dev, GitHub, Figma
- Mentored juniors on projects and hiring preparation

EDUCATION
B.Tech – Computer Science Engineering, 2024
"""

styles = getSampleStyleSheet()
story = [Paragraph(line, styles["BodyText"]) for line in resume_text.split("\n")]

file_path = "/mnt/data/Abishek_Resume.pdf"
doc = SimpleDocTemplate(file_path)
doc.build(story)

file_path
