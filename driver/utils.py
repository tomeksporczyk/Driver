from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string

from driver.models import Advice, TestAnswer, Like


def create_mail_to_user(mail_subject, html_dir, user, variables_dict):
    '''

    :param mail_subject: str - email subject, nothing more
    :param html_dir: str - html template's dir
    :param user: user instance - for email address
    :param variables_dict: dictionary - variables used in the html template
    :return:
    '''
    message = render_to_string(html_dir, variables_dict)
    return EmailMessage(mail_subject, message, to=[user.email])


def check_quiz_answers(request, slug):
    ans = []
    questions = Advice.objects.get(slug=slug).testquestion_set.all()
    for question in questions:
        ans.append(request.POST.get(f'question-{question.id}'))
    print('ans', ans)
    player_points = 0
    max_points = sum([question.testanswer_set.get(is_truth=True).points for question in questions])
    for answer_id in ans:
        try:
            answer = TestAnswer.objects.get(pk=int(answer_id))
        except (ValueError, TypeError, TestAnswer.DoesNotExist):
            continue
        if answer.is_truth is True:
            player_points += answer.points
    user = request.user
    user.score.score += player_points
    user.save()
    Advice.objects.get(slug=slug).passed.add(request.user.pk)
    messages.success(request, f'Zdobyłaś/eś {player_points}, na {max_points} możliwych punktów')
    return redirect(f'/advice/{slug}')


def like_mechanism(request, slug, likes_number, bool_val):
    advice = Advice.objects.get(slug=slug)
    advice.likes += likes_number
    advice.save()
    like, created = Like.objects.get_or_create(user=request.user, advice=advice)
    like.like = bool_val
    like.save()
    return redirect(f'/advice/{slug}')