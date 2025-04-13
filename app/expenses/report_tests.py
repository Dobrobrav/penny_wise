from expenses.report_generators import Report


def test_report() -> None:
    Report(content='test_report_content')
