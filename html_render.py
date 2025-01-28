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


def get_welcome_message():
    return """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Welcome to Your Personal Job Search Journey</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #EEF2FF;">
  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background: linear-gradient(to bottom, #EEF2FF, #FFFFFF);">
    <tr>
      <td align="center" style="padding: 40px 0;">
        <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
          <!-- Hero Section -->
          <tr>
            <td align="center" style="padding-bottom: 40px;">
              <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                </tr>
                <tr>
                  <td align="center" style="padding-bottom: 20px;">
                    <h1 style="font-family: Arial, sans-serif; font-size: 32px; line-height: 1.2; margin: 0; color: #111827;">
                      Welcome to Your Personal<br/>
                      <span style="color: #4F46E5;">Job Search Journey</span> 🎉
                    </h1>
                  </td>
                </tr>
                <tr>
                  <td align="center" style="padding-bottom: 40px;">
                    <p style="font-family: Arial, sans-serif; font-size: 18px; line-height: 1.5; color: #4B5563; margin: 0; max-width: 480px;">
Find your next job easily with our app. We search the internet based on what you're looking for and send the best jobs straight to your email. Let us help you find the perfect job so you can focus on what matters most—growing your career. Happy job hunting!                    </p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Preferences Summary Box -->
          <tr>
            <td style="padding-top: 0px;">
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #EEF2FF; padding: 32px; border-radius: 16px;">
                <tr>
                  <td>
                    <h2 style="font-family: Arial, sans-serif; font-size: 24px; color: #111827; margin: 0 0 16px 0;">
                      Your Job Match Criteria
                    </h2>
                    <p style="font-family: Arial, sans-serif; font-size: 16px; color: #4B5563; margin: 0 0 24px 0;">
                      We'll tailor every recommendation based on your:
                    </p>
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                      <tr>
                        <td width="50%" style="padding: 0 12px 16px 0;">
                          <table border="0" cellpadding="0" cellspacing="0">
                            <tr>
                              <td width="20" style="padding-right: 12px;">
                                <span style="font-size: 20px; line-height: 1;">💼</span>
                              </td>
                              <td style="font-family: Arial, sans-serif; font-size: 14px; color: #374151;">
                                Selected Role
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td width="50%" style="padding: 0 0 16px 12px;">
                          <table border="0" cellpadding="0" cellspacing="0">
                            <tr>
                              <td width="20" style="padding-right: 12px;">
                                <span style="font-size: 20px; line-height: 1;">🏢</span>
                              </td>
                              <td style="font-family: Arial, sans-serif; font-size: 14px; color: #374151;">
                                Industry Preferences
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td width="50%" style="padding: 0 12px 16px 0;">
                          <table border="0" cellpadding="0" cellspacing="0">
                            <tr>
                              <td width="20" style="padding-right: 12px;">
                                <span style="font-size: 20px; line-height: 1;">📍</span>
                              </td>
                              <td style="font-family: Arial, sans-serif; font-size: 14px; color: #374151;">
                                Location Requirements
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td width="50%" style="padding: 0 0 16px 12px;">
                          <table border="0" cellpadding="0" cellspacing="0">
                            <tr>
                              <td width="20" style="padding-right: 12px;">
                                <span style="font-size: 20px; line-height: 1;">⭐</span>
                              </td>
                              <td style="font-family: Arial, sans-serif; font-size: 14px; color: #374151;">
                                Experience Level
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Call to Action -->
          <tr>
            <td align="center" style="padding-top: 40px;">
              <h2 style="font-family: Arial, sans-serif; font-size: 24px; color: #111827; margin: 0 0 24px 0;">
                Watch your inbox tomorrow for your first personalized job matches!
              </h2>
              <table border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center" style="border-radius: 6px;" bgcolor="#4F46E5">
                    <a href="https://yourjobfinder.website" target="_blank" style="font-family: Arial, sans-serif; font-size: 16px; color: #FFFFFF; text-decoration: none; padding: 12px 24px; border: 1px solid #4F46E5; display: inline-block; border-radius: 6px;">
                      <span style="font-size: 16px; line-height: 1; display: inline-block; vertical-align: middle; margin-right: 8px;">⚙️</span>
                      Create New Job Alert
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td align="center" style="padding-top: 40px;">
              <p style="font-family: Arial, sans-serif; font-size: 12px; color: #6B7280; margin: 0;">
                © 2025 Your Job Finder. All rights reserved. This Project is for educational purposes.
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


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
    unsubscribe_url = "https://yourjobfinder.website/unsubscribe/process"  # Replace with your unsubscribe URL

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
          <a class="unsubscribe-button" href="{unsubscribe_url}?email={email}&position={position}&location={location}">Unsubscribe</a>

        </td>
      </tr>
    </table>

    <script>
      function unsubscribe() {{
          fetch("{unsubscribe_url}?email={email}&position={position}&location={location}", {{
              method: 'GET',
              headers: {{
                  'Content-Type': 'application/json'
              }}
          }})
          .then(response => {{
              if (response.ok) {{
              }} else {{
                  alert('There was an error. Please try again later.');
              }}
          }})
          .catch(error => {{
              alert('There was a Network error!');
          }});
      }}
    </script>
</body>
</html>
"""
    return html_template
