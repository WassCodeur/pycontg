hmlt_template = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Email Template</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #f4f6f8;
      font-family: Arial, sans-serif;
    }

    .container {
      width: 100%;
      padding: 20px 0;
      display: flex;
      justify-content: center;
    }

    .email-card {
      width: 100%;
      max-width: 600px;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    .header {
      padding: 20px;
      text-align: center;
      color: #ffffff;
      font-size: 20px;
      font-weight: bold;
    }

    .content {
      padding: 25px;
      color: #333333;
      line-height: 1.6;
      font-size: 15px;
    }

    .content h1 {
      font-size: 18px;
      margin-bottom: 10px;
    }

    .button-container {
      text-align: center;
      margin: 25px 0;
    }

    .cta-button {
      background-color: #9bc6a6;
      color: #ffffff !important;
      padding: 12px 20px;
      text-decoration: none;
      border-radius: 5px;
      display: inline-block;
      font-weight: bold;
    }

    .cta-button:hover {
      background-color: #84b495;
    }

    .footer {
      background-color: #f0f0f0;
      padding: 20px;
      text-align: center;
      font-size: 13px;
      color: #848e9c;
    }

    .signature {
      margin-top: 30px;
    }

    @media only screen and (max-width: 600px) {
      .content {
        padding: 15px;
      }
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="email-card">

      <!-- HEADER -->
            <div class="header">
                <img src="https://res.cloudinary.com/dvg7vky5o/image/upload/v1774223918/5_mvgkea.png" alt="Logo"
                    style="height: 300px; display:block; margin:0 auto 10px; width: 300px;">
            </div>


      <!-- CONTENT -->
      <div class="content">
        <h1>{{TITLE}}</h1>

        <p>Bonjour {{USER_NAME}},</p>

        <p>
          {{MAIN_MESSAGE}}
        </p>

        <!-- CTA BUTTON -->
        {{action_button}}

        <p>
          {{SECONDARY_MESSAGE}}
        </p>

        <!-- SIGNATURE -->
        <div class="signature">
          <p>Cordialement,</p>
          <p><strong>L'équipe {{APP_NAME}}</strong></p>
        </div>
      </div>

      <!-- FOOTER -->
      <div class="footer">
        <p>{{FOOTER_TEXT}}</p>
        <p>
          <a href="{{UNSUBSCRIBE_LINK}}" style="color:#848e9c; text-decoration: underline;">
            Se désinscrire
          </a>
        </p>
      </div>

    </div>
  </div>

</body>
</html>
"""


def generate_action_button(action_url, action_text):
    if action_url and action_text:
        return f"""
        <div class="button-container">
          <a href="{action_url}" class="cta-button">{action_text}</a>
        </div>
        """
    return ""


def generate_email_content(business_name, message_content, second_message_content, action_url=None, action_text=None):
    action_button = generate_action_button(action_url, action_text)
    return hmlt_template.replace("{{APP_NAME}}", business_name) \
        .replace("{{TITLE}}", "Notification de " + business_name) \
        .replace("{{USER_NAME}}", "Utilisateur") \
        .replace("{{MAIN_MESSAGE}}", message_content) \
        .replace("{{SECONDARY_MESSAGE}}", second_message_content) \
        .replace("{{action_button}}", action_button) \
        .replace("{{FOOTER_TEXT}}", f"Vous recevez cet email car vous êtes inscrit sur {business_name}.") \
        .replace("{{UNSUBSCRIBE_LINK}}", "https://www.pycontg.pytogo.org/unsubscribe")


if __name__ == "__main__":
    # Example usage
    html_content = generate_email_content(
        business_name="PyCon Togo",
        message_content="Merci de vous être inscrit à PyCon Togo ! Nous sommes ravis de vous compter parmi nous.",
        second_message_content="Restez à l'écoute pour plus d'informations sur les conférenciers, les ateliers et les activités passionnantes à venir.",
    )
    print(html_content)
