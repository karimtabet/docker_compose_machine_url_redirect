from datetime import datetime

from flask.ext.testing import TestCase
from hamcrest import assert_that, is_, has_length

from app import app, db, get_redirect
from models import Base, Redirect, User
from utils import get_random_string, add_http_to_url


class TestRedirects(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.app = app.test_client()

        for table in reversed(Base.metadata.sorted_tables):
            db.session.execute(table.delete())

    def insert_user(self):
        user = User(name='Test User')
        db.session.add(user)
        db.session.commit()
        return user

    def insert_redirect(self):
        user = self.insert_user()
        redirect = Redirect(
            from_url='test_url',
            to_url='https://www.example.com',
            times_accessed=0,
            created_by=user.uuid.hex,
            date_created=datetime.utcnow()
        )
        db.session.add(redirect)
        return redirect

    def test_get_redirect(self):
        self.insert_redirect()
        assert_that(
            get_redirect('test_url').to_url,
            is_('https://www.example.com')
        )

    def test_increment_times_accessed(self):
        self.insert_redirect()
        assert_that(
            get_redirect('test_url').times_accessed,
            is_(1)
        )

    def test_get_random_string(self):
        assert_that(
            get_random_string(),
            has_length(23)
        )

    def test_add_http_to_url(self):
        assert_that(
            add_http_to_url('www.example.com'),
            is_('http://www.example.com')
        )

    def test_add_http_to_url_already_containing_http(self):
        assert_that(
            add_http_to_url('http://www.example.com'),
            is_('http://www.example.com')
        )

    def test_successful_redirect(self):
        self.insert_redirect()
        response = self.app.get('/to/test_url')
        assert_that(
            response.status_code,
            is_(302)
        )
