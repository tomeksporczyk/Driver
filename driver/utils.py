from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def create_email_message(mail_subject, html_dir, user, variables_dict):
    '''

    :param mail_subject: str - email subject, nothing more
    :param html_dir: str - html template's dir
    :param user: user instance - for email address
    :param variables_dict: dictionary - variables used in the html template
    :return:
    '''
    message = render_to_string(html_dir, variables_dict)
    return EmailMessage(mail_subject, message, to=[user.email])