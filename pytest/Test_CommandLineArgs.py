


# pytest test_case1.py - run the testcases with the name
# pytest -vv -s test_case.py  - -v verbose Shows detailed output ,-s Show Print Statements
# pytest test_case.py -v -s --html=test_case1_report.html - generate the html report
# pytest .\test_parallel.py -n 4 --html=report.html  - run in parllel with 4 workers
# pytest -m smoke - -m - run the smoke testcases
# pytest -m "smoke and api" -run the smoke and apis both  testcases
# pytest -m "not regression" except regression run everything else
# pytest -k login  - run  teh testcase starting with login
# pytest --lf Run Last Failed Tests
# pytest tests/api/   run all the testcases under api  folder
# pytest login.py::test_valid_login - Run specific test inside file:
# pytest -x -Stop After First Failure
