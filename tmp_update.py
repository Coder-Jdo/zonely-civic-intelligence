import re

with open('templates/postcode.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the CTA that is ALREADY IN postcode.html
# Find the CTA (Starts with <div class="verdict-box" style="background: linear-gradient... and ends before FINAL VERDICT)
old_cta_regex = r'<div class="verdict-box" style="background: linear-gradient[^>]*?>.*?</div>'
match = re.search(old_cta_regex, text, flags=re.DOTALL)
if match:
    new_cta = '''{% set headline = "Want Your Area Analysed?" %}
{% set supporting_text = "Join the Zonely network to get detailed, real-time alerts and professional-grade civic intelligence on property transactions and development pipelines in " + code + "." %}
{% set bg_start = "var(--zonely-mid)" %}
{% set bg_end = "var(--zonely-blue)" %}
{% set btn_bg = "var(--zonely-accent)" %}
{% set button_text = "Request Access" %}
{% include "cta.html" %}'''
    # We only replace the first occurrence that looks like the CTA
    text = text.replace(match.group(0), new_cta)

# 2. Add Secondary CTA near Download area
# Look for <section class="card-solid ... Download as PDF ... </section>
download_section_regex = r'(<section class="card-solid[^>]*>.*?Download as PDF.*?</section>)'
match2 = re.search(download_section_regex, text, flags=re.DOTALL)
if match2:
    secondary_cta = match2.group(1) + '''

<div style="margin-top: 24px; text-align: center;">
  <div style="box-shadow: none; border: 1px solid var(--border); background: #ffffff; border-radius: 16px; padding: 24px; margin-top: 16px; text-align: left;">
    <h3 style="font-size: 16px; font-weight: 700; color: #1E4A7A; font-family: 'Inter', sans-serif; margin-bottom: 4px; margin-top: 0;">&#10024; Get a Custom Civic Intelligence Report</h3>
    <p style="font-size: 13px; color: #64748B; margin-bottom: 16px; font-family: 'Inter', sans-serif; line-height: 1.5; margin-top: 0;">Want Zonely coverage for your area? Request a custom report or early access for a different postcode.</p>
    <a href="https://forms.gle/1TwmamGaTaU2A3eW8" target="_blank" style="display: inline-flex; align-items: inherit; background: linear-gradient(90deg, #10B981, #059669); color: white; border-radius: 999px; padding: 10px 24px; font-size: 13px; font-weight: 700; text-decoration: none; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.2);">Request Coverage</a>
  </div>
</div>
'''
    text = text.replace(match2.group(1), secondary_cta)


with open('templates/postcode.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("postcode.html modified.")
