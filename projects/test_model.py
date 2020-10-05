from django.test import TestCase

from .models import Project


class TestModels(TestCase):

    def test_project_progress_steps_default_to_false(self):
        project = Project.objects.create(project_number='CERVFER546575HGHTY65756734')

        self.assertFalse(project.started)
        self.assertFalse(project.wireframes)
        self.assertFalse(project.update_after_wireframes)
        self.assertFalse(project.started_on_site)
        self.assertFalse(project.development_link_sent)
        self.assertFalse(project.development_link)
        self.assertFalse(project.client_approved)
        self.assertFalse(project.domain_hosting)
        self.assertFalse(project.done)

    def test_project_string_method_returns_project_number(self):
        item = Project.objects.create(project_number='DERFCBHER73465BCVGFERYGFC742386')
        self.assertEqual(str(item), 'DERFCBHER73465BCVGFERYGFC742386')
