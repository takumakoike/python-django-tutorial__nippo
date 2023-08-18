from django.test import TestCase

# Create your tests here.
def test_listview_with_anonymous(self):
    url = reverse("nippo-list")
    response = self.client.get(url)
    object_list = response.context_data["object_list"]
    self.assertEqual(len(object_list), 0)

def test_listview_with_own_user(self):
    url = reverse("nippo-list")
    self.client.login(email=self.email, password=self.password)
    response = self.client.get(url)
    object_list = response.context_data["object_list"]
    self.assertEqual(len(object_list), 1)