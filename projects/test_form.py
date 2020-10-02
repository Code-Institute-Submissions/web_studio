from django.test import TestCase

from .forms import ProjectForm


class TestprojectForm(TestCase):
    def test_project_number_is_required(self):
        form = ProjectForm({'project_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('project_number', form.errors.keys())
        self.assertEqual(form.errors['project_number'][0], 'This field is required.')

    def test_project_form_with_project_number_is_valid(self):
        form = ProjectForm({'project_number': 'SDWEFCR54654BFGBHB567BGFB'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProjectForm()
        self.assertEqual(form.Meta.fields,
                         ('project_number', 'development_link', 'started', 'wireframes', 'update_after_wireframes',
                          'started_on_site', 'development_link_sent', 'client_approved', 'domain_hosting', 'done'))
