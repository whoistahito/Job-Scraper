from datetime import datetime
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
                                <span style="font-size: 20px; line-height: 1;">⭐</span>
                              </td>
                              <td style="font-family: Arial, sans-serif; font-size: 14px; color: #374151;">
                                Job type Preferences
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
    """
    Creates an HTML job card from a pandas DataFrame row.

    Expected columns in row:
    - title: str
    - company: str
    - location: str
    - date_posted: datetime or str
    - is_remote: bool
    - job_url: str
    - new_badge: bool (optional)
    """
    # Convert date to proper format if it's a string or datetime
    if isinstance(row['date_posted'], datetime):
        posted_date = row['date_posted'].strftime('%d/%m/%Y')
    else:
        posted_date = 'this Week'

    # New badge HTML - only show if is_new is True
    new_badge = '''
    <tr>
        <td style="padding-top: 8px;">
            <span style="display: inline-block; background-color: #DCFCE7; color: #15803D; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: 600;">● New</span>
        </td>
    </tr>
    ''' if row.get('new_badge', False) else ''

    # Remote badge - only show if remote is True
    remote_badge = '''
    <tr>
        <td style="padding-bottom: 12px;">
            <span style="display: inline-block; background-color: #EEF2FF; color: #4F46E5; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: 500;">Remote</span>
        </td>
    </tr>
    ''' if row['is_remote'] else ''

    return f'''
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #F8FAFF; border: 1px solid #E5E7EB; border-radius: 12px; margin-bottom: 16px;">
        <tr>
            <td style="padding: 20px;">
                <!-- Job Title and New Badge -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 12px;">
                    <tr>
                        <td>
                            <h2 style="color: #1F2937; font-size: 18px; margin: 0; font-weight: 600;">{row['title']}</h2>
                        </td>
                    </tr>
                    {new_badge}
                </table>

                <!-- Company Name -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 12px;">
                    <tr>
                        <td>
                            <p style="color: #4B5563; font-size: 16px; margin: 0; font-weight: 500;">{row['company']}</p>
                        </td>
                    </tr>
                </table>

                <!-- Location and Date -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 12px;">
                    <tr>
                        <td>
                            <p style="color: #6B7280; font-size: 14px; margin: 0 0 8px 0;">📍 {row['location']}</p>
                            <p style="color: #6B7280; font-size: 14px; margin: 0;">🕒 Posted: {posted_date}</p>
                        </td>
                    </tr>
                </table>

                <!-- Remote Badge and Button -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    {remote_badge}
                    <tr>
                        <td>
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                    <td>
                                        <a href="{row['job_url']}" style="display: inline-block; background-color: #4F46E5; color: #ffffff; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 500; text-align: center; width: 100%; box-sizing: border-box;">View Details →</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    '''


def get_html_template(html_content, email, position, location):
    """
    Creates the complete HTML email template with the job cards content.

    Args:
        html_content (str): The concatenated job cards HTML
        email (str): The recipient's username/email
        position (str) : preferred job position
        location (str) : preferred job location
    Returns:
        str: Complete HTML email template
    """
    unsubscribe_url = "https://yourjobfinder.website/unsubscribe/process"
    return f'''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>Job Listings</title>
        <!--[if mso]>
        <style type="text/css">
        body, table, td {{font-family: Arial, Helvetica, sans-serif !important;}}
        </style>
        <![endif]-->
    </head>
    <body style="margin: 0; padding: 0; background-color: #F3F4F6; -webkit-font-smoothing: antialiased;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #F3F4F6; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
            <tr>
                <td align="center" style="padding: 24px 12px;">
                    <!-- Main Container -->
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); max-width: 600px;">
                        <!-- Header with Logo -->
                        <tr>
                            <td style="padding: 32px 24px; background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%); border-radius: 12px 12px 0 0;">
                                <h1 style="color: #ffffff; font-size: 24px; margin: 0; font-weight: 700;">Job Alerts</h1>
                                <p style="color: #E0E7FF; font-size: 16px; margin: 8px 0 0 0;">Latest opportunities for you</p>
                            </td>
                        </tr>

                        <!-- Welcome Message -->
                        <tr>
                            <td style="padding: 24px;">
                                <h2 style="color: #4B5563; font-size: 16px; margin: 12px 0 0 0; line-height: 1.5;">{random.choice(greetings)}</h2>
                            </td>
                        </tr>

                        <!-- Job Cards Container -->
                        <tr>
                            <td style="padding: 0 24px;">
                                {html_content}
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="padding: 32px 24px; border-top: 1px solid #E5E7EB;">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td align="center">
                                            <p style="color: #6B7280; font-size: 14px; margin: 0 0 16px 0;">Prefer not to receive these updates?</p>
                                            <a href="href="{unsubscribe_url}?email={email}&position={position}&location={location}">Unsubscribe" style="color: #4B5563; text-decoration: underline; font-size: 14px;">Unsubscribe</a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>

                    <!-- Footer Message -->
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                        <tr>
                            <td align="center" style="padding: 24px 12px;">
                                <p style="color: #6B7280; font-size: 12px; margin: 0;">This email was sent by Job Board. Please do not reply to this email.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    '''
