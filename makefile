test:
	PYTHONPATH=. pytest --alluredir=allure-results

report:
	allure generate allure-results -o allure-report --clean && open allure-report/index.html

serve:

	allure serve allure-results

clean:
	rm -rf allure-results allure-report

all:
	make clean && make serve