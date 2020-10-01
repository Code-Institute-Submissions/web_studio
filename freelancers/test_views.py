from django.test import TestCase
from django.urls import reverse

from .models import Freelancer


def test_can_freelancer_register(self):
    # freelancer is creating account
    response = self.client.post('/register_freelancer/', {
        'name': 'Name',
        'email': 'email@email',
        'password': 'password',
        'skills': 'skills',
        'portfolio_link': 'portfolio_link',
        'about': 'about'})

    self.assertRedirects(response, '/accounts/login/')
    # we will log him in with his credential
    self.client.login(username='Name', password='password')
    response = self.client.get('/freelancer/')
    self.assertTemplateUsed(response, 'freelancers/freelancer.html')

def test_edit_freelancer(self):
    # CREATING freelancer
    self.freelancer = Freelancer.objects.create(
        name='freelancer name',
        email='some@email.com',
        skills='Python, Django',
        about='about',
        password='password',
        portfolio_link='portfolio_link',
    )

    # get newly created freelancer
    freelancer = Freelancer.objects.get(id=self.freelancer.id)
    # assert it is right one
    self.assertEqual(freelancer.about, 'about')
    # https://stackoverflow.com/a/58242905 self.freelancer.id

    # getting form with the freelancer
    freelancer_id = self.freelancer.id
    update_url = reverse('update_freelancer', args=(freelancer_id,))

    request = self.client.get(update_url)

    form = request.context['form']
    data = form.initial

    # EDITING freelancer
    data['about'] = 'updated about'

    # posting the form
    self.client.post(update_url, data)

    # retrieving the form and checking for updated value
    request = self.client.get(update_url)

    self.assertEqual(request.context['form'].initial['about'], 'updated about')

    # check that we have 1 freelancer
    freelancers = Freelancer.objects.all()
    self.assertTrue(len(freelancers) == 1)


