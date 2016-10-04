from django.test import TestCase, Client

#run pylint on the given file
from pylint import lint
from pylint.reporters.text import TextReporter

# Create your tests here.

class WritableObject(object):
    "dummy output stream for pylint"
    def __init__(self):
        self.content = []
    def write(self, st):
        "dummy write"
        self.content.append(st)
    def read(self):
        "dummy read"
        return self.content
    def reset(self):
        self.content = []


class StaticAnalysis(TestCase):

    def get_analysis_score(self, pylint_output):
        last_line = filter(None, [s.strip() for s in pylint_output.read()])[-1]
        score = float(last_line.split()[6].split('/')[0])
        return score

    def static_analysis_run(self, files):
        pylint_output = WritableObject()
        for filename in files:
            pylint_output.reset()
            lint.Run([filename], reporter=TextReporter(pylint_output), exit=False)
            score = self.get_analysis_score(pylint_output)
            self.assertEqual(score, abs(score))

    def test_static_analysis(self):
        files = ['index_app/models.py', 'index_app/views.py']
        self.static_analysis_run(files)


class ViewsTester(TestCase):

    def test_index_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)