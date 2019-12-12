from HTTPClient import formatters
from colorama import Fore

def test_formatHeaders():
    result = formatters.formatHeaders({"test": "test2", "test1": "test2"})
    expected = """{}test{}: {}test2{}
{}test1{}: {}test2{}\n""".format(Fore.BLUE, Fore.RESET, Fore.GREEN, Fore.RESET, Fore.BLUE, Fore.RESET, Fore.GREEN, Fore.RESET)

    assert result == expected

def test_formatStatusCode():
    infoTestResult = formatters.formatStatusCode(100)
    succesTestResult = formatters.formatStatusCode(200)
    redirectionTestResult = formatters.formatStatusCode(300)
    clientErrorTestResult = formatters.formatStatusCode(400)
    serverErrorTestResult = formatters.formatStatusCode(500)

    infoTestExpected = Fore.BLUE + "100" + Fore.RESET + "(Info)"
    assert infoTestResult == infoTestExpected

    succesTestExpected = Fore.GREEN + "200" + Fore.RESET + "(Success)"
    assert succesTestResult == succesTestExpected

    redirectionTestExpected = Fore.YELLOW + "300" + Fore.RESET + "(Redirection)"
    assert redirectionTestResult == redirectionTestExpected

    clientErrorTestExpected = Fore.RED + "400" + Fore.RESET + "(Client Error)"
    assert clientErrorTestResult == clientErrorTestExpected

    serverErrorTestExpected = Fore.RED + "500" + Fore.RESET + "(Server Error)"
    assert serverErrorTestResult == serverErrorTestExpected