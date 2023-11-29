# main/tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import (
    index, about, contact, courses, dashboard_home, profile, courses_enrolled,
    courses_uploaded, upload, course_edit, delete_course, course_details,
    category, course_search
)

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_courses_url_resolves(self):
        url = reverse('courses')
        self.assertEqual(resolve(url).func, courses)

    def test_dashboard_home_url_resolves(self):
        url = reverse('dashboard-home')
        self.assertEqual(resolve(url).func, dashboard_home)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_courses_enrolled_url_resolves(self):
        url = reverse('courses-enrolled')
        self.assertEqual(resolve(url).func, courses_enrolled)

    def test_courses_uploaded_url_resolves(self):
        url = reverse('courses-uploaded')
        self.assertEqual(resolve(url).func, courses_uploaded)

    def test_upload_url_resolves(self):
        url = reverse('uploade')
        self.assertEqual(resolve(url).func, upload)

    def test_course_edit_url_resolves(self):
        url = reverse('course-edit', args=['course_edit'])
        self.assertEqual(resolve(url).func, course_edit)
    

    def test_delete_course_url_resolves(self):
        url = reverse('delete-course', args=['delete_course'])
        self.assertEqual(resolve(url).func, delete_course)

    def test_course_details_url_resolves(self):
        url = reverse('course_details', args=['instructor', 'course_slug'])
        self.assertEqual(resolve(url).func, course_details)

    def test_category_url_resolves(self):
        url = reverse('category', args=['category'])
        self.assertEqual(resolve(url).func, category)

    def test_course_search_url_resolves(self):
        url = reverse('course_search')
        self.assertEqual(resolve(url).func, course_search)
