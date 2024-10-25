"""Define some fixtures to use in the project."""

import pytest
from Autoris import autoriz


def pytest_report_header():
    return "Thanks for running the tests"
def pytest_report_teststatus(report):
    if report.when=='call' and report.failed:
        return(report.outcome, '0', 'OPPORTUNITY for improvement')
def pytest_addoption(parser):
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
                    help="nice: turn failtures into opportunities")
@pytest.fixture()
def auto_():
    """All summaries and owners are unique."""
    return (
     ('a', 'one'),
     ('b', 'two'),
     ('b', 'Michelle'),
     ('c', 'one'))




