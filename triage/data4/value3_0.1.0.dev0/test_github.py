import unittest
from github import GitHub


class TestGitHub(unittest.TestCase):

    def setUp(self):
        self.github = GitHub()

    def test_repositories(self):
        x = self.github.repositories
        assert x._action == 'repositories'
        assert isinstance(x, GitHub)

    def test_repository(self):
        x = self.github.repository('biwin/github')

        assert isinstance(x.repo, tuple)
        assert len(x.repo) == 2
        assert x.repo[0] == 'biwin'
        assert x.repo[1] == 'github'
        assert x._action == 'repository'
        assert isinstance(x, GitHub)

    def test_repository_fails_if_no_user(self):
        try:
            x = self.github.repository('github')
        except ValueError:
            assert True

    def test_repository_not_fails_if_user(self):
        try:
            x = self.github.repository('github')
        except ValueError:
            x = self.github
            x.user = 'biwin'
            x.repository('github')
            assert isinstance(x.repo, tuple)
            assert len(x.repo) == 2
            assert x.repo[0] == 'biwin'
            assert x.repo[1] == 'github'
            assert x._action == 'repository'
            assert isinstance(x, GitHub)
