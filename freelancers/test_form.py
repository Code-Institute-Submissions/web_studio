from django.test import TestCase

from .forms import FreelancerForm


class TestFreelancerForm(TestCase):
    def test_freelancer_name_is_required(self):
        form = FreelancerForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_on_the_job_field_is_not_required(self):
        form = FreelancerForm(
            {
                'name': 'First Freelancer',
                'phone_num': '0987876',
                'email': 'some@email.com',
                'about': 'I want that job',
                'skills': 'Python, Flask, Django, Jquery, MongoDB',
                'portfolio_link': 'link_to_portfolio',
                'password': 'big password',
                'on_the_job': False,
            }
        )

        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = FreelancerForm()
        self.assertEqual(form.Meta.fields,
                         ('name', 'email', 'about', 'skills', 'portfolio_link', 'phone_num'))
