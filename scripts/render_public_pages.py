from pathlib import Path
import markdown
from jinja2 import Template

ROOT = Path('/root/.openclaw/workspace/projects/regina-lead-github-pages')
REPORTS = ROOT / 'reports'

PAGES = [
    {
        'source': 'regina_public_brief_plain_language_2026-03-12.md',
        'output': 'public-brief.html',
        'title': 'Public Brief',
        'kicker': 'Plain-language summary',
        'description': 'A plain-language overview of what changed, what did not, and what to watch next in Regina’s lead service connection story.'
    },
    {
        'source': 'regina_public_handout_2026-03-16.md',
        'output': 'public-handout.html',
        'title': 'Public Handout',
        'kicker': 'One-page summary',
        'description': 'A concise handout version of the main findings for public readers and sharing.'
    },
    {
        'source': 'regina_journalist_memo_2026-03-16.md',
        'output': 'journalist-memo.html',
        'title': 'Journalist Memo',
        'kicker': 'Media-ready framing',
        'description': 'A reporter-facing summary of the documentary story, key cautions, and best next questions.'
    },
    {
        'source': 'regina_claim_evidence_table_primary_2026-03-12.md',
        'output': 'claim-evidence.html',
        'title': 'Claim / Evidence Table',
        'kicker': 'Primary-source verification',
        'description': 'Primary-source claim mapping used to support publication-safe public wording.'
    },
    {
        'source': 'regina_decision_to_delivery_tracker_2026-03-16.md',
        'output': 'delivery-tracker.html',
        'title': 'Decision / Delivery Tracker',
        'kicker': 'Follow-through tracker',
        'description': 'A practical tracker for what was adopted, what delivery evidence exists, and what still needs verification.'
    },
    {
        'source': 'regina_health_burden_technical_appendix_2026-03-16.md',
        'output': 'technical-appendix.html',
        'title': 'Technical Appendix',
        'kicker': 'Support-layer method note',
        'description': 'A bounded technical appendix covering the child cognitive burden envelope and its limits.'
    },
]

DOC_TEMPLATE = Template("""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{{ page.title }} — Regina Lead Service Connections</title>
  <meta name=\"description\" content=\"{{ page.description }}\" />
  <meta name=\"theme-color\" content=\"#0f4c81\" />
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"> 
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap\" rel=\"stylesheet\">
  <link rel=\"stylesheet\" href=\"../styles.css\" />
</head>
<body>
  <main class=\"wrap page-shell\">
    <div class=\"topbar\">
      <div class=\"pill\">Regina Lead Service Connections</div>
      <div>{{ page.kicker }}</div>
    </div>

    <article class=\"doc-article\">
      <div class=\"breadcrumbs\"><a href=\"../index.html\">← Back to main page</a></div>
      <header class=\"doc-header\">
        <div class=\"kicker\">{{ page.kicker }}</div>
        <h1>{{ page.title }}</h1>
        <p class=\"meta-note\">{{ page.description }}</p>
      </header>
      {{ body | safe }}
    </article>
  </main>
</body>
</html>
""")


def convert(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=['extra', 'tables', 'fenced_code', 'sane_lists', 'toc']
    )


def main():
    for page in PAGES:
        src = REPORTS / page['source']
        out = REPORTS / page['output']
        body = convert(src.read_text())
        out.write_text(DOC_TEMPLATE.render(page=page, body=body))
        print(f'wrote {out.name}')


if __name__ == '__main__':
    main()
