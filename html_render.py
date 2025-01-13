import random

greetings = [
    "Here are some exciting job opportunities we found for you! 🚀",
    "Great news! Check out these potential job matches for you! 🎉",
    "We’ve found some jobs that might interest you. Take a look! 👀",
    "Explore these job openings tailored for you! 🔍",
    "Here's a list of jobs that could be your next big opportunity! 🌟",
    "These jobs caught our attention. We hope they pique yours too! 📌",
    "Discover these job possibilities that align with your criteria! 📈",
    "Look at the career opportunities we’ve gathered for you! 🗂️",
    "Unlock your potential with these job listings we found! 🔑",
    "We’ve curated these job options just for you. Happy exploring! 😊"
]


def create_job_card(row):
    new_badge = "<span style='display: inline-block; background-color: #dcfce7; color: #15803d; padding: 2px 8px; border-radius: 9999px; font-size: 12px; margin-left: 8px;'>New</span>" if \
        row['new_badge'] else ""

    salary_info = f"<p style='padding: 0 0 4px 0; font-size: 14px; color: #4b5563;'>💰 {row.get('min_amount', '')} - {row.get('max_amount', '')}</p>" if \
        row['has_salary'] else ""

    html_card = f"""
    <table cellpadding="0" cellspacing="0" style="width: 100%; margin-bottom: 20px; border-collapse: collapse; background-color: #ffffff; border: 1px solid #e5e7eb; border-radius: 8px;">
        <tr>
            <td style="padding: 16px;">
                <table cellpadding="0" cellspacing="0" style="width: 100%;">
                    <tr>
                        <td>
                            <h2 style="padding: 0; font-size: 18px; color: #1f2937; font-weight: 600; margin-bottom: 8px;">
                                {row['title']}
                                {new_badge}  <!-- Include new badge conditionally -->
                            </h2>
                            <p style="padding: 0; font-size: 14px; color: #4b5563;">{row['company']}</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding-top: 12px;">
                            <p style="padding: 0 0 4px 0; font-size: 14px; color: #4b5563;">📍 {row['location']}</p>
                            {salary_info}  
                            <p style="padding: 0; font-size: 14px; color: #4b5563;">💻 {'Remote' if row['job_type'] else 'Not Remote'}</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td style="border-top: 1px solid #e5e7eb; padding: 12px 16px; background-color: #f9fafb;">
                <table cellpadding="0" cellspacing="0" style="width: 100%;">
                    <tr>
                        <td style="font-size: 12px; color: #6b7280;">Posted on {row['date_posted'] if row['date_posted'] else 'this Week'}</td>
                        <td align="right">
                            <a href="{row['job_url']}" style="background-color: #3b82f6; color: #ffffff; padding: 8px 16px; text-decoration: none; border-radius: 6px; font-size: 14px;">View Job</a>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    """
    return html_card


def get_html_template(html_content, email, position, location):
    unsubscribe_url = "https://example.com"  # Replace with your unsubscribe URL
    unsubscribe_data = {"email": email,
                        "position": position,
                        "location": location}  # Replace with the necessary parameters

    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Opportunities</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #f3f4f6;
            padding: 0;
            margin: 0;
        }}
        .email-container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
        }}
        .job-card {{
            border-bottom: 1px solid #e5e7eb;
            padding: 16px 0;
        }}
        .unsubscribe-button {{
            display: inline-block;
            background-color: #FF4041;
            color: #ffffff;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 6px;
            font-size: 14px;
            margin-top: 20px;
        }}
        .unsubscribe-text {{
            font-size: 12px;
            color: #6b7280;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <table cellpadding="0" cellspacing="0" style="
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      background-color: #f3f4f6;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    ">
      <tr>
        <td style="padding: 32px 24px;">
          <table cellpadding="0" cellspacing="0" style="width: 100%; margin-bottom: 24px;">
            <tr>
              <td>
                <h1 style="
                  margin: 0 0 8px;
                  font-size: 24px;
                  font-weight: bold;
                  color: #1f2937;
                ">{random.choice(greetings)}</h1>
              </td>
            </tr>
          </table>

          <div class="email-container">
            {html_content}
          </div>
           <p class="unsubscribe-text">Don't want to receive these emails anymore?</p>
          <button class="unsubscribe-button" onclick="unsubscribe()">Unsubscribe</button>

        </td>
      </tr>
    </table>

    <script>
      function unsubscribe() {{
          fetch("{unsubscribe_url}", {{
              method: 'DELETE',
              headers: {{
                  'Content-Type': 'application/json'
              }},
              body: JSON.stringify({unsubscribe_data})
          }})
          .then(response => {{
              if (response.ok) {{
                  alert('Successfully unsubscribed.');
              }} else {{
                  alert('There was an error. Please try again later.');
              }}
          }})
          .catch(error => {{
              alert('Network error: ' + error.message);
          }});
      }}
    </script>
</body>
</html>
"""
    return html_template
