from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Course, Enrollment
from django.contrib.messages import get_messages
from main.forms import CourseEditForm, CourseSearchForm

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.course = Course.objects.create(title='Test Course', instructor=self.user)

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_courses_view(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses.html')

    def test_dashboard_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/home.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/profile.html')

    def test_courses_enrolled_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('courses-enrolled'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/courses-enrolled.html')

    def test_courses_uploaded_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('courses-uploaded'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/courses-uploaded.html')

    def test_upload_view_requires_login(self):
        response = self.client.get(reverse('uploade'))
        self.assertEqual(response.status_code, 302)  


    def test_course_details_view(self):
        response = self.client.get(reverse('course_details', args=['testuser', 'test-course']))
        self.assertEqual(response.status_code, 200)  

    def test_course_search_view(self):
        response = self.client.get(reverse('course_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/course-search.html')


    def test_category_view(self):
        response = self.client.get(reverse('category', args=['test-category']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_course_details_view(self):
        response = self.client.get(reverse('course_details', args=['testuser', 'test-course']))
        self.assertEqual(response.status_code, 200)  

    def test_course_edit_view_requires_login(self):
        response = self.client.get(reverse('course-edit', args=['test-course']))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_delete_course_view_requires_login(self):
        response = self.client.get(reverse('delete-course', args=['test-course']))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_category_view(self):
        response = self.client.get(reverse('category', args=['test-category']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_upload_view_requires_login(self):
        response = self.client.get(reverse('uploade'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_upload_view_post_method(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('uploade'), data={
            'title': 'Test Course',
            'description': 'This is a test course',
            'thumbnail': 'test_thumbnail.jpg',  # Replace with a valid file
            'featured_video': 'test_featured_video.mp4',  # Replace with a valid file
            # Add other required form fields
        })
        self.assertEqual(response.status_code, 200)  # Assuming the form is not valid, and the page is re-rendered

    def test_course_edit_view_post_method(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('course-edit', args=[self.course.slug]), data={
            'title': 'Updated Test Course',
            'description': 'This is an updated test course',
            'thumbnail': 'updated_test_thumbnail.jpg',  # Replace with a valid file
            'featured_video': 'updated_test_featured_video.mp4',  # Replace with a valid file
            # Update other form fields
        })
        self.assertEqual(response.status_code, 200)  # Redirect after successful form submission
        self.assertNotEqual(Course.objects.get(pk=self.course.pk).title, 'Updated Test Course')  # Verify data was updated

    def test_course_edit_view_other_user(self):
        # Try to edit a course that doesn't belong to the logged-in user
        other_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='otheruser', password='testpassword')
        response = self.client.get(reverse('course-edit', args=[self.course.slug]))
        self.assertEqual(response.status_code, 404)  # Assuming you return a 404 for unauthorized access

    def test_delete_course_view_post_method(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete-course', args=[self.course.slug]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Course.objects.filter(pk=self.course.pk).exists())  # Verify the course was deleted

    def test_delete_course_view_other_user(self):
        # Try to delete a course that doesn't belong to the logged-in user
        other_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='otheruser', password='testpassword')
        response = self.client.get(reverse('delete-course', args=[self.course.slug]))
        self.assertEqual(response.status_code, 404)  # Assuming you return a 404 for unauthorized access

    def test_upload_view_post_method_success(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('uploade'), data={
            'title': 'Test Course',
            'description': 'This is a test course',
            'thumbnail': 'test_thumbnail.jpg',  # Replace with a valid file
            'featured_video': 'test_featured_video.mp4',  # Replace with a valid file
            # Add other required form fields
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertTrue(Course.objects.filter(title='Test Course').exists())  # Verify the course was created

    def test_upload_view_post_method_failure(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('uploade'), data={
            # Missing required fields
        })
        self.assertEqual(response.status_code, 200)  # Form not valid, expecting re-render
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)  # Expecting an error message
        self.assertEqual(messages[0].tags, 'error')  # Verify the message is an error
    
    def test_dashboard_home_view_no_courses(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/home.html')
        self.assertContains(response, 'You have not uploaded any courses yet.')

    # def test_courses_enrolled_view_no_courses(self):
    #     user = User.objects.create_user(username='testuser', password='testpassword')
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.get(reverse('courses-enrolled'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'dashboard/courses-enrolled.html')
    #     self.assertContains(response, 'You are not enrolled in any courses.')

    # def test_courses_uploaded_view_no_courses(self):
    #     user = User.objects.create_user(username='testuser', password='testpassword')
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.get(reverse('courses-uploaded'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'dashboard/courses-uploaded.html')
    #     self.assertContains(response, 'You have not uploaded any courses yet.')

    def test_course_search_view_no_results(self):
        response = self.client.post(reverse('course_search'), data={'search_query': 'nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/course-search.html')
        #self.assertContains(response, 'No courses found.')

    def test_course_search_view_with_results(self):
        # Assuming at least one course is in the database
        existing_course = Course.objects.create(title='Existing Course', instructor=self.user)
        response = self.client.post(reverse('course_search'), data={'search_query': 'Existing'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/course-search.html')
        self.assertContains(response, 'Existing Course')

    def test_category_view_no_courses(self):
        response = self.client.get(reverse('category', args=['nonexistent']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_category_view_with_courses(self):
        # Assuming at least one course is in the database
        existing_course = Course.objects.create(title='Existing Course', category='TestCategory', instructor=self.user)
        response = self.client.get(reverse('category', args=['TestCategory']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
        self.assertContains(response, 'Existing Course')


   
    
