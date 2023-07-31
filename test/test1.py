from utils.test.TestAnnotation import Test
from utils.test.Constants import OnFail


@Test(
    name="Test should pass if request is 2xx",
    onFail=OnFail.STOP_CURRENT,
    foundThat=["bello", "interessante"],
    willEnsureThat=["qwer", "reqw"]
)
def test_request():
    print("This is a test stampa")
    return "This is a test"