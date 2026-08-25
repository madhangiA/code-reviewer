def get_review_prompt(code, language):

    return f"""
You are a Senior {language} Code Reviewer.

Analyze the following code and provide the output in EXACTLY the format below.

Submitted Code:

```{language.lower()}
{code}
```

Code Quality Score: <score>/10

Severity: Critical/High/Medium/Low

Bugs Found:
- Bug 1
- Bug 2

Bug Explanation:
- Explanation 1
- Explanation 2

Suggestions:
- Suggestion 1
- Suggestion 2

Fixed Code:

```{language.lower()}
<corrected code>
```
"""
